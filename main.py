import requests
from time import *
import telebot

api_uri = "http://localhost:58000/api/v1"
user = "bahrani"
password = "bahrani"

bot = telebot.TeleBot('5585856294:AAEGtdWJlVrJWnDeAuN1jq0lW2vNw22MvcI')

def get_ticket():
    headers = {"content-type": "application/json"}
    data = {"username": user, "password": password}

    response = requests.post(api_uri+"/ticket", headers=headers, json=data)
    ticket = response.json()
    service_ticket = ticket["response"]["serviceTicket"]
    return service_ticket

if __name__ == "__main__":
    tiket= get_ticket()
    print(tiket)


def get_network_health():
     ticket = get_ticket()
     headers = {"X-Auth-Token": ticket}
     response = requests.get(api_uri+"/assurance/health", headers=headers)
     health = response.json()
     network_health = health['response'][0]['networkDevices']['totalPercentage']
     return network_health

if __name__ == "__main__":
    h= get_network_health()
    print(h)

def get_network_issues():
    ticket = get_ticket()
    headers = {'Accept': 'application/yang-data+json', 'X-Auth-Token': ticket}
    issues = requests.get(url = api_uri + "/assurance/health-issues", headers=headers)
    issue_details = issues.json()
    devices = len(issue_details['response'])
    output = "Peringatan! Terjadi gangguan akses ke "+ str(devices) +" perangkat berikut:\n"
    output += "-"*60 +"\n"
    output += "NO. | PERANGKAT | WAKTU | DESKRIPSI\n"
    output +="-"*60 +"\n"
    number=1
    for device in issue_details['response']:
        output += ""+ str(number) +". | "+ device['issueSource'] +" | "+ device['issueTimestamp'] +" | "+ device['issueDescription'] +"\n"
        number +=1
    return output

if __name__ == "__main__":
    i= get_network_issues()
    print(i)

# def get_hosts():
#     ticket = get_ticket()
#     headers = {'Accept': 'application/yang-data+json', 'X-Auth-Token': ticket}
#     hosts = requests.get(url = api_uri + "/host", headers=headers)
#     hosts_details = hosts.json()
#     #devices = len(hosts_details['response'])
#     # hs = "Peringatan! Terjadi gangguan akses ke "+ str(devices) +" perangkat berikut:\n"
#     # hs += "-"*60 +"\n"
#     # hs += "NO. | PERANGKAT | WAKTU | DESKRIPSI\n"
#     # hs +="-"*60 +"\n"
#     # number=1
#     for host in hosts_details['response']:
#         print(host["hostName"], "\t", host["hostIp"], "\t", host["hostMac"], "\t", host["connectedInterfaceName"])
    
# if __name__ == "__main__":
#     h = get_hosts()
#     print(h)

@bot.message_handler(commands=['help','start'])
def tes(message):
    # membalas pesan
    bot.reply_to(message,'''Fungsi Yang Disediakan 
/tiket - mendapatkan Token 
/issues - Menanpilkan Health Issues
/health - Menampilkan Kesehatan Perangkat
''')


@bot.message_handler(commands=['tiket'])
def tiket(message):
    print("Ada yang Requst Token")
    bot.send_message(message.chat.id,get_ticket())

@bot.message_handler(commands=['issues'])
def kamu(message):
    print("Ada yang Requst Health Issues")
    bot.send_message(message.chat.id,get_network_issues())

@bot.message_handler(commands=['health'])
def kamu(message):
    print("Ada yang Requst Network Health")
    bot.send_message(message.chat.id,get_network_health())


bot.polling()