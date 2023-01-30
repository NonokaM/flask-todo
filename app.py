from flask import Flask, request, render_template
import codecs

app = Flask(__name__)

@app.route("/")
def top():
    message = "test_message = OK"

    return render_template("mainpage.html", message = message)

