https://docs.claude.com/en/docs/claude-code/slash-commands

# Slash Commands Documentation

## Overview

Slash commands are a way to control Claude's behavior during an interactive session. They come in several types:

### 1. Built-in Slash Commands
- Examples include `/clear`, `/help`, `/review`, `/model`, `/init`
- Provide quick access to system functions and settings

### 2. Custom Slash Commands
- Can be created at two levels:
  - **Project-level**: Stored in `.claude/commands/`
  - **Personal-level**: Stored in `~/.claude/commands/`

### 3. Command Syntax
- Basic format: `/<command-name> [arguments]`
- Support argument placeholders like `$ARGUMENTS`, `$1`, `$2`

## Key Features

- Supports file references using `@` prefix
- Can execute bash commands with `!` prefix
- Allows namespacing for organization
- Supports frontmatter for metadata configuration

## Example Custom Command Creation

```markdown
---
allowed-tools: Bash(git add:*), Bash(git commit:*)
description: Create a git commit
---
Create a git commit with message: $ARGUMENTS
```

## Advanced Capabilities

- Plugin commands can extend functionality
- MCP (Model Context Protocol) servers can expose additional commands
- Supports extended thinking and complex interactions

## Permissions and Security

- Can configure tool and command permissions
- Supports disabling specific commands or entire slash command tool

The system provides a flexible, extensible way to create custom interactions and automate workflows with Claude.
