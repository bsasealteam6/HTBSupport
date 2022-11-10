import http.client
import os
import json
from dotenv import load_dotenv

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
template = open("/etc/hosts.template", "r").read()
output = open("/etc/hosts", "w")
newHosts = "\n#Hack the Box:"
for i in machines['info']:
    newHosts = (f'{newHosts}\n{i["ip"]}\t{i["name"].lower()}.htb')
# print(newHosts)
hosts = template.replace("{HTB}", newHosts)
output.write(hosts)
