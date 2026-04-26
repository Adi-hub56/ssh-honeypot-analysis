import json
from collections import defaultdict

log_file =  "/home/cyrus/cowrie/var/log/cowrie/cowrie.json"

ip_count = defaultdict(int)
passwords = defaultdict(int)
usernames = defaultdict(int)

with open(log_file) as f:
    for line in f:
        try:
            data = json.loads(line)

            if data.get("eventid") == "cowrie.login.success":
                ip = data.get("src_ip")
                password = data.get("password", "unknown" )
                user = data.get("username", "unknown")

                ip_count[ip] += 1
                passwords[password] += 1
                usernames[user] += 1

        except:
            continue

print("\nTop Attacking IPs:")
for ip, count in sorted(ip_count.items(), key=lambda x:[1], reverse=True)[:5]:
    print(f"{ip}  - {count} attempts")

print("\nMost Used Passwords:")
for pwd, count in sorted(passwords.items(), key=lambda x:[1], reverse=True)[:5]:
    print(f"{pwd} - {count} times")

print("\nMost Used Usernames:")
for user, count in sorted(usernames.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{user} - {count} times")

#report path
report_path = "/home/cyrus/honeypot-project/reports/attack_report.txt"

with open(report_path, "w") as report:
    report.write("Top Attacking IPs:\n")
    for ip, count in ip_count.items():
        report.write(f"{ip} - {count} attempts\n")

    report.write("\nMost Used Passwords:\n")
    for pwd, count in passwords.items():
        report.write(f"{pwd} - {count} times\n")

    report.write("\nMost Used Usernames:\n")
    for user, count in usernames.items():
        report.write(f"{user} - {count} times\n")


