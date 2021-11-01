"""
Routes and views for the flask application.
"""
from flask import Flask
from datetime import datetime
from flask import render_template
app = Flask(__name__)
title = 'M.B. Farms'


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title=title,
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About M.B. Farms',
        year=datetime.now().year,
    )
