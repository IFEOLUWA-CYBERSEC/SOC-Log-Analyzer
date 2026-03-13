import re
import os
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = os.path.join(BASE_DIR, "logs", "auth.log")

pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")

attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            attempts[ip] += 1

for ip, count in attempts.items():
    if count >= 5:
        print(f"🚨 ALERT: Possible SSH brute force attack from {ip} ({count} failed attempts)")
