#Import necessary modules
from flask import Blueprint, render_template

#Create a blueprint for each page
bp = Blueprint("pages", __name__,template_folder="templates", static_folder="static")
#Define routes for the pages
@bp.route("/")
def home():
    return render_template("base.html")

@bp.route("/projects")
def projects():
    return render_template("projects.html")

@bp.route("/contact")
def contact():
    return render_template("contact.html")