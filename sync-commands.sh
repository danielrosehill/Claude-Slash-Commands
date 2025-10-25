#!/bin/bash

# Sync script for Claude slash commands
# Syncs repo-level commands (.claude/commands/*) to ~/.claude/commands/repo-commands
# This keeps project-specific commands separate from the main command library

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get the script's directory (repository root)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${SCRIPT_DIR}/repo-commands"
TARGET_DIR="${HOME}/.claude/commands/repo-commands"

echo -e "${BLUE}Claude Repo Commands Sync${NC}"
echo "================================"
echo "Source: ${SOURCE_DIR}"
echo "Target: ${TARGET_DIR}"
echo ""

# Check if source directory exists
if [ ! -d "${SOURCE_DIR}" ]; then
    echo -e "${RED}Error: Source directory ${SOURCE_DIR} does not exist${NC}"
    exit 1
fi

# Create target directory if it doesn't exist
if [ ! -d "${TARGET_DIR}" ]; then
    echo -e "${BLUE}Creating target directory: ${TARGET_DIR}${NC}"
    mkdir -p "${TARGET_DIR}"
fi

total_count=0
updated_count=0
skipped_count=0
removed_count=0

# Create a temporary file to track synced files
SYNC_MANIFEST=$(mktemp)
trap "rm -f $SYNC_MANIFEST" EXIT

echo -e "${BLUE}Syncing markdown files...${NC}"

# Find all .md files in SOURCE_DIR and copy them to base of TARGET_DIR
while IFS= read -r -d $'\0' file; do
    # Get just the filename
    filename=$(basename "$file")
    target_path="${TARGET_DIR}/${filename}"

    # Check if file needs updating (doesn't exist or is different)
    if [ ! -f "$target_path" ] || ! cmp -s "$file" "$target_path"; then
        cp "$file" "$target_path"
        echo -e "  ${GREEN}✓${NC} ${filename}"
        ((updated_count++))
    else
        ((skipped_count++))
    fi

    # Track this file as synced
    echo "$target_path" >> "$SYNC_MANIFEST"
    ((total_count++))

done < <(find "$SOURCE_DIR" -type f -name "*.md" -print0)

# Clean up orphaned files (exist in target but not in source)
echo -e "${BLUE}Cleaning up orphaned files...${NC}"

while IFS= read -r -d $'\0' target_file; do
    if ! grep -qxF "$target_file" "$SYNC_MANIFEST"; then
        echo -e "  ${RED}✗${NC} Removing orphaned: ${target_file#${TARGET_DIR}/}"
        rm "$target_file"
        ((removed_count++))
    fi
done < <(find "${TARGET_DIR}" -type f -name "*.md" -print0 2>/dev/null)

# Remove empty directories
find "${TARGET_DIR}" -type d -empty -delete 2>/dev/null || true

echo ""
if [ $total_count -eq 0 ]; then
    echo -e "${YELLOW}No markdown files found to sync${NC}"
else
    echo -e "${GREEN}✓ Sync complete!${NC}"
    echo -e "  Total: ${total_count} file(s)"
    echo -e "  Updated: ${updated_count} file(s)"
    echo -e "  Unchanged: ${skipped_count} file(s)"
    echo -e "  Removed: ${removed_count} file(s)"
    echo ""
    echo "Available repo commands:"
    while IFS= read -r -d $'\0' file; do
        cmd_name=$(basename "$file" .md)
        echo -e "  ${GREEN}/repo-commands:${cmd_name}${NC}"
    done < <(find "${TARGET_DIR}" -maxdepth 1 -type f -name "*.md" -print0 2>/dev/null | sort -z)
fi
