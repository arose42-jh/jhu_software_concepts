"""
Flask web application for displaying applicant statistics.

This app uses a route to display statistics queried from the database and renders them.

Routes:
    / : Displays all applicant statistics using the 'index.html' template.

Usage:
    Run this file directly to start the Flask development server.
"""

from flask import Flask, render_template
from query_data import get_all_statistics

# Create a Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """
    Home page route.

    Queries all  statistics from the database and renders them using the 'index.html' template.

    Returns:
        str: Rendered HTML page with applicant statistics.
    """
    db_results = get_all_statistics()
    return render_template('index.html', results=db_results)


# Run the application
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)
