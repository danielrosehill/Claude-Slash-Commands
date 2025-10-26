#!/usr/bin/env python3
"""
Generate a graph showing slash command count over time.
Reads from command_counts.csv and creates a visualization.
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path

# Configuration
SCRIPT_DIR = Path(__file__).parent
CSV_FILE = SCRIPT_DIR / "command_counts.csv"
OUTPUT_FILE = SCRIPT_DIR / "command_growth.png"

def generate_graph():
    """Generate and save the command count graph."""

    # Check if CSV file exists
    if not CSV_FILE.exists():
        print(f"Error: {CSV_FILE} not found")
        return

    # Read the CSV file
    df = pd.read_csv(CSV_FILE)

    # Check if there's data
    if len(df) == 0:
        print("No data to plot yet")
        return

    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Sort by date
    df = df.sort_values('date')

    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['count'], marker='o', linewidth=2, markersize=6, color='#4A90E2')

    # Styling
    plt.title('Slash Command Count Over Time', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Commands', fontsize=12, fontweight='bold')
    plt.grid(True, alpha=0.3, linestyle='--')

    # Format x-axis to show dates nicely
    plt.gcf().autofmt_xdate()

    # Add some padding to y-axis
    y_min, y_max = plt.ylim()
    plt.ylim(max(0, y_min - 5), y_max + 5)

    # Tight layout to prevent label cutoff
    plt.tight_layout()

    # Save the figure
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
    print(f"Graph saved to: {OUTPUT_FILE}")

    # Also display statistics
    print(f"\nStatistics:")
    print(f"  Total data points: {len(df)}")
    print(f"  Date range: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}")
    print(f"  Current count: {df['count'].iloc[-1]}")
    if len(df) > 1:
        print(f"  Starting count: {df['count'].iloc[0]}")
        print(f"  Total growth: {df['count'].iloc[-1] - df['count'].iloc[0]}")

if __name__ == "__main__":
    generate_graph()
