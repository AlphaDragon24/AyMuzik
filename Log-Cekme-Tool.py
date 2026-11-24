import requests
import webbrowser
print("\x1b[1;39m—"*60)
print("\033[1;33m")
print("""
//  **         *******     ******** 
// /**        **/////**   **//////**
// /**       **     //** **      // 
// /**      /**      /**/**         
// /**      /**      /**/**    *****
// /**      //**     ** //**  ////**
// /******** //*******   //******** 
// ////////   ///////     ////////  
""")

print("\033[0m")
print("~ Programmer : @daluj | Channel: @ThomasFederasyonu ~")
webbrowser.open("https://t.me/ThomasFederasyonu")
api = "https://rootturkey.xyz/log"
print("\x1b[1;39m—"*60)
kuz = input("\x1b[1;36m URL gir (Steam): ")
params = {
    "url": kuz,
    "limit": 5000
}

response = requests.get(api, params=params)
dosya_adi = f"@{kuz}-Steam.txt"
with open(dosya_adi, "w", encoding="utf-8") as f:
    f.write(response.text)
print(response.text)    
print("\x1b[1;39m—"*60)
print(f"\x1b[1;32mKaydettim✅ {dosya_adi}")