# Claude Slash Commands

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Shell](https://img.shields.io/badge/shell-bash-green.svg)
![Commands](https://img.shields.io/badge/commands-357-brightgreen.svg)

A curated collection of custom slash commands for Claude Code CLI, designed to streamline common development workflows and enforce consistent patterns across projects.

## Command Organization Visualization

![Command Organization Graph](ref/from-ai/command-graph.png)

*Visual representation of slash command organization across categories and subcategories.*

## Overview

This repository provides reusable slash commands that can be invoked within Claude Code sessions to automate repetitive tasks, enforce coding standards, and improve productivity. Commands are organized by category and can be easily integrated into any Claude Code workflow.

## Repository Structure

| Directory | Purpose |
|-----------|---------|
| [`commands`](commands) | 350+ slash commands organized by category |
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

The repository includes a pre-push hook that automatically syncs slash commands and regenerates the command index before pushing changes. This ensures the repository stays consistent and the index is always up to date.

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
1. Runs `sync-commands.sh` to sync all slash commands
2. Runs `scripts/generate_index.py` to regenerate the command index
3. Checks if INDEX.md or README.md were updated
4. If files were updated, stages them and prompts you to commit
5. Aborts the push if sync or index generation fails
6. Proceeds with push if everything is up to date

This helps maintain consistency by preventing pushes when command synchronization issues exist or when the index is outdated.

## Command Development

Commands follow a consistent structure:
- Clear, actionable instructions
- Specific do/don't guidelines
- Context-aware behavior
- Minimal user intervention required

## Browsing Available Commands

**For a complete, searchable index of all 357 slash commands organized by category, see [INDEX.md](INDEX.md).**

The index provides:
- Commands grouped by category and subcategory
- Descriptions and usage examples
- File paths for easy navigation
- Auto-generated from the repository structure

<!-- INDEX_START -->
# Command Index

*This index is automatically generated. Do not edit manually.*

**Total Commands:** 87


## Ai Engineering

*Path: `commands/public/ai-engineering`*

**Commands in this category:** 1


| Command | Description |
|---------|-------------|
| [`multiagent`](commands/public/ai-engineering/multiagent.md) | *No description available* |

## Conv Mgmt

*Path: `commands/public/conv-mgmt`*

**Commands in this category:** 1


| Command | Description |
|---------|-------------|
| [`give-me-number-options`](commands/public/conv-mgmt/give-me-number-options.md) | *No description available* |

## Development

*Path: `commands/public/development`*

**Commands in this category:** 6


| Command | Description |
|---------|-------------|
| [`containerize`](commands/public/development/containerize.md) | docker build -t project-name . |
| [`decontainerize`](commands/public/development/decontainerize.md) | *No description available* |
| [`dont-reinvent-the-wheel`](commands/public/development/dont-reinvent-the-wheel.md) | *No description available* |
| [`inspect-deployment`](commands/public/development/inspect-deployment.md) | *No description available* |
| [`setup-ci-cd`](commands/public/development/setup-ci-cd.md) | *No description available* |
| [`setup-hot-reload`](commands/public/development/setup-hot-reload.md) | *No description available* |

## Code Editing

*Path: `commands/public/development/code-editing`*

**Commands in this category:** 2


| Command | Description |
|---------|-------------|
| [`format-code`](commands/public/development/code-editing/format-code.md) | *No description available* |
| [`remove-comments`](commands/public/development/code-editing/remove-comments.md) | *No description available* |

## Github

*Path: `commands/public/development/deployment/github`*

**Commands in this category:** 2


| Command | Description |
|---------|-------------|
| [`make-private-gh-repo`](commands/public/development/deployment/github/make-private-gh-repo.md) | *No description available* |
| [`make-public-gh-repo`](commands/public/development/deployment/github/make-public-gh-repo.md) | *No description available* |

## Hf

*Path: `commands/public/development/deployment/hf`*

**Commands in this category:** 2


| Command | Description |
|---------|-------------|
| [`hf-dataset`](commands/public/development/deployment/hf/hf-dataset.md) | *No description available* |
| [`hf-space`](commands/public/development/deployment/hf/hf-space.md) | *No description available* |

## Github Workflow

*Path: `commands/public/development/github-workflow`*

**Commands in this category:** 5


| Command | Description |
|---------|-------------|
| [`backup-repo`](commands/public/development/github-workflow/backup-repo.md) | *No description available* |
| [`choose-license`](commands/public/development/github-workflow/choose-license.md) | *No description available* |
| [`contributor-guide`](commands/public/development/github-workflow/contributor-guide.md) | *No description available* |
| [`create-branch`](commands/public/development/github-workflow/create-branch.md) | *No description available* |
| [`fork-setup`](commands/public/development/github-workflow/fork-setup.md) | git clone [your-fork-url] git remote add upstream [original-repo-url] git remote -v git fetch upstream |

## Language Refactor

*Path: `commands/public/development/language-refactor`*

**Commands in this category:** 2


| Command | Description |
|---------|-------------|
| [`js-to-python`](commands/public/development/language-refactor/js-to-python.md) | *No description available* |
| [`python-to-js`](commands/public/development/language-refactor/python-to-js.md) | *No description available* |

## Python

*Path: `commands/public/development/python`*

**Commands in this category:** 4


| Command | Description |
|---------|-------------|
| [`add-repo-index`](commands/public/development/python/add-repo-index.md) | *No description available* |
| [`add-uv-venv`](commands/public/development/python/add-uv-venv.md) | *No description available* |
| [`migrate-to-uv`](commands/public/development/python/migrate-to-uv.md) | *No description available* |
| [`use-conda`](commands/public/development/python/use-conda.md) | *No description available* |

## Repo Org

*Path: `commands/public/development/repo-org`*

**Commands in this category:** 2


| Command | Description |
|---------|-------------|
| [`clean-repo`](commands/public/development/repo-org/clean-repo.md) | *No description available* |
| [`set-up-task-mgmt`](commands/public/development/repo-org/set-up-task-mgmt.md) | *No description available* |

## Security

*Path: `commands/public/development/security`*

**Commands in this category:** 2


| Command | Description |
|---------|-------------|
| [`allow-env`](commands/public/development/security/allow-env.md) | *No description available* |
| [`scan-pii`](commands/public/development/security/scan-pii.md) | - File: src/config.js:45 Type: Email address Content: [REDACTED]@company.com Context: Developer email in comment |

## Ux Design

*Path: `commands/public/development/ux-design`*

**Commands in this category:** 7


| Command | Description |
|---------|-------------|
| [`improve-css`](commands/public/development/ux-design/improve-css.md) | *No description available* |
| [`make-it-pretty`](commands/public/development/ux-design/make-it-pretty.md) | *No description available* |
| [`optimize-dashboard`](commands/public/development/ux-design/optimize-dashboard.md) | *No description available* |
| [`optimize-fonts`](commands/public/development/ux-design/optimize-fonts.md) | *No description available* |
| [`responsive-audit`](commands/public/development/ux-design/responsive-audit.md) | *No description available* |
| [`standardize-icons`](commands/public/development/ux-design/standardize-icons.md) | *No description available* |
| [`suggest-frameworks`](commands/public/development/ux-design/suggest-frameworks.md) | *No description available* |

## Docs

*Path: `commands/public/docs`*

**Commands in this category:** 4


| Command | Description |
|---------|-------------|
| [`create-changelog`](commands/public/docs/create-changelog.md) | All notable changes to this project will be documented in this file. |
| [`create-reference`](commands/public/docs/create-reference.md) | *No description available* |
| [`format-links`](commands/public/docs/format-links.md) | *No description available* |
| [`document-stack`](commands/public/docs/document-stack.md) | - Framework: [Name] (version) - UI Library: [Name] (version) - State Management: [Name] (version) - Runtime: [Name] (version) |

## Readme

*Path: `commands/public/docs/readme`*

**Commands in this category:** 4


| Command | Description |
|---------|-------------|
| [`add-readme`](commands/public/docs/readme/add-readme.md) | *No description available* |
| [`create-readme`](commands/public/docs/readme/create-readme.md) | Brief description of what this project does. |
| [`update-readme`](commands/public/docs/readme/update-readme.md) | *No description available* |
| [`create-hf-readme`](commands/public/docs/readme/create-hf-readme.md) | tags: - tag1 - tag2 license: mit datasets: - dataset-name language: - en --- Description of the model, dataset, or space. |

## Educational

*Path: `commands/public/educational`*

**Commands in this category:** 4


| Command | Description |
|---------|-------------|
| [`analyze-commits`](commands/public/educational/analyze-commits.md) | **Period:** Last 30 days **Total Commits:** 45 - Feature: User authentication system (15 commits) - Refactor: Database layer optimization (8 commits) |
| [`create-briefing`](commands/public/educational/create-briefing.md) | *No description available* |
| [`explain-code`](commands/public/educational/explain-code.md) | *No description available* |
| [`find-learning`](commands/public/educational/find-learning.md) | *No description available* |

## Filesystem Mgmt

*Path: `commands/public/filesystem-mgmt`*

**Commands in this category:** 2


| Command | Description |
|---------|-------------|
| [`flatten`](commands/public/filesystem-mgmt/flatten.md) | *No description available* |
| [`organise`](commands/public/filesystem-mgmt/organise.md) | *No description available* |

## General Purpose

*Path: `commands/public/general-purpose`*

**Commands in this category:** 1


| Command | Description |
|---------|-------------|
| [`recursive-spellcheck`](commands/public/general-purpose/recursive-spellcheck.md) | *No description available* |

## Ideation

*Path: `commands/public/ideation`*

**Commands in this category:** 4


| Command | Description |
|---------|-------------|
| [`design-ideas`](commands/public/ideation/design-ideas.md) | **Visual Style:** - Frosted glass effect cards - Soft shadows and blurs - Vibrant gradient backgrounds |
| [`fresh-perspective`](commands/public/ideation/fresh-perspective.md) | [What was tried and why it failed] Instead of [X], what if we [opposite of X]? - Rationale: [Why this could work] |
| [`innovative-features`](commands/public/ideation/innovative-features.md) | **Problem Solved:** Users struggle to find relevant content quickly **Implementation Approach:** - Integrate vector embeddings for semantic search |
| [`suggest-ideas`](commands/public/ideation/suggest-ideas.md) | 1. Add user profile customization 2. Implement dark mode toggle 3. Create export to PDF functionality |

## Media Mgmt

*Path: `commands/public/media-mgmt`*

**Commands in this category:** 2


| Command | Description |
|---------|-------------|
| [`process-stock`](commands/public/media-mgmt/process-stock.md) | *No description available* |
| [`sort-media`](commands/public/media-mgmt/sort-media.md) | *No description available* |

## Misc

*Path: `commands/public/misc`*

**Commands in this category:** 1


| Command | Description |
|---------|-------------|
| [`wrong-number`](commands/public/misc/wrong-number.md) | *No description available* |

## Operations

*Path: `commands/public/operations`*

**Commands in this category:** 7


| Command | Description |
|---------|-------------|
| [`collect-feedback`](commands/public/operations/collect-feedback.md) | - Duration: - Tasks completed: - Overall satisfaction: [1-5 stars] - [Bullet points] - [Bullet points] |
| [`create-scope`](commands/public/operations/create-scope.md) | **Description:** [Clear, concise description] **Goals:** - Goal 1 - Goal 2 - [ ] Feature 1: [Description] |
| [`debug-fix`](commands/public/operations/debug-fix.md) | *No description available* |
| [`document-blocker`](commands/public/operations/document-blocker.md) | **Date:** [YYYY-MM-DD] **Priority:** [High/Medium/Low] **Status:** [Blocked/Investigating/Resolved] [Detailed description] |
| [`manage-project`](commands/public/operations/manage-project.md) | - [ ] Task currently being worked on - [ ] High priority task - [ ] Medium priority task - [x] Completed task 1 |
| [`refactor-plan`](commands/public/operations/refactor-plan.md) | - Improve code organization - Reduce technical debt - Enhance maintainability 1. Restructure folders: |
| [`session-summary`](commands/public/operations/session-summary.md) | - ✅ Implemented user authentication - ✅ Fixed navbar responsive issues - ✅ Updated API documentation - ⚠️ Database migration (90% complete) |

## Recurrent Tasks

*Path: `commands/public/recurrent-tasks`*

**Commands in this category:** 1


| Command | Description |
|---------|-------------|
| [`index-repo`](commands/public/recurrent-tasks/index-repo.md) | Created Description shields.io badge (END TEMPLATE) The shields.io badge should be a Github badge that says View Repo and links to the repository. |

## Seo Web

*Path: `commands/public/seo-web`*

**Commands in this category:** 2


| Command | Description |
|---------|-------------|
| [`ai-friendly-seo`](commands/public/seo-web/ai-friendly-seo.md) | *No description available* |
| [`seo-audit`](commands/public/seo-web/seo-audit.md) | *No description available* |

## Steers

*Path: `commands/public/steers`*

**Commands in this category:** 1


| Command | Description |
|---------|-------------|
| [`use-uv`](commands/public/steers/use-uv.md) | *No description available* |

## Sysadmin

*Path: `commands/public/sysadmin`*

**Commands in this category:** 5


| Command | Description |
|---------|-------------|
| [`docker-help`](commands/public/sysadmin/docker-help.md) | docker logs container_name docker inspect container_name docker stats docker ps -a ``` 3. Address specific issues: |
| [`organize-files`](commands/public/sysadmin/organize-files.md) | *No description available* |
| [`python-env-setup`](commands/public/sysadmin/python-env-setup.md) | python3 -m venv venv source venv/bin/activate  # Linux/Mac venv\Scripts\activate     # Windows conda create -n myenv python=3.11 |
| [`review-boot`](commands/public/sysadmin/review-boot.md) | *No description available* |
| [`setup-conda`](commands/public/sysadmin/setup-conda.md) | conda create -n myenv python=3.11 conda activate myenv conda install numpy pandas scikit-learn conda install pytorch torchvision torchaudio... |

## Shared

*Path: `commands/public/sysadmin/shared`*

**Commands in this category:** 6


| Command | Description |
|---------|-------------|
| [`btrfs-snapper-health`](commands/public/sysadmin/shared/btrfs-snapper-health.md) | *No description available* |
| [`check-boot-logs`](commands/public/sysadmin/shared/check-boot-logs.md) | *No description available* |
| [`diagnose-slowdown`](commands/public/sysadmin/shared/diagnose-slowdown.md) | *No description available* |
| [`review-startup-services`](commands/public/sysadmin/shared/review-startup-services.md) | *No description available* |
| [`system-health-checkup`](commands/public/sysadmin/shared/system-health-checkup.md) | *No description available* |
| [`system-upgrade`](commands/public/sysadmin/shared/system-upgrade.md) | *No description available* |

## Writing

*Path: `commands/public/writing`*

**Commands in this category:** 7


| Command | Description |
|---------|-------------|
| [`add-headings`](commands/public/writing/add-headings.md) | *No description available* |
| [`add-sources`](commands/public/writing/add-sources.md) | *No description available* |
| [`fix-typos`](commands/public/writing/fix-typos.md) | *No description available* |
| [`improve-flow`](commands/public/writing/improve-flow.md) | *No description available* |
| [`proofread`](commands/public/writing/proofread.md) | *No description available* |
| [`seo-optimize`](commands/public/writing/seo-optimize.md) | *No description available* |
| [`uk-english`](commands/public/writing/uk-english.md) | *No description available* |
<!-- INDEX_END -->

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Related Repositories

This repository is part of a collection of Claude Code resources:

- **[Claude-Code-Repos-Index](https://github.com/danielrosehill/Claude-Code-Repos-Index)** - Comprehensive index of all Claude Code related repositories
- **[Claude-Code-Writing-Squad](https://github.com/danielrosehill/Claude-Code-Writing-Squad)** - Specialized writing-focused agents for Claude Code
- **[Claude-Sub-Agent-Network](https://github.com/danielrosehill/Claude-Sub-Agent-Network)** - Network of sub-agents for complex multi-step tasks
- **[Smithery-Claude-Code-MCP-Jumpstarter](https://github.com/danielrosehill/Smithery-Claude-Code-MCP-Jumpstarter)** - MCP server configurations and jumpstart guides
- **[Cool-Claude-Code-Stuff](https://github.com/danielrosehill/Cool-Claude-Code-Stuff)** - Collection of interesting Claude Code workflows and patterns
- **[Non-Code-Claude-Code](https://github.com/danielrosehill/Non-Code-Claude-Code)** - Claude Code usage for non-coding tasks