from flask import Flask, render_template,request,redirect
from indeed import get_jobs as indeed_get_jobs
from so import get_jobs as so_get_jobs

app = Flask("Super Scrapper")

db = {}

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
def report():
  search = request.args.get('search')
  if search:
    search = search.lower()
    fromDb = db.get(search)
    if fromDb:
      indeed_jobs = fromDb
    else:
      indeed_jobs = indeed_get_jobs(search)
      db[search] = indeed_jobs
    
  else:
    return redirect("/")
  return render_template("report.html", word=search, resultsNumber = len(indeed_jobs), results = indeed_jobs)

app.run(host="0.0.0.0")