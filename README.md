# Claude Slash Commands

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Shell](https://img.shields.io/badge/shell-bash-green.svg)

A curated collection of custom slash commands for Claude Code CLI, designed to streamline common development workflows and enforce consistent patterns across projects.

## Overview

This repository provides reusable slash commands that can be invoked within Claude Code sessions to automate repetitive tasks, enforce coding standards, and improve productivity. Commands are organized by category and can be easily integrated into any Claude Code workflow.

## Repository Structure

| Directory | Purpose |
|-----------|---------|
| [`commands/public`](commands/public) | 70+ publicly shareable slash commands organized by category |
| [`commands/private`](commands/private) | Private/personal slash commands |
| [`scripts`](scripts) | Python automation scripts |
| [`ref`](ref) | Reference documentation |
| [`hooks`](hooks) | Git hooks for repository automation |
| [`inspiration`](inspiration) | Ideas and inspiration for new commands |

## Command Categories

| Category | Description | Example Commands |
|----------|-------------|------------------|
| **Code Editing** | Format and modify code | `format-code`, `remove-comments` |
| **Deployment** | Deploy to GitHub and Hugging Face | `make-private-gh-repo`, `make-public-gh-repo`, `hf-dataset`, `hf-space` |
| **Development** | Development workflow tools | `containerize`, `decontainerize`, `setup-ci-cd`, `setup-hot-reload`, `inspect-deployment` |
| **Documentation** | Generate and format documentation | `create-readme`, `update-readme`, `create-hf-readme`, `create-changelog`, `create-reference`, `document-stack`, `format-links` |
| **Educational** | Learning and code analysis | `analyze-commits`, `create-briefing`, `explain-code`, `find-learning` |
| **Filesystem Management** | Organize files and directories | `flatten`, `organise` |
| **GitHub Workflow** | GitHub repository management | `backup-repo`, `choose-license`, `contributor-guide`, `create-branch`, `fork-setup` |
| **Ideation** | Generate ideas and suggestions | `design-ideas`, `fresh-perspective`, `innovative-features`, `suggest-ideas` |
| **Media Management** | Process and organize media files | `process-stock`, `sort-media` |
| **Operations** | Project management and debugging | `collect-feedback`, `create-scope`, `debug-fix`, `document-blocker`, `manage-project`, `refactor-plan`, `session-summary` |
| **Recurrent Tasks** | Automated recurring tasks | `index-repo` |
| **Repository Organization** | Clean and organize repositories | `clean-repo`, `set-up-task-mgmt` |
| **Security** | Security scanning and configuration | `allow-env`, `scan-pii` |
| **SEO & Web** | SEO optimization and auditing | `ai-friendly-seo`, `seo-audit` |
| **Development Steers** | Guide development patterns | `use-uv` |
| **System Administration** | System configuration and management | `docker-help`, `organize-files`, `python-env-setup`, `review-boot`, `setup-conda` |
| **UX Design** | UI/UX improvements | `improve-css`, `optimize-dashboard`, `optimize-fonts`, `responsive-audit`, `standardize-icons`, `suggest-frameworks` |
| **Writing** | Content writing and editing | `add-headings`, `add-sources`, `fix-typos`, `improve-flow`, `proofread`, `seo-optimize`, `uk-english` |
| **Miscellaneous** | Utility commands | `wrong-number` |

## Usage

Slash commands are invoked within Claude Code sessions using the `/` prefix followed by the command name. Commands are stored as markdown files containing prompts that Claude Code executes.

### Setup

The repository includes a bash wrapper script for managing Python dependencies:

```bash
# Setup virtual environment
./run.sh setup

# Run repository info fetcher
./run.sh fetch
```

### Command Structure

Each command is a markdown file containing instructions for Claude Code to execute. Commands can:
- Automate documentation generation
- Enforce coding standards
- Perform repository maintenance
- Guide development patterns

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `requests` | >=2.31.0 | HTTP requests for API interactions |
| `python-dotenv` | >=1.0.0 | Environment variable management |

Dependencies are managed using `uv` for fast, reliable Python package installation.

## Integration

To use these commands in your Claude Code workflow:

1. Clone this repository
2. Copy desired command files to your project's `.claude/commands` directory
3. Invoke commands using `/command-name` within Claude Code sessions

## Git Hooks

The repository includes a pre-push hook that automatically syncs slash commands before pushing changes. This ensures the repository stays consistent.

### Installing the Pre-Push Hook

To install the pre-push hook in your local repository:

```bash
# Copy the hook from the hooks directory
cp hooks/pre-push .git/hooks/pre-push

# Make it executable (if not already)
chmod +x .git/hooks/pre-push
```

### What the Hook Does

The pre-push hook:
1. Runs `sync-commands.sh` before each push
2. Ensures all slash commands are properly synced
3. Aborts the push if sync fails
4. Proceeds with push if sync succeeds

This helps maintain consistency by preventing pushes when command synchronization issues exist.

## Command Development

Commands follow a consistent structure:
- Clear, actionable instructions
- Specific do/don't guidelines
- Context-aware behavior
- Minimal user intervention required

## Related Repositories

This repository is part of a collection of Claude Code resources:

- **[Claude-Code-Repos-Index](https://github.com/danielrosehill/Claude-Code-Repos-Index)** - Comprehensive index of all Claude Code related repositories
- **[Claude-Code-Writing-Squad](https://github.com/danielrosehill/Claude-Code-Writing-Squad)** - Specialized writing-focused agents for Claude Code
- **[Claude-Sub-Agent-Network](https://github.com/danielrosehill/Claude-Sub-Agent-Network)** - Network of sub-agents for complex multi-step tasks
- **[Smithery-Claude-Code-MCP-Jumpstarter](https://github.com/danielrosehill/Smithery-Claude-Code-MCP-Jumpstarter)** - MCP server configurations and jumpstart guides
- **[Cool-Claude-Code-Stuff](https://github.com/danielrosehill/Cool-Claude-Code-Stuff)** - Collection of interesting Claude Code workflows and patterns
- **[Non-Code-Claude-Code](https://github.com/danielrosehill/Non-Code-Claude-Code)** - Claude Code usage for non-coding tasks