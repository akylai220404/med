from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recomendations")
@app.route('/recomendations/<string:man>')
def recomendations(man=""):
    return render_template("recomendations.html", man=man)

@app.route("/all")
def all():
    return render_template("all.html")