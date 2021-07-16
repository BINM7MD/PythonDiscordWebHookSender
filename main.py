from colorama import Fore, Back, Style
import requests
import json
def banner():
 print(Fore.RED + '''\
██   ██ ███████ ██   ██ 
██   ██ ██       ██ ██  
███████ █████     ███   
██   ██ ██       ██ ██  
██   ██ ███████ ██   ██                                           
  ''')

banner()
print(Fore.RED + "[HEX] Enter Your Message Content : ")
MessageContent = input()
print(Fore.RED + "[HEX] Enter Your WebHook :  ")
WebHook = input()
print(Fore.RED + "[HEX] Enter Username : ")
User = input()
data = {
    'username': f"{User}",
    'content': f"{MessageContent}"
}
response = requests.post(WebHook, data=json.dumps(data), headers={'Content-Type': 'application/json'})
