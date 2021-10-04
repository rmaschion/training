import logging
import webview
from flask import Flask

from contextlib import redirect_stdout
from io import StringIO
from server import server

app = Flask(__name__)

logger = logging.getLogger(__name__)
stream = StringIO()
with redirect_stdout(stream):
    window = webview.create_window('My first pywebview application', server)
    print('WINDOW IS CREATED')
    webview.start(debug=True)

def initialize():
    # perform heavy stuff here
    return True


def do_stuff():
    # do whatever you need to do
    response = "This is response from Python backend"
    return response

# @app.route("/")
# def home_view():
#     return "<h1>Welcome to Geeks for Geeks</h1>"

# if __name__ == '__main__':
#     pass
    # stream = StringIO()
    # with redirect_stdout(stream):
    #     window = webview.create_window('My first pywebview application', server)
    #     print('WINDOW IS CREATED')
    #     webview.start(debug=True)
