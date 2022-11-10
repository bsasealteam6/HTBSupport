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
for i in machines['info']:
    print(f'{i["ip"]}\t{i["name"].lower()}.htb')
