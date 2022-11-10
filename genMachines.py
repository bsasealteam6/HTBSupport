import http.client
import os
import json
from dotenv import load_dotenv
import sys

load_dotenv()


conn = http.client.HTTPSConnection("www.hackthebox.com")
payload = ''
headers = {
    'Authorization': f'Bearer {os.environ["HTB_TOKEN"]}'
}
conn.request("GET", "/api/v4/machine/list", payload, headers)
res = conn.getresponse()
data = res.read()
# print(data.decode("utf-8"))
machines = json.loads(data.decode("utf-8"))
newHosts = "\n#Hack the Box:"
for i in machines['info']:
    newHosts = (f'{newHosts}\n{i["ip"]}\t{i["name"].lower()}.htb')
# print(newHosts)
if len(sys.argv) == 1:
    template = open("/etc/hosts.template", "r").read()
    output = open("/etc/hosts", "w")
    hosts = template.replace("{HTB}", newHosts)
    output.write(hosts)
elif len(sys.argv) == 2:
    if sys.argv[1] == "print" or sys.argv[1] == "-p":
        print(newHosts)
    elif sys.argv[1] == "update" or sys.argv[1] == "-u":
        template = open("/etc/hosts.template", "r").read()
        output = open("/etc/hosts", "w")
        hosts = template.replace("{HTB}", newHosts)
        output.write(hosts)
    elif sys.argv[1] == "help" or sys.argv[1] == "-h":
        print("""Usage: genMachines.py [OPTION]
              - print: prints the new hosts to the terminal
              - update: updates the /etc/hosts file
              - help: prints this message
              - no option: updates the /etc/hosts file
              """)
    else:
        print("Invalid argument")
