"""
Application stub
"""

from flask import Flask

app = Flask(__name__)


def initialize():
    # perform heavy stuff here
    return True


def do_stuff():
    # do whatever you need to do
    response = "This is response from Python backend"
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0")
