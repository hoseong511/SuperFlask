from flask import Flask, render_template

app = Flask("Super Scrapper")

@app.route("/")
def home():
  return "Hello! welcome to super page!!"

# github도 마찬가지 https://github.com/hoseong511 하면 hoseong511 repository로 접속되는 거에 대한 원리임!
@app.route("/<username>")
def potato(username):
  return f"Hello {username} how are you doing"

@app.route("/contact")
def contact():
  return "contact me!"

@app.route("/potato")
def potato2():
  return render_template("main.html")

@app.route("/report")

app.run(host="0.0.0.0")