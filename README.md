SSH Honeypot Attack Analysis Project

Overview

This project demonstrates how to simulate and analyze SSH brute-force attacks using a honeypot.

Tools Used

(1) Cowrie (SSH Honeypot)
(2) Hydra(Attack Simulation)
(3) Python (Log Analysis)

What I Did

1. Deployed a Cowrie honeypot to capture attacker activity
2. Simulated brute-force attacks using hydra
3. Collected and analyzed attack logs
4. Built a Python script to extract:
      * Top attacking IP addresses
      * Most used passwords
      * Most targeted usernames

Key Findings

1. Attackers frequently targetted the "root" account
2. Weak passwords like "1234" were commonly used
3. A single IP performed multiple login attempts

Project Structure

* scripts/ = Python analysis scripts
* reports/ = Generated attack reports
* data/ =  processed logs

  ## Screenshots

### Hydra Attack
![Hydra](screenshots/hydra.png)

### Cowrie Logs
![Logs](screenshots/cowrie_logs.png)

### Analyzer Output
![Output](screenshots/analyzer.png)

Conclusion

This project demonstrates basic threat detection and log analysis using honeypot environment.

