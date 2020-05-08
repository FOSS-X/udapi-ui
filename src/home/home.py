# 
#   home.py
#   Home page
#
#   Created by FOSS-X UDAPI Desgin Team on 7/05/20.
#   Copyright © 2020 FOSS-X. All rights reserved.
#   

from flask import Blueprint, render_template, request, redirect, url_for, session, flash

home = Blueprint("home", __name__, static_folder="static", template_folder="templates")

@home.route("/home")
def homepage():
    try:
        username = session["username"]
        return render_template("home.html", username=username)
    except:
        return redirect(url_for('index'))

@home.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("jwt", None)
    flash("Logged out Successfully", 'info')
    return redirect(url_for("index"))