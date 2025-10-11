---
description: Diagnose system slowdown and performance issues by checking CPU, memory, disk I/O, and process activity
tags: [sysadmin, diagnostics, performance, slowdown, troubleshooting]
---

Diagnose system slowdown and identify performance bottlenecks:

1. **CPU Usage**: Check current CPU usage and identify top CPU-consuming processes
2. **Memory Usage**: Analyze RAM and swap usage, identify memory-heavy processes
3. **Disk I/O**: Check for disk I/O bottlenecks and high I/O processes
4. **Load Average**: Check system load averages
5. **Process Analysis**: Identify zombie processes, high-priority processes, and resource hogs
6. **Network Activity**: Check for network-related slowdowns if applicable

Run the following diagnostic commands:
- `top -b -n 1 | head -n 20` for quick overview
- `free -h` for memory usage
- `df -h` for disk space
- `iostat -x 1 5` for disk I/O statistics (requires sysstat package)
- `vmstat 1 5` for virtual memory statistics
- `ps aux --sort=-%cpu | head -n 10` for top CPU processes
- `ps aux --sort=-%mem | head -n 10` for top memory processes
- `uptime` for load averages

Analyze the output and provide:
- Identification of the primary bottleneck (CPU, RAM, disk I/O, or swap)
- List of top resource-consuming processes
- Recommendations for addressing the slowdown
- Whether the issue is transient or persistent

If sysstat is not installed, offer to install it with `sudo apt-get install sysstat`.
