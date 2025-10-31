#!/usr/bin/env python3
"""
Auto-tag VS Code Project Manager favorites based on path and name patterns.

This script analyzes projects in the Project Manager extension and automatically
applies tags based on configurable rules.
"""

import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set

# Path to Project Manager data
PROJECTS_FILE = Path.home() / ".config/Code/User/globalStorage/alefragnani.project-manager/projects.json"

# Tagging rules based on path patterns
PATH_RULES = {
    "/indexing-repos/": ["Index Repo"],
    "/work-repos/": ["Work"],
    "/forks/": ["Fork"],
    "/hugging-face/datasets/": ["Dataset"],
    "/hugging-face/spaces/": ["HF Space"],
    "/hugging-face/": ["Documentation"],
}

# Tagging rules based on name patterns (case-insensitive)
NAME_RULES = {
    "claude": ["Claude Code"],
    "blog": ["Blog"],
    "github": ["Github"],
    "backup": ["Backup"],
    "nfc": ["NFC"],
    "health": ["Health"],
    "website": ["Websites"],
    "site": ["Websites"],
    "homepage": ["Websites"],
    "stt": ["STT"],
    "speech": ["STT"],
    "network": ["Networking"],
    "script": ["Scripts"],
    "video": ["Video"],
    "image": ["Images"],
    "dataset": ["Dataset"],
    "conda": ["Conda"],
    "podcast": ["Podcasts"],
    "gui": ["GUIs"],
    "assistant": ["AI Agent"],
    "agent": ["AI Agent"],
    "ezra": ["Ezra"],
    "3d": ["3D"],
    "notebook": ["Notebook"],
    "index": ["Index Repo"],
    "poc": ["POC"],
    "documentation": ["Documentation"],
    "docs": ["Documentation"],
}


def backup_projects_file():
    """Create a timestamped backup of the projects file."""
    if not PROJECTS_FILE.exists():
        print(f"Error: Projects file not found at {PROJECTS_FILE}")
        return False

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = PROJECTS_FILE.with_suffix(f".backup_{timestamp}.json")
    shutil.copy2(PROJECTS_FILE, backup_path)
    print(f"✓ Backup created: {backup_path}")
    return True


def load_projects() -> List[Dict]:
    """Load projects from the JSON file."""
    with open(PROJECTS_FILE, 'r') as f:
        return json.load(f)


def save_projects(projects: List[Dict]):
    """Save projects back to the JSON file."""
    with open(PROJECTS_FILE, 'w') as f:
        json.dump(projects, f, indent='\t')


def get_tags_for_project(project: Dict) -> Set[str]:
    """Determine tags for a project based on rules."""
    suggested_tags = set()
    root_path = project.get("rootPath", "")
    name = project.get("name", "")

    # Apply path-based rules
    for path_pattern, tags in PATH_RULES.items():
        if path_pattern in root_path:
            suggested_tags.update(tags)

    # Apply name-based rules (case-insensitive)
    name_lower = name.lower()
    for keyword, tags in NAME_RULES.items():
        if keyword in name_lower:
            suggested_tags.update(tags)

    return suggested_tags


def auto_tag_projects(dry_run: bool = False) -> Dict[str, int]:
    """
    Auto-tag projects based on defined rules.

    Args:
        dry_run: If True, only show what would be changed without modifying files

    Returns:
        Dictionary with statistics about the tagging operation
    """
    stats = {
        "total_projects": 0,
        "already_tagged": 0,
        "newly_tagged": 0,
        "tags_added": 0,
        "unchanged": 0,
    }

    projects = load_projects()
    stats["total_projects"] = len(projects)

    changes = []

    for project in projects:
        name = project.get("name", "Unknown")
        current_tags = set(project.get("tags", []))
        suggested_tags = get_tags_for_project(project)

        # Calculate new tags to add (don't remove existing tags)
        new_tags = suggested_tags - current_tags

        if current_tags:
            stats["already_tagged"] += 1

        if new_tags:
            stats["newly_tagged"] += 1
            stats["tags_added"] += len(new_tags)

            # Merge existing and new tags
            updated_tags = sorted(current_tags | new_tags)

            changes.append({
                "name": name,
                "old_tags": sorted(current_tags),
                "new_tags": sorted(new_tags),
                "final_tags": updated_tags,
            })

            if not dry_run:
                project["tags"] = updated_tags
        else:
            stats["unchanged"] += 1

    if not dry_run and changes:
        save_projects(projects)

    return stats, changes


def print_summary(stats: Dict[str, int], changes: List[Dict], dry_run: bool):
    """Print a summary of the tagging operation."""
    print("\n" + "="*60)
    print("AUTO-TAGGING SUMMARY")
    print("="*60)

    print(f"\nTotal projects: {stats['total_projects']}")
    print(f"Already tagged: {stats['already_tagged']}")
    print(f"Projects to be updated: {stats['newly_tagged']}")
    print(f"Total new tags to add: {stats['tags_added']}")
    print(f"Projects unchanged: {stats['unchanged']}")

    if changes:
        print("\n" + "-"*60)
        print("CHANGES" + (" (DRY RUN - NOT APPLIED)" if dry_run else ""))
        print("-"*60)

        for change in changes:
            print(f"\n📁 {change['name']}")
            if change['old_tags']:
                print(f"   Current tags: {', '.join(change['old_tags'])}")
            else:
                print(f"   Current tags: (none)")
            print(f"   Adding tags:  {', '.join(change['new_tags'])}")
            print(f"   Final tags:   {', '.join(change['final_tags'])}")

    print("\n" + "="*60)

    if dry_run and changes:
        print("\n💡 Run without --dry-run to apply these changes")
    elif not dry_run and changes:
        print("\n✓ Changes have been applied!")
        print("💡 Restart VS Code to see the updated tags")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Auto-tag VS Code Project Manager favorites"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying files"
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Skip creating a backup (not recommended)"
    )

    args = parser.parse_args()

    print("🏷️  VS Code Project Manager Auto-Tagger")
    print()

    if not PROJECTS_FILE.exists():
        print(f"❌ Error: Projects file not found at {PROJECTS_FILE}")
        print("   Make sure Project Manager extension is installed and has projects.")
        return 1

    if not args.dry_run and not args.no_backup:
        if not backup_projects_file():
            return 1

    stats, changes = auto_tag_projects(dry_run=args.dry_run)
    print_summary(stats, changes, args.dry_run)

    return 0


if __name__ == "__main__":
    exit(main())
