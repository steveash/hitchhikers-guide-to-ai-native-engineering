#!/usr/bin/env bash
#
# bulk-add-to-project.sh — Add all existing issues and PRs to the GitHub
# Project (v2). Idempotent: items already in the project are skipped.
#
# Requires gh CLI with 'project' scope:
#   gh auth refresh -s project
#
# Usage:
#   ./scripts/bulk-add-to-project.sh              # uses defaults
#   PROJECT_NUMBER=1 ./scripts/bulk-add-to-project.sh
#
set -euo pipefail

PROJECT_OWNER="${PROJECT_OWNER:-steveash}"
PROJECT_NUMBER="${PROJECT_NUMBER:-1}"
REPO="${REPO:-steveash/hitchhikers-guide-to-ai-native-engineering}"

err() { printf 'error: %s\n' "$*" >&2; exit 1; }

command -v gh >/dev/null || err "gh CLI not found"
command -v jq >/dev/null || err "jq not found"

# Verify project scope
if ! gh project view "$PROJECT_NUMBER" --owner "$PROJECT_OWNER" >/dev/null 2>&1; then
  err "Cannot access project #${PROJECT_NUMBER}. Run: gh auth refresh -s project"
fi

echo "Adding all issues and PRs from ${REPO} to project #${PROJECT_NUMBER}..."
echo

ok=0
skip=0
fail=0

# Process issues
for number in $(gh issue list --repo "$REPO" --state all --json number --limit 1000 | jq -r '.[].number'); do
  url="https://github.com/${REPO}/issues/${number}"
  output=$(gh project item-add "$PROJECT_NUMBER" --owner "$PROJECT_OWNER" --url "$url" 2>&1) && {
    ok=$((ok + 1))
  } || {
    if echo "$output" | grep -qi "already"; then
      skip=$((skip + 1))
    else
      fail=$((fail + 1))
      [ "$fail" -le 3 ] && echo "  FAIL #${number}: ${output}" >&2
    fi
  }
  total=$((ok + skip + fail))
  [ $((total % 25)) -eq 0 ] && echo "  Progress: ${ok} added, ${skip} skipped, ${fail} failed (${total} processed)"
done

# Process PRs (separate from issues in gh CLI)
for number in $(gh pr list --repo "$REPO" --state all --json number --limit 1000 | jq -r '.[].number'); do
  url="https://github.com/${REPO}/pull/${number}"
  output=$(gh project item-add "$PROJECT_NUMBER" --owner "$PROJECT_OWNER" --url "$url" 2>&1) && {
    ok=$((ok + 1))
  } || {
    if echo "$output" | grep -qi "already"; then
      skip=$((skip + 1))
    else
      fail=$((fail + 1))
      [ "$fail" -le 3 ] && echo "  FAIL PR #${number}: ${output}" >&2
    fi
  }
done

echo
echo "Done: ${ok} added, ${skip} already present, ${fail} failed"
