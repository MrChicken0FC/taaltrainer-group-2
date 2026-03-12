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