from flask import Flask, render_template

import subprocess
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello</p>"

@app.route("/script")
def script():
    return render_template ("script.html")