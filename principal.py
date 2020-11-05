from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/detalhe")
def detalhe():
    return render_template("detalhe.html")

app.run(debug=True)