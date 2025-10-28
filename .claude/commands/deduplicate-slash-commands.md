I need you to identify and resolve duplicate slash commands in this repository.

**The Problem:**
This repository maintains slash commands in a hierarchical structure under `commands/`, which are then flattened into `commands-flat/` and synced to `~/.claude/commands/`. When multiple files with the same name exist in different subdirectories, the sync script adds numeric suffixes (`-2`, `-3`, etc.), creating confusion for users.

**Your Task:**

1. **Identify duplicates**: Search for files with identical names in different locations within the `commands/` directory
   - Use: `find commands -type f -name "*.md" -printf "%f\n" | sort | uniq -d`
   - For each duplicate found, locate all instances: `find commands -name "filename.md"`

2. **Compare and decide**: For each set of duplicates:
   - Compare file contents using `diff`
   - If **identical**: Delete all but one copy (keep the version in the most logical location)
   - If **different**: Rename each file to have a descriptive, unique name that clearly indicates its purpose

3. **Naming guidelines** for different files:
   - Names must clearly convey what the command does
   - Use descriptive prefixes or suffixes (e.g., `create-repo-index.md` vs `add-index-badge-and-structure.md`)
   - Avoid generic names that could apply to multiple contexts

4. **Run sync**: After resolving duplicates, run `bash sync-commands.sh` to regenerate the flattened commands

5. **Verify**: Confirm no collisions are reported in the sync output and no `-2`, `-3`, etc. files exist in `commands-flat/` or `~/.claude/commands/`

**Success Criteria:**
- No filename collisions during sync
- No files with numeric suffixes in `commands-flat/` or `~/.claude/commands/`
- All commands have clear, descriptive names
- Total command count matches between `commands-flat/` and `~/.claude/commands/`
