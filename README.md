# Dns-exfiltration

in the last report of kaspersky , we can see clearly that hackers tend to use steganography to hide their malicious activities of tools of detection and protection.Dns exfiltration is a sophisticated steganography technique used by hackers to transmit sensitive data from an infected system to a hacker system in a "silence" way . the main idea of this technique is based on this vulnerability:"DNS is a legitime protocole, we should not make any rules or surveillance to control the flow transmitted by dns packets",the scenario of the attack is so simple:
1-the hacker create a fake  DNS-server and start listening for incoming requests
2-the malware that reside in the infected system start sending data which is embeded in dns pakcets to the fake dns-server 
3-the fake dns-server respond to the dns-request with a random address ip
You can find an example of this scenario in this repository.
