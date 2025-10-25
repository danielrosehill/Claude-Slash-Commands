#!/bin/bash
# Interactive command finder using fzf
# Scans ~/.claude/commands and presents an interactive fuzzy search picker

set -e

COMMANDS_DIR="$HOME/.claude/commands"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check if fzf is installed
if ! command -v fzf &> /dev/null; then
    echo -e "${YELLOW}Error: fzf is not installed. Please install it first.${NC}"
    echo "Install with: sudo apt install fzf"
    exit 1
fi

# Check if commands directory exists
if [ ! -d "$COMMANDS_DIR" ]; then
    echo -e "${YELLOW}Error: Commands directory not found: $COMMANDS_DIR${NC}"
    exit 1
fi

# Build a list of commands with their descriptions
# Format: /command/path → First line of content
temp_list=$(mktemp)
trap "rm -f $temp_list" EXIT

while IFS= read -r -d $'' file; do
    # Get relative path from commands directory and convert to command format
    rel_path="${file#$COMMANDS_DIR/}"
    # Remove .md extension and convert path to command format
    cmd_path="${rel_path%.md}"
    cmd_name="/${cmd_path//\//:}"

    # Get first non-empty line as description
    description=$(head -20 "$file" | grep -v '^[[:space:]]*$' | head -1 | sed 's/^[[:space:]]*//')

    # Truncate description if too long
    if [ ${#description} -gt 80 ]; then
        description="${description:0:77}..."
    fi

    echo -e "${cmd_name}\t${description}" >> "$temp_list"
done < <(find "$COMMANDS_DIR" -type f -name "*.md" -print0)

# Sort the list
sort -o "$temp_list" "$temp_list"

# Use fzf to select a command
selected=$(cat "$temp_list" | fzf \
    --height=80% \
    --border \
    --prompt="Search commands > " \
    --preview-window=right:60%:wrap \
    --preview='
        cmd=$(echo {} | cut -f1)
        # Convert command back to file path
        file_path=$(echo "$cmd" | sed "s|^/||" | sed "s|:|/|g")
        full_path="'"$COMMANDS_DIR"'/${file_path}.md"
        if [ -f "$full_path" ]; then
            echo -e "\033[1;34mCommand:\033[0m $cmd"
            echo -e "\033[1;34mFile:\033[0m $full_path"
            echo ""
            echo -e "\033[1;34mContent:\033[0m"
            echo "---"
            cat "$full_path"
        fi
    ' \
    --header='↑↓ Navigate | Enter: Select | Esc: Cancel' \
    --delimiter='\t' \
    --with-nth=1,2 \
) || exit 0

if [ -n "$selected" ]; then
    # Extract command name
    cmd_name=$(echo "$selected" | cut -f1)

    # Convert to file path
    file_path=$(echo "$cmd_name" | sed 's|^/||' | sed 's|:|/|g')
    full_path="$COMMANDS_DIR/${file_path}.md"

    echo ""
    echo -e "${GREEN}Selected command: ${BLUE}$cmd_name${NC}"
    echo -e "${GREEN}File location: ${NC}$full_path"
    echo ""
    echo -e "${BLUE}Command content:${NC}"
    echo "---"
    cat "$full_path"
    echo ""
    echo "---"
    echo -e "${YELLOW}To use this command, type: ${BLUE}$cmd_name${NC}"
fi
