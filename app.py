from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return "<center><h1>Hello</h1></center>"


