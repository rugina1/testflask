from app import app
from flask import url_for,render_template,redirect

@app.route('/')
def index():
    return render_template('index.html')

