import webview
from flask import Flask

print("************BEFORE IMPORT********")
from app.main import app
print("************after IMPORT********")
print("************BEFORE FLASK********")
app = Flask(__name__)
print("************after FLASK********")


from contextlib import redirect_stdout
from io import StringIO
from server import server

@app.route("/")
def home_view():
    return "<h1>Welcome to Geeks for Geeks</h1>"

if __name__ == "__main__":
    # app.run()
    stream = StringIO()
    with redirect_stdout(stream):
        window = webview.create_window('My first pywebview application', server)
        print('WINDOW IS CREATED')
        webview.start(debug=True)
