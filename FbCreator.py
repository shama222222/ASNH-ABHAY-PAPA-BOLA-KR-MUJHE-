def liness():
		print('\u001b[37m' + '[>] ================================')
	
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;31;1m'  # mode 31 = red foreground
RESET = '\033[1;37;1m'  # mode 0  = reset
BLUE = "\033[1;36;1m"
WHITE = "\033[1;30;1m",
YELLOW = "\033[1;37;1m",
CYAN = "\033[1;36;1m"
MAGENTA = "\033[1;37;1m",
GREEN = "\033[1;32;1m"
RESET = "\033[1;37;1m"
BOLD = '\033[1;37;1m'
REVERSE = "\033[1;37;1m"



def logo():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    x = """
 
 
 /$$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$ /$$      
| $$__  $$ /$$__  $$| $$  | $$| $$  | $$| $$      
| $$  \ $$| $$  \ $$| $$  | $$| $$  | $$| $$      
| $$$$$$$/| $$$$$$$$| $$$$$$$$| $$  | $$| $$      
| $$__  $$| $$__  $$| $$__  $$| $$  | $$| $$      
| $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$      
| $$  | $$| $$  | $$| $$  | $$|  $$$$$$/| $$$$$$$$
|__/  |__/|__/  |__/|__/  |__/ \______/ |________/
"""
       
logo()
print('''\033[1;33m---------------------------------------------------------------------\n''')
def venom():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    y = '''
\033[1;97m╔═════════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mN4M3    \033[1;91m: \033[1;96mSOURAV TIWARI \033[1;97m                       
\033[1;97m║\033[1;93m* \033[1;97mRULL3X  \033[1;91m: \033[1;96mNO RUL3X N0 G9NG \033[1;97m         
\033[1;97m║\033[1;93m* \033[1;97mBR9ND   \033[1;91m: \033[1;96mMR R9HUL H3R3  \033[1;97m             
\033[1;97m║\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;96mhttps://www.facebook.com/R4HULD0NH3R3\033[1;97m.   
\033[1;97m║\033[1;93m* \033[1;97mWH9TS99P N0. \033[1;91m: \033[1;96m+91 9106****71\033[1;97m                           
\033[1;97m╚═════════════════════════════════════════════════════════════╝

'''
    for N, line in enumerate(y.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
    	
venom()
print('''\033[1;32m[#] _ KATTAR HINDU == > [ Jai Shree Ram ❤️💪]\n''')
import requests
import random
import string
import json
import hashlib
from faker import Faker
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))
def get_mail_domains():
    url = "https://api.mail.tm/domains"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            print(f'[×] E-mail Error : {response.text}')
            return None
    except Exception as e:
        print(f'[×] Error : {e}')
        return None
def create_mail_tm_account():
    fake = Faker()
    mail_domains = get_mail_domains()
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = generate_random_string(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = "https://api.mail.tm/accounts"
        headers = {"Content-Type": "application/json"}
        data = {"address": f"{username}@{domain}", "password":password}       
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                print(f'')
                return f"{username}@{domain}", password, first_name, last_name, birthday
            else:
                print(f'[×] Email Error : {response.text}')
                return None, None, None, None, None
        except Exception as e:
            print(f'[×] Error : {e}')
            return None, None, None, None, None
def register_facebook_account(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    req = {'api_key': api_key,'attempt_login': True,'birthday': birthday.strftime('%Y-%m-%d'),'client_country_code': 'EN','fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod','fb_api_req_friendly_name': 'registerAccount','firstname': first_name,'format': 'json','gender': gender,'lastname': last_name,'email': email,'locale': 'en_US','method': 'user.register','password': password,'reg_instance': generate_random_string(32),'return_multiple_errors': True}
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    reg = _call(api_url, req)
    id=reg['new_user_id']
    token=reg['session_info']['access_token']
    print(f'''
\x1b[38;5;22m⋘▬▭▬▭▬▭▬﴾𓆩OK𓆪﴿▬▭▬▭▬▭▬⋙
﴾𝐕𝐈𝐏﴿ EMAIL : {email}
﴾𝐕𝐈𝐏﴿ ID : {id}
﴾𝐕𝐈𝐏﴿ PASSWORD : {password}
﴾𝐕𝐈𝐏﴿ NAME : {first_name} {last_name}
﴾𝐕𝐈𝐏﴿ BIRTHDAY : {birthday} 
﴾𝐕𝐈𝐏﴿GENDER : {gender}
⋘▬▭▬▭▬▭▬﴾𓆩OK𓆪﴿▬▭▬▭▬▭▬⋙
﴾𝐕𝐈𝐏﴿ Token : {token}
⋘▬▭▬▭▬▭▬﴾𓆩OK𓆪﴿▬▭▬▭▬▭▬⋙''')
open('username.txt','a')
def _call(url, params, post=True):
    headers = {'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'}
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()
for i in range(int(input('[+] How Many Accounts You Want:  '))):
 email, password, first_name, last_name, birthday = create_mail_tm_account()
 if email and password and first_name and last_name and birthday:
  register_facebook_account(email, password, first_name, last_name, birthday)
print('\x1b[38;5;208m⇼'*60)  
