import json 
from collections import   defaultdict
log_file = "/home/cyrus/cowrie/var/log/cowrie/cowrie.json"

 ip_count = defaultdict(int)
 passwords = defaultdict(int)

 with open(log_file) as f:
     for  line in f:
          try:
              data = json.loads(line)

                if data.get("eventid") == "cowrie.login.success":
                    ip = data.get("src_ip")
                     password = data.get("password")
                          
                      ip_count[ip] += 1
                      passwords[password] += 1

           execpt:
              continue
  
     print("\n  Top Attacking IPs:")
     for ip, count in ip_count.items():
           print(f"{ip}  -- {count} attempts")


     print("\n Most Used Passwords:")
     for  pwd, count in passwords.items():
           print(f"[pwd} --  {count} times")



