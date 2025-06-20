"""
Entry point for the Flask web application in module_6.

- Initializes the Flask app and registers the pages blueprint.
- Runs the server on host 0.0.0.0 and port 8080 when executed directly.
"""

#Import necessary modules
from flask import Flask
from pages import pages

# Create a Flask application
def create_app():
    """
    Create and configure the Flask application.

    Registers the 'pages' blueprint and returns the Flask app instance.
    
    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    # Call the pages blueprint
    app.register_blueprint(pages.bp)

    return app

# Run the application
if __name__ == "__main__":
    site = create_app()
    site.run(host = '0.0.0.0', port = 8080)
