from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
import pandas as pd
import io
import datapull

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session handling

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        code = request.form.get('access_code')
        if code == 'karan1234':  # Your passcode
            session['authenticated'] = True
            return redirect(url_for('dashboard'))
        return render_template("login.html", error="Invalid access code")
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template("index.html")

@app.route('/teachers/All')
def all_teachers():
    return jsonify(datapull.getdata("teachers"))

@app.route('/colleges/All')
def all_colleges():
    return jsonify(datapull.getdata("colleges"))

@app.route('/zones/All')
def all_colleges_zones():
    return jsonify(datapull.getdata("zones"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/teachers')
def teachers():
    return render_template("teachers.html")

@app.route('/colleges')
def collegs():
    return render_template("colleges.html")

@app.route('/zones')
def zones():
    return render_template("zones.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
