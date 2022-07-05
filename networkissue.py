import json
import requests

api_url = "http://localhost:58000/api/v1/assurance/health-issues"
headers={"X-Auth-Token": "NC-20-04da8b9da3a14fddb328-nbi"}
issues = requests.get(api_url, headers=headers, verify=False)
print("Request status: ", issues.status_code)


def get_network_issues():
    issue_details = issues.json()
    devices = len(issue_details['response'])
    output = "Peringatan! Terjadi gangguan akses ke "+ str(devices) +" perangkat berikut:\n"
    output += "-"*60 +"\n"
    output += "NO.| PERANGKAT |     WAKTU       |   DESKRIPSI\n"
    output +="-"*60 +"\n"
    number=1
    for device in issue_details['response']:
        output += ""+ str(number) +".| "+ device['issueSource'] +" | "+ device['issueTimestamp'] +" | "+ device['issueDescription'] +"\n"
        number +=1
    return output
if __name__ == "__main__":
    get_network_issues = get_network_issues()
    print(get_network_issues)