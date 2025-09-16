import re
ips = []

pattern = r"\d+\.\d+\.\d+\.\d+"
with open('auth.log', 'r') as f:
    ips = re.findall(pattern, str(f.readlines()))

unique_ips = set(ips)

with open('unique_ips.txt', 'w') as g:
    for ip in unique_ips:
        g.write(ip)
        g.write("\n")


