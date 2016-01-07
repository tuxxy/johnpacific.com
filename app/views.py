from app import app
from flask import render_template, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
