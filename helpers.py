from nba_api.stats.static import teams
from flask import request, render_template

# def lookup():
#     response = teams.find_teams_by_state(request.form.args("inputstate"))
#     # hometeam = response.json()
#     return {
#         "name": response["full_name"],
#         "city": response["city"],
#         "yrfounded": response["year_founded"]
#     }

# @app.route("/lookup", methods=["GET", "POST"])
# def hi():
#     """Get home team."""
#     if request.method == "POST":
#         teamz = lookup()
#         #hometeam = teamz.json()
#         if not teamz:
#             return render_template("please.html", team=teamz)
#         else:
#             # Goes after lookedup.html(name=hometeam["full_name"], city=hometeam["city"], yrfounded=hometeam["year_founded"])
#             return render_template("please.html",team=teamz)
#     else:
#         return render_template('lookup.html')

def teaminfo(team):
        hometeam = teams.find_teams_by_city(team)
        return render_template("kings.html", city = hometeam[0]["city"], state = hometeam[0]["state"], year = hometeam[0]["year_founded"])