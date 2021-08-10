# ------------------------------------------------
# Program by Victoria Baktov
#
#
# Version      Date           Info
# 1.0          10-Aug-2021    Initial Version
#
# ----------------------------------------------
from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def root():
    return render_template("index.html")

@application.route("/help")
def helppage():
    return render_template("help.html")

@application.route("/hello")
def index():
    return "Hello World from vikiFlask Hello Page.<b> v1.0"

#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.run()
#------------------------------
