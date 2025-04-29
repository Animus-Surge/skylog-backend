"""
Skylog backend - main.py

Entry point
"""

import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask("Skylog_API")

# Routes

@app.route("/")
def index():
    return "Skylog API is running!"



if __name__ == "__main__":
    app.run(debug=True)
