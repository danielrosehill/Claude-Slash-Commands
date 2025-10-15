# Command Index Generation

This directory contains the Python script for automatically generating a comprehensive index of all slash commands in the repository.

## Overview

The `generate_index.py` script:
- Scans `commands/public/` recursively for all `.md` files
- Extracts titles and descriptions from each command file
- Groups commands by category (directory structure)
- Generates a formatted markdown index with relative GitHub links
- Outputs to both a standalone `INDEX.md` file and injects into `README.md`

## Usage

### Manual Generation

Run the script directly to generate/update the index:

```bash
python3 scripts/generate_index.py
```

The script will:
1. Create/update `INDEX.md` in the repository root
2. Look for injection markers in `README.md`:
   - `<!-- INDEX_START -->`
   - `<!-- INDEX_END -->`
3. If markers are found, inject the index content between them
4. Report what was done

### Automatic Generation (via Git Hook)

The pre-push hook automatically runs this script before each push. See the main README for hook installation instructions.

## How It Works

### Command Scanning

The script walks through the `commands/public/` directory tree and:
- Finds all `.md` files
- Extracts the first `# Heading` as the title
- Extracts the first paragraph as a description
- Records the relative file path

### Category Organization

Commands are organized by their directory structure:
- `commands/public/development/python/add-repo-index.md`
  - Category: `Python` (from `development/python`)
  - Command: `add-repo-index`

### Link Generation

All links are relative to the repository root, making them work correctly on GitHub:
- Format: `commands/public/category/subcategory/command.md`
- GitHub automatically renders these as clickable links

### Injection System

The script uses HTML comment markers to identify where to inject content:

```markdown
<!-- INDEX_START -->
[Index content gets injected here]
<!-- INDEX_END -->
```

Benefits:
- Content before/after markers is preserved
- Index can be regenerated without manual editing
- Safe to run multiple times (idempotent)

## Output Files

### INDEX.md

A standalone file containing the complete index. Useful for:
- Direct navigation on GitHub
- Linking from other documentation
- Offline reference

### README.md (injected section)

The same index content injected between markers in README.md, providing:
- Single-file navigation
- Reduced user friction (don't need to open separate file)
- Consistent with repository structure documentation

## Index Format

The generated index includes:

```markdown
# Command Index

*This index is automatically generated. Do not edit manually.*

**Total Commands:** 87

## Category Name

*Path: `commands/public/category`*

**Commands in this category:** X

| Command | Description |
|---------|-------------|
| [`command-name`](path/to/file.md) | Brief description |
```

Each category shows:
- Formatted category name
- File system path
- Command count
- Table of commands with links and descriptions

## Incremental Updates

The script is designed to be run incrementally:
- Safe to run multiple times
- Only reports changes when content actually differs
- Git hook prevents pushes if index is outdated
- No database or state files needed

## Adding New Commands

When you add a new command:
1. Create the `.md` file in `commands/public/[category]/`
2. Run `python3 scripts/generate_index.py` (or let the hook do it)
3. Review the updated INDEX.md and README.md
4. Commit the changes

## Troubleshooting

### No descriptions showing

Make sure your command files have:
- A `# Title` heading as the first heading
- At least one paragraph of text after the title

### Markers not found

If you see "Injection markers not found in README.md":
1. Open README.md
2. Add these markers where you want the index:
   ```markdown
   <!-- INDEX_START -->
   <!-- INDEX_END -->
   ```
3. Run the script again

### Script fails

Check:
- Python 3 is installed and in PATH
- You're running from the repository root or scripts directory
- The `commands/public/` directory exists
- You have write permissions for INDEX.md and README.md

## Technical Details

**Language:** Python 3
**Dependencies:** None (uses only standard library)
**Execution time:** < 1 second for 100 commands
**Compatibility:** Works on Linux, macOS, Windows

The script is intentionally dependency-free to ensure it works in all environments without requiring package installation.
