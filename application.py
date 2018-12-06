import os

from flask import Flask, render_template, request
from nba_api.stats.static import teams

app = Flask(__name__)

# Ensures responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

allteams = teams.get_teams()

@app.route("/")
def welcome():
    return render_template("welcome.html", allteams = allteams)

@app.route("/ATL")
def hawks():
    hometeam = teams.find_teams_by_city("atlanta")
    return render_template("hawks.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/BOS")
def boston():
    hometeam = teams.find_teams_by_city("boston")
    return render_template("celtics.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/CLE")
def cavs():
    hometeam = teams.find_teams_by_city("cleveland")
    return render_template("cavaliers.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/NOP")
def nop():
    hometeam = teams.find_teams_by_city("new orleans")
    return render_template("pelicans.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/CHI")
def chi():
    hometeam = teams.find_teams_by_city("chicago")
    return render_template("bulls.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/DAL")
def dal():
    hometeam = teams.find_teams_by_city("dallas")
    return render_template("mavericks.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/DEN")
def den():
    hometeam = teams.find_teams_by_city("denver")
    return render_template("nuggets.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/GSW")
def gsw():
    hometeam = teams.find_teams_by_city("Golden state")
    return render_template("kings.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/HOU")
def hou():
    hometeam = teams.find_teams_by_city("houston")
    return render_template("rockets.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/LAC")
def lac():
    hometeam = teams.find_teams_by_city("los angeles")
    return render_template("clippers.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/LAL")
def lal():
    hometeam = teams.find_teams_by_city("los angeles")
    return render_template("lakers.html", name = hometeam[1]["full_name"], city = hometeam[1]["city"], state = hometeam[1]["state"], year = hometeam[1]["year_founded"])

@app.route("/MIA")
def mia():
    hometeam = teams.find_teams_by_city("miami")
    return render_template("heat.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/MIL")
def mil():
    hometeam = teams.find_teams_by_city("milwaukee")
    return render_template("bucks.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/MIN")
def twolves():
    hometeam = teams.find_teams_by_city("minnesota")
    return render_template("timberwolves.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/BKN")
def bkn():
    hometeam = teams.find_teams_by_city("brooklyn")
    return render_template("nets.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/NYK")
def nyk():
    hometeam = teams.find_teams_by_city("new york")
    return render_template("knicks.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/ORL")
def orl():
    hometeam = teams.find_teams_by_city("orlando")
    return render_template("magic.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/IND")
def ind():
    hometeam = teams.find_teams_by_city("indiana")
    return render_template("pacers.html", name = hometeam[0]["full_name"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/PHI")
def phi():
    hometeam = teams.find_teams_by_city("philadelphia")
    return render_template("76ers.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/PHX")
def phx():
    hometeam = teams.find_teams_by_city("phoenix")
    return render_template("suns.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/POR")
def por():
    hometeam = teams.find_teams_by_city("portland")
    return render_template("trailblazers.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/SAC")
def kings():
    hometeam = teams.find_teams_by_city("sacramento")
    return render_template("kings.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/SAS")
def sas():
    hometeam = teams.find_teams_by_city("san antonio")
    return render_template("spurs.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/OKC")
def okc():
    hometeam = teams.find_teams_by_city("oklahoma city")
    return render_template("thunder.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/TOR")
def tor():
    hometeam = teams.find_teams_by_city("toronto")
    return render_template("raptors.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/UTA")
def uta():
    hometeam = teams.find_teams_by_city("utah")
    return render_template("jazz.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/MEM")
def mem():
    hometeam = teams.find_teams_by_city("memphis")
    return render_template("grizzlies.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/WAS")
def was():
    hometeam = teams.find_teams_by_city("washington")
    return render_template("wizards.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/DET")
def det():
    hometeam = teams.find_teams_by_city("detroit")
    return render_template("pistons.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])

@app.route("/CHA")
def cha():
    hometeam = teams.find_teams_by_city("charlotte")
    return render_template("hornets.html", name = hometeam[0]["full_name"], city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])