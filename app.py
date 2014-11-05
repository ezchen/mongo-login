import login
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import Connection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['un']
        password = request.form['pw']
        login.addUser(username, password)
        return redirect('/u/'+username)
    return render_template("login.html")

@app.route('/u/<username>', methods=['GET', 'POST'])
def user(username=None):
    if request.method == 'POST':
        if request.form['logout'] == 'Logout':
            login.logout(username)
            return redirect(url_for('home'))
    if login.authenticated(username)== True:
        return render_template("user.html", username=username)
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)
