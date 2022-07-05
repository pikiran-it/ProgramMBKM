import json
import requests
api_url = "http://localhost:58000/api/v1/host"

headers={"X-Auth-Token": "NC-20-04da8b9da3a14fddb328-nbi"}

resp = requests.get(api_url, headers=headers, verify=False)

print("Request status: ", resp.status_code)

response_json = resp.json()
hosts = response_json["response"]

 for host in hosts:
    print(host["hostName"], "\t", host["hostIp"], "\t", host["hostMac"], "\t", host["connectedInterfaceName"])

