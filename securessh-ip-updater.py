import socket
import os

_ = "\t"
hosts = ['foo-smartphone', 'foo-lavoro','foo-pc','foo-homelab'] # DuckDNS domains
rule = "# Accesso consentito solo da questi IP \nsshd: 127.0.0.1 \nsshd: 192.168.1." 

print("\nRitrovamento indirizzi IP dai DDNS...")
for host in hosts:
    host = host + ".duckdns.org"
    try     : ip = socket.gethostbyname(host)
    except  : ip = "127.0.0.1"

    if ip:
        print(f"DDNS: ['{host}': {ip}]")
        rule = f"{rule}\nsshd: {ip} \t#{host}"

print("\nRegola per gli accessi SSH remoti e locali")
print("--- INIZIO REGOLA ---")
print(f"\n{rule}\n")
print("--- FINE REGOLA ---")

if os.path.exists("/etc/hosts.allow"):
    print("\nScrittura della regola...")
    with open("/etc/hosts.allow", 'w') as f:
        f.write(rule+"\n")
else:
    print("File non trovato")

print("Okay")
