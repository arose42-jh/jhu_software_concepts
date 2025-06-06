from flask import Flask, render_template
from query import get_all_statistics

# Create a Flask application
app = Flask(__name__)
    # Call the pages blueprint
@app.route('/')


def index():
    db_results = get_all_statistics()
    return render_template('index.html', results=db_results)


# Run the application
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)