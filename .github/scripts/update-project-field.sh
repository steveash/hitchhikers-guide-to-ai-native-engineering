#!/usr/bin/env bash
# Update a GitHub Projects V2 single-select field for an issue or PR.
#
# Usage: update-project-field.sh <NUMBER> <FIELD_ID> <OPTION_ID> [issue|pr]
#
# Requires GH_TOKEN with 'project' scope (typically secrets.PROJECT_PAT).
# Exits 0 on any failure so project board updates never break the pipeline.

set -uo pipefail

PROJECT_ID="PVT_kwHOABIwvc4BUXvu"
REPO="${GITHUB_REPOSITORY:-steveash/hitchhikers-guide-to-ai-native-engineering}"
OWNER="${REPO%%/*}"
REPO_NAME="${REPO##*/}"

NUMBER="${1:?Usage: update-project-field.sh <NUMBER> <FIELD_ID> <OPTION_ID> [issue|pr]}"
FIELD_ID="${2:?Missing FIELD_ID}"
OPTION_ID="${3:?Missing OPTION_ID}"
ITEM_TYPE="${4:-issue}"

if [ -z "${GH_TOKEN:-}" ]; then
  echo "::warning::PROJECT_PAT not configured — skipping project board update."
  exit 0
fi

# Resolve the content node ID
if [ "$ITEM_TYPE" = "pr" ]; then
  QUERY='query($owner:String!,$repo:String!,$n:Int!){repository(owner:$owner,name:$repo){pullRequest(number:$n){id}}}'
  JQ_PATH='.data.repository.pullRequest.id'
else
  QUERY='query($owner:String!,$repo:String!,$n:Int!){repository(owner:$owner,name:$repo){issue(number:$n){id}}}'
  JQ_PATH='.data.repository.issue.id'
fi

NODE_ID=$(gh api graphql \
  -f query="$QUERY" \
  -f owner="$OWNER" -f repo="$REPO_NAME" -F n="$NUMBER" \
  --jq "$JQ_PATH" 2>&1) || {
  echo "::warning::Failed to resolve node ID for $ITEM_TYPE #$NUMBER: $NODE_ID"
  exit 0
}

if [ -z "$NODE_ID" ] || [ "$NODE_ID" = "null" ]; then
  echo "::warning::No node ID returned for $ITEM_TYPE #$NUMBER"
  exit 0
fi

# Add to project (idempotent — returns existing item if already present)
ITEM_ID=$(gh api graphql -f query='
  mutation($pid:ID!,$cid:ID!){
    addProjectV2ItemById(input:{projectId:$pid,contentId:$cid}){item{id}}
  }' -f pid="$PROJECT_ID" -f cid="$NODE_ID" \
  --jq '.data.addProjectV2ItemById.item.id' 2>&1) || {
  echo "::warning::Failed to add $ITEM_TYPE #$NUMBER to project: $ITEM_ID"
  exit 0
}

# Update the field
RESULT=$(gh api graphql -f query='
  mutation($pid:ID!,$iid:ID!,$fid:ID!,$oid:String!){
    updateProjectV2ItemFieldValue(input:{
      projectId:$pid,itemId:$iid,fieldId:$fid,
      value:{singleSelectOptionId:$oid}
    }){projectV2Item{id}}
  }' -f pid="$PROJECT_ID" -f iid="$ITEM_ID" \
  -f fid="$FIELD_ID" -f oid="$OPTION_ID" 2>&1) || {
  echo "::warning::Failed to update field on $ITEM_TYPE #$NUMBER: $RESULT"
  exit 0
}

echo "Updated project board: $ITEM_TYPE #$NUMBER field=$FIELD_ID option=$OPTION_ID"
