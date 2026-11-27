from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.get("/")
def landing():
    return render_template("index.html")

@app.post("/simulate")
def simulate():
    return redirect(url_for("result"))

@app.get("/result")
def result():
    return render_template("result.html")

@app.get("/continue")
def utk_public_link():
    return redirect("https://www.utk.edu/", code=302)

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        ssl_context=("certs/localhost.pem", "certs/localhost-key.pem"),
    )
