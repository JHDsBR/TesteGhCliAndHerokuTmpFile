from flask import Flask

app = Flask(__name__)

@app.route("/")
def Home():
    return "Está no ar"
