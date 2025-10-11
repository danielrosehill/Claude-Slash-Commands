#!/bin/bash

# Sync script for Claude slash commands
# Syncs commands from this repository to ~/.claude/commands
# Preserves nested directory structure while skipping private/public containers

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get the script's directory (repository root)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${SCRIPT_DIR}/commands"
TARGET_DIR="${HOME}/.claude/commands"

echo -e "${BLUE}Claude Slash Commands Sync${NC}"
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

# Process both private and public containers
for container in "private" "public"; do
    container_path="${SOURCE_DIR}/${container}"

    if [ ! -d "${container_path}" ]; then
        continue
    fi

    # Find all subdirectories in the container (one level deep)
    for subdir in "${container_path}"/*; do
        # Skip if glob didn't match anything or not a directory
        [ ! -d "$subdir" ] && continue

        subdir_name=$(basename "$subdir")

        # Find all .md files recursively within this subdirectory
        while IFS= read -r -d $'\0' file; do
            # Calculate relative path from the subdirectory
            rel_path="${file#${subdir}/}"
            target_path="${TARGET_DIR}/${subdir_name}/${rel_path}"
            target_dir=$(dirname "$target_path")

            # Create target subdirectory if needed
            mkdir -p "$target_dir"

            # Check if file needs updating (doesn't exist or is different)
            if [ ! -f "$target_path" ] || ! cmp -s "$file" "$target_path"; then
                cp "$file" "$target_path"
                echo -e "  ${GREEN}✓${NC} ${subdir_name}/${rel_path} (from ${container})"
                ((updated_count++))
            else
                ((skipped_count++))
            fi

            # Track this file as synced
            echo "$target_path" >> "$SYNC_MANIFEST"
            ((total_count++))

        done < <(find "$subdir" -type f -name "*.md" -print0)

    done
done

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
    echo "Available commands:"
    while IFS= read -r -d $'\0' file; do
        cmd_name=$(basename "$file" .md)
        rel_path="${file#${TARGET_DIR}/}"
        namespace=$(dirname "$rel_path")
        if [ "$namespace" != "." ]; then
            echo -e "  ${GREEN}/${cmd_name}${NC} (${namespace})"
        else
            echo -e "  ${GREEN}/${cmd_name}${NC}"
        fi
    done < <(find "${TARGET_DIR}" -type f -name "*.md" -print0 2>/dev/null | sort -z)
fi
