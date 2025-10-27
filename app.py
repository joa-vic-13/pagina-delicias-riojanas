from flask import Flask, render_template, url_for
from products import products
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
