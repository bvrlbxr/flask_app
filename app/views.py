from app import app
from flask import render_template
from .constants import *

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'User' } # выдуманный пользователь
    return render_template("index.html",
        title = 'Home',
        user = user)

@app.route("/counter")
def counter():
    global visit_counts
    visit_counts += 1
    return render_template("counter.html",
                    title='Total Users',
                    count=visit_counts)