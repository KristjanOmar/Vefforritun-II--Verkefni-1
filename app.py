from flask import Flask

app = Flask(__name__)

@app.route('/')
def nafn():
    return "nafnið þitt"
