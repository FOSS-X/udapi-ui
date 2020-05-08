# 
#   login.py
#   User login page
#
#   Created by FOSS-X UDAPI Desgin Team on 7/05/20.
#   Copyright © 2020 FOSS-X. All rights reserved.
#   

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import requests

register = Blueprint("register", __name__, static_folder="static", template_folder="templates")

@register.route("/register", methods=('GET', 'POST'))
def userRegister():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']

        if password != password2:
            flash("Password did not match.", 'error')
            return redirect(url_for("register.userRegister"))

        if username == '' or password2 == '':
            flash("Please fill in the details.", 'error')
            return redirect(url_for("register.userRegister"))

        url = "http://localhost:8080/udapi/v1/auth/signup"
        payload = "{{\n    \"userName\": \"{}\",\n    \"password\": \"{}\",\n    \"type\": 1\n}}".format(username, password)
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data = payload)
        msg = response.json()

        # return f'{msg}'
        try: 
            if msg["userName"]:
                flash("Registerd Successfully!", "info")
                return redirect(url_for("login.userLogin"))     # signed up sucessfully
        except:
            flash("User Already exists!", "warning")
            return redirect(url_for("register.userRegister"))       # user already exists

    else:
        return render_template("register.html")

