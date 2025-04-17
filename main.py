"""
Skylog backend - main.py

Entry point
"""

import flask

app = flask.Flask("Skylog_API")

@app.route("/")
def index():
    return "Skylog API is running!"

if __name__ == "__main__":
    app.run(debug=True)
