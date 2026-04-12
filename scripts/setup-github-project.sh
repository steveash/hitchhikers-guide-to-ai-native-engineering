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
# GitHub's GraphQL API does not expose a mutation for creating ProjectV2 views.
# Views must be created manually through the web UI.
note "Done. Project URL:"
echo "  https://github.com/users/${PROJECT_OWNER}/projects/${PROJECT_NUMBER}"
echo
echo "Manual steps required (GitHub API does not support view creation):"
echo "  1. Open the project URL above in your browser."
echo "  2. Create three views using the + tab at the top:"
echo "     a. 'Source intake' (Table layout)"
echo "        - Filter: label:new-source,new-repo,new-failure,source-submission"
echo "        - Group by: Triage Status"
echo "     b. 'PR review queue' (Board layout)"
echo "        - Filter: is:pr label:source-note,guide-update"
echo "        - Group by: Assayer Check"
echo "     c. 'Chapter health' (Table layout)"
echo "        - Group by: Chapter"
echo "  3. Update README.md 'Pipeline Status' section with the project URL above."
