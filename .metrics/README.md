# Slash Command Metrics

This directory contains metrics tracking for the slash commands repository.

## Files

- **`command_counts.csv`** - Historical record of slash command counts by date
- **`generate_graph.py`** - Python script to visualize command growth over time
- **`command_growth.png`** - Generated graph (gitignored, regenerate as needed)

## How It Works

The pre-commit hook automatically:
1. Counts all `.md` files in `commands-flat/` directory
2. Records the count with today's date in `command_counts.csv`
3. Only adds one entry per calendar date (prevents duplicate entries)

## Generating the Graph

To visualize the command growth over time:

```bash
cd .metrics
python3 generate_graph.py
```

Or using the Python script directly:

```bash
./generate_graph.py
```

### Requirements

The graph generation requires:
- Python 3.x
- pandas
- matplotlib

Install dependencies:

```bash
pip install pandas matplotlib
```

Or with uv:

```bash
uv pip install pandas matplotlib
```

## Data Format

The CSV file uses the following format:

```csv
date,count
2025-10-26,357
2025-10-27,360
```

- **date**: YYYY-MM-DD format
- **count**: Total number of slash command files

## Notes

- The count is updated automatically during commits
- Only one count per day is recorded (subsequent commits on the same day won't add duplicates)
- The graph image is gitignored but the data CSV is tracked
- Commands are counted from the `commands-flat/` directory after the flatten process runs
