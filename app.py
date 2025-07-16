from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from your CI/CD Flask app!"

@app.route("/hello")
def hello():
    return "Hi from /hello"
