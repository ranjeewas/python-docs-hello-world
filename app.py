from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, RanjeewaSen-This is MASTER!"
