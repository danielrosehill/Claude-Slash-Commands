---
description: Check BTRFS filesystem health and Snapper snapshot status
tags: [sysadmin, btrfs, snapper, filesystem, snapshots, health]
---

Check BTRFS filesystem health and Snapper snapshot management:

1. **BTRFS Filesystem Health**: Check filesystem status, errors, and statistics
2. **Disk Usage**: Analyze BTRFS disk usage including metadata and data
3. **Snapper Status**: Check snapshot configurations and recent snapshots
4. **Latest Snapshots**: Show the most recent snapshots and their details
5. **Snapshot Disk Usage**: Analyze space used by snapshots
6. **Scrub Status**: Check if scrub is needed or show last scrub results

Run the following diagnostic commands:

**BTRFS Health:**
- `sudo btrfs filesystem show` for filesystem overview
- `sudo btrfs filesystem df /` for detailed space usage (adjust mount point as needed)
- `sudo btrfs device stats /` for device error statistics
- `sudo btrfs filesystem usage /` for comprehensive usage breakdown

**Scrub Status:**
- `sudo btrfs scrub status /` to check scrub status
- Recommend running `sudo btrfs scrub start /` if scrub hasn't been done recently

**Snapper Configuration:**
- `sudo snapper list-configs` to show all snapshot configurations
- `sudo snapper -c root list` to list snapshots for root config (adjust config name as needed)
- `sudo snapper -c root list --columns number,date,description | tail -n 10` for latest 10 snapshots

**Snapshot Space Usage:**
- `sudo snapper -c root list --columns number,pre-number,date,used-space,cleanup` for space analysis
- `sudo btrfs qgroup show /` for quota group information (if quotas enabled)

**Latest Snapshot Details:**
- Show the most recent snapshot number, date, and description
- Show pre/post snapshot pairs if using zypper/YaST integration

Analyze the output and provide:
- Overall BTRFS filesystem health status
- Any errors or warnings in device statistics
- Current disk usage and available space
- Number of snapshots and total space used by snapshots
- Details of the latest snapshot(s)
- Recommendations for:
  - Running a scrub if needed
  - Cleaning up old snapshots if space is low
  - Any filesystem maintenance needed
- Whether automatic snapshot cleanup is working properly

Note: Adjust mount points and config names based on the actual system configuration.
