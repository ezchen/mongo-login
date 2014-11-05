import login
from flask import Flask, render_template,request, redirect, url_for
from pymongo import Connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

if __name__=='__main__':
    app.run(debug=True)
