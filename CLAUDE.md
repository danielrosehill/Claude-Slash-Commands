# Claude Slash Commands Repository

## Purpose

This repository maintains a curated library of slash commands for Claude Code, organized for public sharing and personal use.

## Directory Structure

- **`commands/public/`** - Publicly sharable slash commands organized by category
- **`commands/private/`** - Personal/private slash commands not intended for public sharing
- **`repo-commands/`** - Project-specific commands for maintaining this repository
- **`sync-commands.sh`** - Sync script to deploy repo-commands to `~/.claude/commands/repo-commands`

## Working with Commands

### Creating New Commands

Create prompts to be shared publicly within `commands/public`. Only create prompts in `commands/private` if explicitly requested or if, from context, it is obvious that they are not intended for public consumption/sharing.

### Repo-Level Commands

The `repo-commands/` folder contains commands specific to maintaining this repository:
- `/repo-commands:review-typos` - Review commands for typos and grammatical errors
- `/repo-commands:organize-commands` - Analyze and suggest better organization
- `/repo-commands:add-frontmatter` - Add YAML frontmatter to commands
- `/repo-commands:detect-duplicates` - Find duplicate or similar commands

These commands are synced to `~/.claude/commands/repo-commands` via the sync script.

## Command Organization

Commands are organized hierarchically by domain and purpose within the public/private containers. The structure helps maintain clarity and discoverability.