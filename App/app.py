from flask import Flask, request, jsonify, session, redirect, render_template
import os
import json

app = Flask(__name__)
app.secret_key = "nieuw_secret_key_456"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INLOG_PATH = os.path.join(BASE_DIR, "AccountData", "Account.json")

try:
    with open(INLOG_PATH, "r", encoding="utf-8") as f:
        inlog = json.load(f)
except:
    inlog = {"Accounts": []}

def save_inlog():
    os.makedirs(os.path.dirname(INLOG_PATH), exist_ok=True)
    with open(INLOG_PATH, "w", encoding="utf-8") as f:
        json.dump(inlog, f, indent=2)

def get_account(email):
    for acc in inlog["Accounts"]:
        if acc["email"] == email:
            return acc
    return None

def login_required():
    if "user" not in session:
        return redirect("/login")
    return None

@app.route("/")
def home():
    if "user" in session:
        return redirect("/main")
    return redirect("/login")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/vergeten")
def vergeten_page():
    return render_template("WachtwoordVergeten.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/main")
def main():
    if "user" not in session:
        return redirect("/login")
    return render_template("main.html")

# Frans
@app.route("/frans")
def frans_page():
    if "user" not in session: return redirect("/login")
    return render_template("frans.html")

@app.route("/franslvl1")
def franslvl1():
    if "user" not in session: return redirect("/login")
    return render_template("Frans_levels/level1frans.html")

@app.route("/franslvl2")
def franslvl2():
    if "user" not in session: return redirect("/login")
    return render_template("Frans_levels/level2frans.html")

@app.route("/franslvl3")
def franslvl3():
    if "user" not in session: return redirect("/login")
    return render_template("Frans_levels/level3frans.html")

@app.route("/franslvl4")
def franslvl4():
    if "user" not in session: return redirect("/login")
    return render_template("Frans_levels/level4frans.html")

@app.route("/franslvl5")
def franslvl5():
    if "user" not in session: return redirect("/login")
    return render_template("Frans_levels/level5frans.html")

@app.route("/franslvl6")
def franslvl6():
    if "user" not in session: return redirect("/login")
    return render_template("Frans_levels/level6frans.html")

# Latijns
@app.route("/latijns")
def latijns_page():
    if "user" not in session: return redirect("/login")
    return render_template("Latijns.html")

@app.route("/latijnslvl1")
def latijnslvl1():
    if "user" not in session: return redirect("/login")
    return render_template("Latijs_levels/level1latijn.html")

@app.route("/latijnslvl2")
def latijnslvl2():
    if "user" not in session: return redirect("/login")
    return render_template("Latijs_levels/level2latijn.html")

@app.route("/latijnslvl3")
def latijnslvl3():
    if "user" not in session: return redirect("/login")
    return render_template("Latijs_levels/level3latijn.html")

@app.route("/latijnslvl4")
def latijnslvl4():
    if "user" not in session: return redirect("/login")
    return render_template("Latijs_levels/level4latijn.html")

@app.route("/latijnslvl5")
def latijnslvl5():
    if "user" not in session: return redirect("/login")
    return render_template("Latijs_levels/level5latijn.html")

@app.route("/latijnslvl6")
def latijnslvl6():
    if "user" not in session: return redirect("/login")
    return render_template("Latijs_levels/level6latijn.html")

@app.route("/levels/<language>")
def levels(language):
    if "user" not in session: return redirect("/login")
    acc = get_account(session["user"])
    unlocked = acc["data"].get(language, [1])
    return render_template("levels.html", language=language, unlocked=unlocked)

@app.route("/play/<language>/<int:level>")
def play(language, level):
    if "user" not in session: return redirect("/login")
    return render_template("play.html", language=language, level=level)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    acc = get_account(data.get("email"))
    if acc and acc["wachtwoord"] == data.get("password"):
        session["user"] = acc["email"]
        return jsonify({"success": True})
    return jsonify({"success": False})

@app.route("/api/register", methods=["POST"])
def register():
    data = request.json
    if get_account(data.get("email")):
        return jsonify({"success": False, "message": "Account bestaat al!"})
    new_acc = {
        "email": data.get("email"),
        "wachtwoord": data.get("password"),
        "data": {"latin": [1], "french": [1]}
    }
    inlog["Accounts"].append(new_acc)
    save_inlog()
    return jsonify({"success": True})

@app.route("/api/complete_level", methods=["POST"])
def complete_level():
    data = request.json
    language = data.get("language")
    level = data.get("level")
    acc = get_account(session["user"])
    if language not in acc["data"]:
        acc["data"][language] = [1]
    if level + 1 not in acc["data"][language]:
        acc["data"][language].append(level + 1)
    save_inlog()
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)