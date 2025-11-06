#!/bin/bash

# Sync script for Claude slash commands
# 1. Flattens commands/ directory into commands-flat/ (handling name collisions with numeric suffixes)
# 2. Syncs commands-flat/ to ~/.claude/commands (destructively)
# 3. Git add, commit, and push

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get the script's directory (repository root)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${SCRIPT_DIR}/commands"
FLAT_DIR="${SCRIPT_DIR}/commands-flat"
TARGET_DIR="${HOME}/.claude/commands"

echo -e "${BLUE}Claude Commands Sync${NC}"
echo "================================"
echo "Source: ${SOURCE_DIR}"
echo "Flat: ${FLAT_DIR}"
echo "Target: ${TARGET_DIR}"
echo ""

# Check if source directory exists
if [ ! -d "${SOURCE_DIR}" ]; then
    echo -e "${RED}Error: Source directory ${SOURCE_DIR} does not exist${NC}"
    exit 1
fi

# Step 1: Flatten commands/ into commands-flat/
echo -e "${BLUE}Step 1: Flattening commands directory...${NC}"

# Remove and recreate commands-flat
if [ -d "${FLAT_DIR}" ]; then
    rm -rf "${FLAT_DIR}"
fi
mkdir -p "${FLAT_DIR}"

# Track filename usage for collision detection
declare -A filename_count

flatten_count=0
collision_count=0

# Find all .md files in SOURCE_DIR
while IFS= read -r -d $'\0' file; do
    # Get just the filename
    original_filename=$(basename "$file")
    base_name="${original_filename%.md}"

    # Check if this filename has been used before
    if [ -n "${filename_count[$original_filename]}" ]; then
        # Collision detected - add numeric suffix
        count=${filename_count[$original_filename]}
        new_filename="${base_name}-${count}.md"
        filename_count[$original_filename]=$((count + 1))

        echo -e "  ${YELLOW}⚠${NC} Collision: ${original_filename} -> ${new_filename}"
        ((collision_count++))
    else
        # First occurrence of this filename
        new_filename="$original_filename"
        filename_count[$original_filename]=2  # Next collision will be -2
    fi

    # Copy to flat directory
    cp "$file" "${FLAT_DIR}/${new_filename}"
    ((flatten_count++))

done < <(find "$SOURCE_DIR" -type f -name "*.md" -print0)

echo -e "${GREEN}✓${NC} Flattened ${flatten_count} files"
if [ $collision_count -gt 0 ]; then
    echo -e "${YELLOW}  ${collision_count} filename collision(s) resolved${NC}"
fi
echo ""

# Step 2: Sync commands-flat/ to ~/.claude/commands (non-destructively)
echo -e "${BLUE}Step 2: Syncing to ~/.claude/commands...${NC}"

# Create target directory if it doesn't exist
if [ ! -d "${TARGET_DIR}" ]; then
    mkdir -p "${TARGET_DIR}"
fi

# Copy all files from commands-flat to target (non-destructive)
# Only overwrites files with same name, doesn't delete existing files
sync_count=0
updated_count=0
new_count=0

while IFS= read -r -d $'\0' file; do
    filename=$(basename "$file")
    target_file="${TARGET_DIR}/${filename}"

    if [ -f "$target_file" ]; then
        # File exists - check if it needs updating
        if ! cmp -s "$file" "$target_file"; then
            cp "$file" "$target_file"
            echo -e "  ${YELLOW}↻${NC} Updated: ${filename}"
            ((updated_count++))
        else
            echo -e "  ${GREEN}✓${NC} Unchanged: ${filename}"
        fi
    else
        # New file
        cp "$file" "$target_file"
        echo -e "  ${GREEN}+${NC} New: ${filename}"
        ((new_count++))
    fi
    ((sync_count++))
done < <(find "$FLAT_DIR" -type f -name "*.md" -print0)

echo -e "${GREEN}✓${NC} Synced ${sync_count} commands to ~/.claude/commands"
if [ $new_count -gt 0 ]; then
    echo -e "  ${GREEN}+${NC} ${new_count} new command(s)"
fi
if [ $updated_count -gt 0 ]; then
    echo -e "  ${YELLOW}↻${NC} ${updated_count} updated command(s)"
fi
echo ""

# Step 3: Git operations
echo -e "${BLUE}Step 3: Git operations...${NC}"

cd "${SCRIPT_DIR}" || exit 1

# Check if there are changes to commit
if git diff --quiet && git diff --cached --quiet; then
    echo -e "${YELLOW}No changes to commit${NC}"
else
    # Add all changes
    git add .
    echo -e "${GREEN}✓${NC} Added changes to git"

    # Commit with timestamp
    commit_message="Sync slash commands - $(date '+%Y-%m-%d %H:%M:%S')"
    git commit -m "$commit_message"
    echo -e "${GREEN}✓${NC} Committed: ${commit_message}"
fi

echo ""
echo -e "${GREEN}✓ Sync complete!${NC}"
echo -e "  Total commands flattened: ${flatten_count}"
echo -e "  Commands synced: ${sync_count}"
if [ $new_count -gt 0 ]; then
    echo -e "  New: ${new_count}"
fi
if [ $updated_count -gt 0 ]; then
    echo -e "  Updated: ${updated_count}"
fi
