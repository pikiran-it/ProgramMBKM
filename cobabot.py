import telebot
import json
import requests

bot = telebot.TeleBot('5585856294:AAEGtdWJlVrJWnDeAuN1jq0lW2vNw22MvcI')
api_url = "http://localhost:58000/api/v1"
headers = {
    "content-type": "application/json"
}
body_json = {
    "username": "bahrani",
    "password": "bahrani"  
}
resp = requests.post(api_url+"/ticket", json.dumps(body_json), headers=headers, verify=False)
print("Ticket request status: ", resp.status_code)
response_json = resp.json()
serviceTicket = response_json["response"]["serviceTicket"]
serviceTicket = "Token anda: "+serviceTicket+""
# print(serviceTicket)

# def get_network_issues():
#     issues = requests.get(url = api_url+"/assurance/health-issues", headers=headers)
#     issue_details = issues.json()
#     devices = len(issue_details['response'])
#     output = "Peringatan! Terjadi gangguan akses ke "+ str(devices) +" perangkat berikut:\n"
#     output += "-"*60 +"\n"
#     output += "NO.| PERANGKAT |     WAKTU       |   DESKRIPSI\n"
#     output +="-"*60 +"\n"
#     number=1
#     for device in issue_details['response']:
#         output += ""+ str(number) +".| "+ device['issueSource'] +" | "+ device['issueTimestamp'] +" | "+ device['issueDescription'] +"\n"
#         number +=1
#     return output
# if __name__ == "__main__":
#     get_network_issues = get_network_issues()

# Menghandle Pesan /start
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
    print("aku")
    bot.send_message(message.chat.id,serviceTicket)

@bot.message_handler(commands=['issues'])
def kamu(message):
    print("Health Issues")
    bot.send_message(message.chat.id,"get_network_issues")

bot.polling()