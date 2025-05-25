#Import necessary modules
from flask import Flask, render_template
from pages import pages

# Create a Flask application
def create_app():
    app = Flask(__name__)
    # Call the pages blueprint
    app.register_blueprint(pages.bp)

    return app

# Run the application
if __name__ == "__main__":
    app = create_app()
    app.run(host = '0.0.0.0', port = 8080)