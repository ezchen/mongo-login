import login
from flask import Flask, render_template, request, redirect, url_for
from pymongo import Connection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['un']
        password = request.form['pw']
        login.addUser(username, password)
        return render_template("login.html")
    return render_template("login.html")

if __name__=='__main__':
    app.run(debug=True)
