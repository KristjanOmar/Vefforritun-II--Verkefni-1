from flask import Flask

app = Flask(__name__)

@app.route('/')
def nafn():
    return "<h1>Verkefni 1</h1> <br> nafnið þitt"
