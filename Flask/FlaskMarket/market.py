from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
def market_page():
    return render_template("market.html", item_name="Phone")

if __name__ == "__main__":
    app.run(debug=True, port=5001)

