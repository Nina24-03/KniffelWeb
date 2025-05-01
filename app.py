from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

KATEGORIEN = [
    "Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser",
    "Bonus", "Dreierpasch", "Viererpasch", "Full House",
    "Kleine Straße", "Große Straße", "Kniffel", "Chance"
]

spieler_punkte = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        namen = [n.strip() for n in request.form["spieler"].split(",") if n.strip()]
        for name in namen:
            spieler_punkte[name] = {k: "" for k in KATEGORIEN}
        return redirect(url_for("spiel"))
    return render_template("index.html")

@app.route("/spiel", methods=["GET", "POST"])
def spiel():
    if request.method == "POST":
        for spieler, kategorien in spieler_punkte.items():
            for kategorie in KATEGORIEN:
                eingabe = request.form.get(f"{spieler}_{kategorie}")
                spieler_punkte[spieler][kategorie] = eingabe
    return render_template("spiel.html", spieler_punkte=spieler_punkte, kategorien=KATEGORIEN)

@app.route("/reset")
def reset():
    for spieler in spieler_punkte:
        spieler_punkte[spieler] = {k: "" for k in KATEGORIEN}
    return redirect(url_for("spiel"))

if __name__ == "__main__":
    app.run(debug=True)