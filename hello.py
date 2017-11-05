from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('Mainlogin.html')
