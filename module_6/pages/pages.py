"""
Defines the Flask blueprint and routes for the main pages of the module_6 web application.

Includes routes for the home, projects, and contact pages, rendering their respective templates.
"""

#Import necessary modules
from flask import Blueprint, render_template

#Create a blueprint for each page
bp = Blueprint("pages", __name__,template_folder="templates", static_folder="static")
#Define routes for the pages
@bp.route("/")
def home():
    """
    Render the home page.

    Returns:
        str: Rendered HTML for the base (home) page.
    """
    return render_template("base.html")

@bp.route("/projects")
def projects():
    """
    Render the projects page.

    Returns:
        str: Rendered HTML for the projects page.
    """
    return render_template("projects.html")

@bp.route("/contact")
def contact():
    """
    Render the contact page.

    Returns:
        str: Rendered HTML for the contact page.
    """
    return render_template("contact.html")
