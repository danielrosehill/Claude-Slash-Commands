#!/usr/bin/env python3
"""
Generate a comprehensive index of all slash commands in the repository.

This script:
1. Scans commands/public/ directory recursively
2. Groups commands by category (directory structure)
3. Generates markdown index with relative GitHub links
4. Can output to standalone file or inject into README.md
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict


def get_repo_root() -> Path:
    """Get the repository root directory."""
    script_dir = Path(__file__).resolve().parent
    return script_dir.parent


def extract_title_from_md(file_path: Path) -> str:
    """
    Extract the first heading from a markdown file as the title.
    Falls back to filename if no heading found.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for first # heading
            match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if match:
                return match.group(1).strip()
    except Exception:
        pass

    # Fallback to filename without extension
    return file_path.stem.replace('-', ' ').title()


def extract_description_from_md(file_path: Path) -> str:
    """
    Extract a brief description from the markdown file.
    Looks for the first paragraph after the title.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Skip the title and find first non-empty paragraph
            lines = content.split('\n')
            in_content = False
            description_lines = []

            for line in lines:
                line = line.strip()
                # Skip title
                if line.startswith('#'):
                    in_content = True
                    continue

                if in_content and line:
                    # Stop at next heading or after first paragraph
                    if line.startswith('#'):
                        break
                    description_lines.append(line)
                    # Limit to first sentence or ~100 chars
                    joined = ' '.join(description_lines)
                    if len(joined) > 100 or joined.endswith('.'):
                        break

            if description_lines:
                desc = ' '.join(description_lines)[:150]
                # Truncate at last complete word if needed
                if len(' '.join(description_lines)) > 150:
                    desc = desc.rsplit(' ', 1)[0] + '...'
                return desc
    except Exception:
        pass

    return ""


def scan_commands(commands_dir: Path) -> Dict[str, List[Tuple[Path, str, str]]]:
    """
    Scan the commands directory and organize by category.

    Returns:
        Dict mapping category paths to list of (file_path, title, description) tuples
    """
    commands = defaultdict(list)

    if not commands_dir.exists():
        print(f"Warning: Commands directory not found: {commands_dir}")
        return commands

    # Walk through all markdown files
    for md_file in sorted(commands_dir.rglob("*.md")):
        # Get relative path from commands/public
        rel_path = md_file.relative_to(commands_dir)
        category = str(rel_path.parent) if rel_path.parent != Path('.') else "root"

        title = extract_title_from_md(md_file)
        description = extract_description_from_md(md_file)

        commands[category].append((md_file, title, description))

    return commands


def format_category_name(category: str) -> str:
    """Convert category path to readable name."""
    if category == "root":
        return "General Commands"

    # Take the last directory name and format it
    parts = category.split(os.sep)
    last_part = parts[-1]

    # Convert from kebab-case to Title Case
    return last_part.replace('-', ' ').title()


def generate_index_content(commands: Dict[str, List[Tuple[Path, str, str]]],
                          repo_root: Path) -> str:
    """
    Generate the markdown content for the index.

    Args:
        commands: Dict mapping categories to command lists
        repo_root: Repository root path for generating relative links

    Returns:
        Markdown formatted index content
    """
    lines = []
    lines.append("# Command Index\n")
    lines.append("*This index is automatically generated. Do not edit manually.*\n")
    lines.append(f"**Total Commands:** {sum(len(cmds) for cmds in commands.values())}\n")

    # Sort categories for consistent output
    sorted_categories = sorted(commands.keys())

    for category in sorted_categories:
        category_commands = commands[category]
        if not category_commands:
            continue

        # Category header
        category_name = format_category_name(category)
        lines.append(f"\n## {category_name}\n")
        lines.append(f"*Path: `commands/public/{category}`*\n")
        lines.append(f"**Commands in this category:** {len(category_commands)}\n")

        # Command table
        lines.append("\n| Command | Description |")
        lines.append("|---------|-------------|")

        for file_path, title, description in sorted(category_commands, key=lambda x: x[1]):
            # Generate relative GitHub link
            rel_link = file_path.relative_to(repo_root)
            github_link = str(rel_link).replace(os.sep, '/')

            # Format command name (filename without extension)
            command_name = file_path.stem

            # Create table row
            desc_text = description if description else "*No description available*"
            lines.append(f"| [`{command_name}`]({github_link}) | {desc_text} |")

    return '\n'.join(lines)


def write_standalone_index(content: str, output_path: Path) -> None:
    """Write index to a standalone INDEX.md file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Standalone index written to: {output_path}")


def inject_into_readme(content: str, readme_path: Path) -> bool:
    """
    Inject index content into README.md between markers.

    Returns:
        True if README was modified, False otherwise
    """
    START_MARKER = "<!-- INDEX_START -->"
    END_MARKER = "<!-- INDEX_END -->"

    if not readme_path.exists():
        print(f"Warning: README.md not found at {readme_path}")
        return False

    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # Check if markers exist
    if START_MARKER not in readme_content or END_MARKER not in readme_content:
        print(f"Warning: Injection markers not found in README.md")
        print(f"Please add the following markers where you want the index:")
        print(f"  {START_MARKER}")
        print(f"  {END_MARKER}")
        return False

    # Find marker positions
    start_pos = readme_content.find(START_MARKER)
    end_pos = readme_content.find(END_MARKER)

    if start_pos >= end_pos:
        print("Error: START_MARKER must come before END_MARKER")
        return False

    # Extract existing content between markers
    start_content_pos = start_pos + len(START_MARKER)
    existing_index = readme_content[start_content_pos:end_pos].strip()
    new_index = content.strip()

    # Check if content changed
    if existing_index == new_index:
        print("✓ Index in README.md is already up to date")
        return False

    # Inject new content
    new_readme = (
        readme_content[:start_content_pos] +
        "\n" + new_index + "\n" +
        readme_content[end_pos:]
    )

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_readme)

    print(f"✓ Index injected into README.md")
    return True


def main():
    """Main entry point for the script."""
    repo_root = get_repo_root()
    commands_dir = repo_root / "commands" / "public"

    print(f"Scanning commands in: {commands_dir}")

    # Scan commands
    commands = scan_commands(commands_dir)

    if not commands:
        print("No commands found!")
        return 1

    print(f"Found {sum(len(cmds) for cmds in commands.values())} commands " +
          f"in {len(commands)} categories")

    # Generate index content
    index_content = generate_index_content(commands, repo_root)

    # Write standalone index
    index_file = repo_root / "INDEX.md"
    write_standalone_index(index_content, index_file)

    # Inject into README.md
    readme_file = repo_root / "README.md"
    readme_modified = inject_into_readme(index_content, readme_file)

    if readme_modified:
        print("\n⚠️  README.md has been modified. Please review and commit the changes.")

    return 0


if __name__ == "__main__":
    exit(main())
