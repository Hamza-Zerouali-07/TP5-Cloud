from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return f"message changé\n"

@app.route("/healthx")
def health():
    return "ok\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
