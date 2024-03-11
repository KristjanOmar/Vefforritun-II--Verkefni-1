from flask import Flask

app = Flask(__name__)

@app.route('/')
def hallo_heimur():
    return "halló heimur"
