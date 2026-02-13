import os
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "project": "KAIxGenMusic",
        "message": "Telegram Music Bot is Alive 🎵",
        "time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    })

@app.route("/health")
def health():
    return jsonify({"health": "ok"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
