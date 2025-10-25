Add YAML frontmatter to slash commands that are missing it.

The frontmatter should include:
- title: A clear, descriptive title for the command
- description: A brief description of what the command does
- category: The category/domain (derived from folder structure)
- tags: Relevant tags for searchability

Example frontmatter:
```yaml
---
title: Review Code for Security Issues
description: Performs a security audit of code looking for common vulnerabilities
category: cybersecurity
tags: [security, audit, vulnerability-scanning]
---
```

Your task:
1. Scan through commands/public and commands/private
2. Identify files without frontmatter
3. For each file, generate appropriate frontmatter based on:
   - The command content
   - Its location in the folder structure
   - The purpose/function of the command
4. Show me the proposed frontmatter for each file

After showing the proposals, ask if I want you to add the frontmatter to the files or if I want to modify any of them first.

Note: Preserve all existing content - only ADD frontmatter at the beginning of files that don't have it.
