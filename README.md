# Claude Slash Commands

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Shell](https://img.shields.io/badge/shell-bash-green.svg)

A curated collection of custom slash commands for Claude Code CLI, designed to streamline common development workflows and enforce consistent patterns across projects.

## Overview

This repository provides reusable slash commands that can be invoked within Claude Code sessions to automate repetitive tasks, enforce coding standards, and improve productivity. Commands are organized by category and can be easily integrated into any Claude Code workflow.

## Repository Structure

| Directory | Purpose |
|-----------|---------|
| [`commands/public`](commands/public) | Publicly shareable slash commands |
| [`scripts`](scripts) | Python automation scripts |
| [`ref`](ref) | Reference documentation |

## Command Categories

| Category | Description | Commands |
|----------|-------------|----------|
| **Documentation** | Commands for generating and formatting documentation | [`add-readme`](commands/public/docs/add-readme.md), [`format-links`](commands/public/docs/format-links.md) |
| **Repository Organization** | Commands for cleaning and organizing repositories | [`clean-repo`](commands/public/repo-org/clean-repo.md) |
| **Security** | Commands for security-related tasks | [`allow-env`](commands/public/security/allow-env.md) |
| **Development Steers** | Commands that guide development patterns | [`use-uv`](commands/public/steers/use-uv.md) |
| **Miscellaneous** | Utility commands | [`wrong-number`](commands/public/misc/wrong-number.md) |

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

## Command Development

Commands follow a consistent structure:
- Clear, actionable instructions
- Specific do/don't guidelines
- Context-aware behavior
- Minimal user intervention required