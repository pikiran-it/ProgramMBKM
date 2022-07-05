
import json
import requests
from prettytable import PrettyTable
x = PrettyTable()

api_url = "http://localhost:58000/api/v1/assurance/health-issues"
headers={"X-Auth-Token": "NC-58-7d80b64b6b0f490897af-nbi"}
resp = requests.get(api_url, headers=headers, verify=False)
print("Request status: ", resp.status_code)

response_json = resp.json()
issue_details = response_json["response"]

for host in issue_details:
   x = PrettyTable(["Perangkat"])
   x.add_row(host["issueSource"])
   print(host)



