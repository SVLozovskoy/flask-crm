from app import app
from flask import Flask,request,render_template,url_for, redirect
from app import db


@app.route('/', methods=['POST', 'get'])
def index():
    if request.method == 'POST':
        lname = request.form['search']
        return redirect(url_for('customers.searsh' ,lname=lname))
    else:
        return render_template('index.html')
