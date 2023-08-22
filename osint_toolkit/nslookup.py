"""
    Automated script to get all informations from nslookup

    Author: @lubiku35
"""
import os

# COMMANDS


def main():
    ip = input("Provide IP / Domain: ")
    out(ip=ip)


def nslookup(ip):
    # COMMANDS
    a = os.popen(f"nslookup -type=A {ip}").read()
    mx = os.popen(f"nslookup -type=MX {ip}").read()
    txt = os.popen(f"nslookup -type=TXT {ip}").read()
    cname = os.popen(f"nslookup -type=CNAME {ip}").read()
    return [a, mx, txt, cname]

def out(ip):
    outputs = nslookup(ip=ip)
    strings = [
        "\t #### a | IPv4 ####\n", 
        "\t #### mx | Mail Servers ####\n", 
        "\t #### txt | TXT Records ####\n", 
        "\t #### cname | Canonical Name ####\n"]
    
    for i in range(len(strings)):
        print(strings[i])
        print(outputs[i]) 

    with open(f"{ip}_ns.log", "w") as f:
        for i in range(len(strings)):
            f.write(strings[i])
            f.write(outputs[i]) 
        print(f"Data written to file: {ip}_ns.log")
    return 

if __name__ == "__main__":
    main()