
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello, Welcome to Modern Softwar Concepts in Python!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
# To run the application, use the command: python main.py