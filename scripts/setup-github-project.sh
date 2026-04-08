#!/usr/bin/env bash
#
# setup-github-project.sh — Bootstrap the GitHub Project (v2) for the
# Hitchhiker's Guide pipeline. Creates the project, custom fields, links it
# to the repo, and creates the three views described in docs/PROJECT-SETUP.md.
#
# Idempotency: this script is meant to run once. It detects an existing
# project with the same title and aborts rather than creating duplicates.
# Re-running after a partial failure is safe — already-created fields/views
# will report a conflict and be skipped.
#
# Required gh scopes: repo, project. If you see a scope error, run:
#   gh auth refresh -s project
#
# Usage:
#   ./scripts/setup-github-project.sh                 # uses defaults below
#   PROJECT_OWNER=steveash ./scripts/setup-github-project.sh
#
set -euo pipefail

PROJECT_OWNER="${PROJECT_OWNER:-steveash}"
PROJECT_TITLE="${PROJECT_TITLE:-Hitchhikers Guide Pipeline}"
REPO="${REPO:-steveash/hitchhikers-guide-to-ai-native-engineering}"

err() { printf 'error: %s\n' "$*" >&2; exit 1; }
note() { printf '\n>> %s\n' "$*"; }

command -v gh >/dev/null || err "gh CLI not found"
command -v jq >/dev/null || err "jq not found"

# Verify scopes
scopes=$(gh auth status 2>&1 | grep -o "Token scopes:.*" || true)
if ! echo "$scopes" | grep -q "project"; then
  err "gh token missing 'project' scope. Run: gh auth refresh -s project"
fi

# ---------------------------------------------------------------- create project
note "Looking up existing project '${PROJECT_TITLE}' under ${PROJECT_OWNER}"
existing=$(gh project list --owner "$PROJECT_OWNER" --format json 2>/dev/null \
  | jq -r --arg t "$PROJECT_TITLE" '.projects[] | select(.title == $t) | .number' \
  | head -1)

if [ -n "$existing" ]; then
  note "Project already exists as #${existing}. Reusing."
  PROJECT_NUMBER="$existing"
else
  note "Creating project '${PROJECT_TITLE}'"
  PROJECT_NUMBER=$(gh project create \
    --owner "$PROJECT_OWNER" \
    --title "$PROJECT_TITLE" \
    --format json | jq -r '.number')
  note "Created project #${PROJECT_NUMBER}"
fi

# Resolve project node id (needed for GraphQL view creation)
PROJECT_NODE_ID=$(gh project view "$PROJECT_NUMBER" --owner "$PROJECT_OWNER" --format json \
  | jq -r '.id')
[ -n "$PROJECT_NODE_ID" ] || err "could not resolve project node id"

# ----------------------------------------------------------------- link to repo
note "Linking project #${PROJECT_NUMBER} to ${REPO}"
gh project link "$PROJECT_NUMBER" --owner "$PROJECT_OWNER" --repo "$REPO" || \
  note "(link may already exist — continuing)"

# --------------------------------------------------------------- custom fields
# Triage status (single-select) — used by Source intake view
note "Creating custom field: Triage Status"
gh project field-create "$PROJECT_NUMBER" --owner "$PROJECT_OWNER" \
  --name "Triage Status" \
  --data-type SINGLE_SELECT \
  --single-select-options "untriaged,accepted,rejected,duplicate,in-progress,done" \
  2>&1 | grep -v "already exists" || true

# Assayer Check (single-select) — used by PR review queue view
note "Creating custom field: Assayer Check"
gh project field-create "$PROJECT_NUMBER" --owner "$PROJECT_OWNER" \
  --name "Assayer Check" \
  --data-type SINGLE_SELECT \
  --single-select-options "pending,running,passed,failed,skipped" \
  2>&1 | grep -v "already exists" || true

# Chapter (single-select) — used by Chapter health view
note "Creating custom field: Chapter"
gh project field-create "$PROJECT_NUMBER" --owner "$PROJECT_OWNER" \
  --name "Chapter" \
  --data-type SINGLE_SELECT \
  --single-select-options "ch00-principles,ch01-daily-workflows,ch02-harness-engineering,ch03-safety-and-verification,ch04-context-engineering,ch05-team-adoption,cross-cutting" \
  2>&1 | grep -v "already exists" || true

# ------------------------------------------------------------------------ views
# `gh project` does NOT support view creation as of 2026-04. Views must be
# created via the GraphQL API. The mutations below are best-effort: if your
# gh version's GraphQL schema lacks createProjectV2View, the script will
# print the equivalent click-by-click instructions and exit cleanly.
note "Creating views via GraphQL"

create_view() {
  local name="$1" layout="$2"
  gh api graphql -f query='
    mutation($projectId: ID!, $name: String!, $layout: ProjectV2ViewLayout!) {
      createProjectV2View(input: {projectId: $projectId, name: $name, layout: $layout}) {
        projectV2View { id name }
      }
    }' \
    -F projectId="$PROJECT_NODE_ID" \
    -F name="$name" \
    -F layout="$layout" 2>&1 || {
      note "createProjectV2View failed for '$name' — see docs/PROJECT-SETUP.md for manual steps"
      return 1
    }
}

create_view "Source intake"     "TABLE_LAYOUT" || true
create_view "PR review queue"   "BOARD_LAYOUT" || true
create_view "Chapter health"    "TABLE_LAYOUT" || true

note "Done. Project URL:"
echo "  https://github.com/users/${PROJECT_OWNER}/projects/${PROJECT_NUMBER}"
echo
echo "Next steps (manual — gh CLI cannot configure view filters/groupings):"
echo "  1. Open each view and apply the filter/group-by described in"
echo "     docs/PROJECT-SETUP.md §View Configuration."
echo "  2. Update README.md 'Pipeline Status' section with the project URL above."
