# SOC Log Analyzer 🔍

A Python-based **Security Operations Center (SOC) automation tool** that detects brute force attacks from system logs, performs threat intelligence lookups, and automatically blocks malicious IP addresses.

This project simulates a **real-world SOC workflow** used by cybersecurity analysts.

---

# Features

- Real-time log monitoring
- SSH brute force detection
- Threat intelligence lookup
- Automated attacker blocking
- SOC-style alert output
- Security incident simulation

---

# How It Works

The tool monitors authentication logs (`auth.log`) and detects repeated failed login attempts.

Workflow:

1. Monitor authentication logs
2. Detect repeated failed SSH login attempts
3. Extract attacker IP address
4. Perform threat intelligence lookup
5. Generate SOC alert
6. Automatically block malicious IP using firewall rules

---

# Project Structure



---

# Installation

Clone the repository:
