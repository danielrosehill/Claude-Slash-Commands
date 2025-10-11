#!/usr/bin/env python3
"""
Fetch GitHub repository information and format into organized markdown.
"""

import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get GitHub API key
GITHUB_TOKEN = os.getenv('GITHUB_API_KEY')

# List of repository URLs
repos = [
    "https://github.com/iannuttall/claude-sessions",
    "https://github.com/wshobson/commands",
    "https://github.com/qdhenry/Claude-Command-Suite",
    "https://github.com/papaoloba/spec-based-claude-code",
    "https://github.com/hikarubw/claude-commands",
    "https://github.com/Divyanshubansaldb/claude-code-session-manager",
    "https://github.com/IgorWarzocha/CCCT",
    "https://github.com/ctoth/slashcommands",
    "https://github.com/artemgetmann/claude-slash-commands",
    "https://github.com/jeremyeder/claude-slash",
    "https://github.com/drdator/ccm",
    "https://github.com/sugarshin/.claude-code-slash-commands",
    "https://github.com/SerjoschDuering/ClaudeCodeSlashPrompts",
    "https://github.com/ccalvarez/claude-code-commands",
    "https://github.com/masamerc/ccsc",
]

def get_repo_info(owner, repo):
    """Fetch repository information from GitHub API."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {owner}/{repo}: {e}")
        return None

def format_date(date_string):
    """Format ISO date string to readable format."""
    if not date_string:
        return "N/A"
    try:
        dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d')
    except:
        return date_string

def create_markdown_entry(repo_data):
    """Create markdown entry for a repository."""
    if not repo_data:
        return ""

    name = repo_data.get('name', 'N/A')
    full_name = repo_data.get('full_name', 'N/A')
    description = repo_data.get('description') or 'No description provided'
    stars = repo_data.get('stargazers_count', 0)
    last_updated = format_date(repo_data.get('pushed_at'))
    html_url = repo_data.get('html_url', '')

    # Create badge URLs
    stars_badge = f"![Stars](https://img.shields.io/github/stars/{full_name}?style=social)"
    last_commit_badge = f"![Last Commit](https://img.shields.io/github/last-commit/{full_name})"

    markdown = f"""
### [{name}]({html_url})

**Repository:** `{full_name}`

**Description:** {description}

**Stars:** {stars} {stars_badge}

**Last Updated:** {last_updated} {last_commit_badge}

---
"""
    return markdown

def main():
    """Main function to generate the markdown document."""
    print("Fetching repository information from GitHub API...")

    # Header
    output = """# Claude Code Slash Commands - Community Libraries

This document provides an organized list of community-created slash command libraries and tools for Claude Code.

Last updated: {date}

---

""".format(date=datetime.now().strftime('%Y-%m-%d'))

    repo_data_list = []

    # Fetch all repository data
    for repo_url in repos:
        parts = repo_url.replace('https://github.com/', '').split('/')
        if len(parts) >= 2:
            owner = parts[0]
            repo = parts[1]
            print(f"Fetching {owner}/{repo}...")
            data = get_repo_info(owner, repo)
            if data:
                repo_data_list.append(data)

    # Sort by stars (descending)
    repo_data_list.sort(key=lambda x: x.get('stargazers_count', 0), reverse=True)

    # Generate markdown for each repo
    output += f"## Repositories ({len(repo_data_list)} total)\n\n"

    for repo_data in repo_data_list:
        output += create_markdown_entry(repo_data)

    # Write to file
    output_file = 'ref/other-libs.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"\nSuccessfully updated {output_file}")
    print(f"Total repositories processed: {len(repo_data_list)}")

if __name__ == '__main__':
    main()
