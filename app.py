from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><P style='font-size:7px;text-align:center'>If you can read me you are too close to the screen!</P></html>"
