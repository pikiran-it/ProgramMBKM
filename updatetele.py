import requests
from time import *
import json
import realhttp

base_url = "http://localhost:58000/api/v1"
user = "bahrani"
password = "bahrani"


def get_ticket():
    headers = {"content-type": "application/json"}
    data = {"username": user, "password": password}

    response = requests.post(base_url+"/ticket", headers=headers, json=data)
    ticket = response.json()
    service_ticket = ticket["response"]["serviceTicket"]
    return service_ticket

if __name__ == "__main__":
    ticket = get_ticket()
    print("Service Tiket:",ticket)

def get_network_health():
    ticket = get_ticket()
    headers = {"X-Auth-Token": ticket}
    response = requests.get(base_url+"/assurance/health", headers=headers)
    health = response.json()
    network_health = health['response'][0]['networkDevices']['totalPercentage']
    return network_health

if __name__ == "__main__":
    network_health = get_network_health()
    print("Presentase Network Health:"+ network_health +"%")
