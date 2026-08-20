from flask import Flask

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    return "Press 1 for Music, press 2 for sports and press 3 for movies."

@app.route("/", methods=["GET"])
def home():
    return "Webhook is working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
