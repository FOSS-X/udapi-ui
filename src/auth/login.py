# 
#   login.py
#   User login page
#
#   Created by FOSS-X UDAPI Desgin Team on 7/05/20.
#   Copyright © 2020 FOSS-X. All rights reserved.
#   

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import requests

login = Blueprint("login", __name__, static_folder="static", template_folder="templates")

@login.route("/login", methods=('GET', 'POST'))
def userLogin():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        session["username"] = username

        url = "http://localhost:8080/udapi/v1/auth/login"
        payload = "{{\n    \"userName\": \"{}\",\n    \"password\": \"{}\",\n    \"type\": 1\n}}".format(username, password)
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data = payload)
        msg = response.json()

        try:
            if msg['token']:
                session['jwt'] = msg['token']
                flash("Logged in Successfully!", "info")
                return redirect(url_for("index"))
        except:
            flash("Invalid Credentials.", "warning")
            return render_template("login.html")

    else:
        return render_template("login.html")

