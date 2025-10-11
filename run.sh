#!/bin/bash
# Bash wrapper to setup/update venv and run Python scripts

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
REQUIREMENTS="$SCRIPT_DIR/requirements.txt"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to setup or update venv
setup_venv() {
    echo -e "${BLUE}Checking virtual environment...${NC}"

    if [ ! -d "$VENV_DIR" ]; then
        echo -e "${YELLOW}Creating virtual environment with uv...${NC}"
        uv venv "$VENV_DIR"
    fi

    echo -e "${BLUE}Installing/updating dependencies...${NC}"
    uv pip install -r "$REQUIREMENTS"

    echo -e "${GREEN}Virtual environment ready!${NC}"
}

# Function to activate venv and run script
run_script() {
    local script_name=$1
    local script_path="$SCRIPT_DIR/scripts/$script_name"

    if [ ! -f "$script_path" ]; then
        echo -e "${YELLOW}Error: Script '$script_name' not found in scripts/ directory${NC}"
        exit 1
    fi

    echo -e "${BLUE}Running $script_name...${NC}"
    source "$VENV_DIR/bin/activate"
    python "$script_path"
    deactivate
}

# Main script logic
case "${1:-}" in
    setup)
        setup_venv
        ;;
    fetch|fetch_repo_info.py)
        setup_venv
        run_script "fetch_repo_info.py"
        ;;
    *)
        echo "Usage: $0 {setup|fetch}"
        echo ""
        echo "Commands:"
        echo "  setup               - Setup or update the virtual environment"
        echo "  fetch               - Run fetch_repo_info.py script"
        echo ""
        exit 1
        ;;
esac
