---
description: Analyze boot logs to diagnose slow boot times and identify boot-time issues
tags: [sysadmin, diagnostics, boot, systemd, logs, troubleshooting]
---

Analyze system boot logs to identify slow boot causes and issues:

1. **Boot Time Analysis**: Show overall boot time and critical-path timing
2. **Slow Services**: Identify services that delayed boot
3. **Failed Services**: Check for any services that failed during boot
4. **Kernel Messages**: Review kernel boot messages for hardware issues
5. **Critical Chain**: Show the critical path of services during boot

Run the following diagnostic commands:

**Boot Time Overview:**
- `systemd-analyze` for total boot time
- `systemd-analyze blame` for service-by-service timing (top 20 slowest)
- `systemd-analyze critical-chain` for critical path analysis

**Boot Logs:**
- `journalctl -b` for current boot logs (use `-b -1` for previous boot)
- `journalctl -b -p err` for errors during current boot
- `journalctl -b -p warning` for warnings during boot
- `dmesg | grep -i error` for kernel errors
- `dmesg | grep -i warning` for kernel warnings

**Failed Services:**
- `systemctl --failed` to show failed services
- `systemctl list-units --state=failed` for detailed failed unit list

Analyze the output and provide:
- Total boot time and comparison to typical boot times
- Top 5 slowest services and whether they can be optimized
- Any failed services and potential impact
- Hardware or driver issues detected in kernel logs
- Specific recommendations for improving boot time
- Whether any services can be disabled or masked safely

Offer to investigate specific slow services in detail if needed.
