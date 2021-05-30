from flask import render_template

from web.base import base

@base.route('/')
def index():
    return render_template('index.html')

@base.route('/about')
def about():
    return render_template('about.html')