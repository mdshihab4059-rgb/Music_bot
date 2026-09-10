from flask import Flask
import os
import subprocess
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Shihab X Music Bot is running!"

def start_bot():
    subprocess.run(["python3", "-m", "ShrutiMusic"])

if __name__ == "__main__":
    threading.Thread(target=start_bot, daemon=True).start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)