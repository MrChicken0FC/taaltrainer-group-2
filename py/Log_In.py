import os
import json

#variable levels
level1 = (0)

#pathing
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INLOG_PATH = os.path.join(BASE_DIR, "AccountData", "Account.json")

#Json load
try:
    with open(INLOG_PATH, "r", encoding="utf-8") as f:
        inlog = json.load(f)
except:
    inlog = {}

if "Accounts" not in inlog:
    inlog["Accounts"] = []

#def functions
def save_inlog():
    os.makedirs(os.path.dirname(INLOG_PATH), exist_ok=True)
    with open(INLOG_PATH, "w", encoding="utf-8") as f:
        json.dump(inlog, f, indent=2)
    print("Saved to:", INLOG_PATH)

def account_bestaat(email, wachtwoord):
    for account in inlog["Accounts"]:
        if account["email"] == email and account["wachtwoord"] == wachtwoord:
            return True
    return False
def voeg_level_toe(email, level):
    for account in inlog["Accounts"]:
        if account["email"] == email:

            if "data" not in account:
                account["data"] = {"levels_unlocked": []}

            if level not in account["data"]["levels_unlocked"]:
                account["data"]["levels_unlocked"].append(level)

            save_inlog()
            return True

    return False


#mail check
EmailCheck = (
# .com
"@gmail.com",
"@googlemail.com",
"@outlook.com",
"@hotmail.com",
"@icloud.com",
"@yahoo.com",
"@live.com",
"@msn.com",
"@aol.com",
"@protonmail.com",
"@pm.me",
"@mail.com",
"@gmx.com",
"@gmx.net",
"@zoho.com",
"@yandex.com",
"@fastmail.com",
"@hushmail.com",
"@tutanota.com",
"@tuta.com",
"@inbox.com",
"@me.com",
"@mac.com",

# .nl
"@gmail.nl",
"@outlook.nl",
"@hotmail.nl",
"@icloud.nl",
"@yahoo.nl",
"@live.nl",
"@msn.nl",
"@ziggo.nl",
"@kpnmail.nl",
"@kpnplanet.nl",
"@planet.nl",
"@xs4all.nl",
"@telfort.nl",
"@upcmail.nl",
"@home.nl",
"@chello.nl",
"@casema.nl",
"@zonnet.nl",
"@quicknet.nl",
"@hetnet.nl",
"@online.nl",
"@solcon.nl",
"@freeler.nl",

# overige
"@gmail.co.uk",
"@yahoo.co.uk",
"@hotmail.co.uk",
"@outlook.co.uk",
"@yandex.ru",
"@mail.ru",
"@bk.ru",
"@list.ru",
"@internet.ru",
"@qq.com",
"@163.com",
"@126.com"
)
#sign in
while True:
    email = input("Voer uw email in:\n")
    wachtwoord = input("Voer uw wachtwoord in:\n")
    if account_bestaat(email, wachtwoord):
        print("Inloggen gelukt!!!")
        
            
        break
    else:
        print("De mail of het wachtwoord is fout")
        continue