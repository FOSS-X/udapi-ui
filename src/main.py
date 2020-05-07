# 
#   main.py
#   Start of UDAPI UI server
#
#   Created by FOSS-X UDAPI Desgin Team on 7/05/20.
#   Copyright © 2020 FOSS-X. All rights reserved.
#   

from flask import Flask, render_template, session, redirect, url_for
from datetime import timedelta
from auth.login import login
from auth.register import register
from home.home import home


app = Flask(__name__)
app.secret_key = "udapi"
app.permanent_session_lifetime = timedelta(minutes=1)

app.register_blueprint(home, url_prefix="/")
app.register_blueprint(login, url_prefix="/")
app.register_blueprint(register, url_prefix="/")

@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("home.homepage"))
    else:
        return redirect(url_for("login.userLogin"))

if __name__ == "__main__":
    app.run(debug=True)