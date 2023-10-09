from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/2")
def home2():
    return render_template("index-m.html")

if __name__ == "__main__":
    app.run(debug=True)