"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the index page."""
    return render_template(
        'home.html',
        title='中山國際轉運',
        year=datetime.now().year,
    )

@app.route('/tutorial')
def tutorial():
    """Renders the tutorial page."""
    return render_template(
        'tutorial.html',
        title='代運使用教學',
        year=datetime.now().year,
    )

@app.route('/ServiceContent')
def ServiceContent():
    """Renders the about page."""
    return render_template(
        'ServiceContent.html',
        title='服務內容',
        year=datetime.now().year,
        message='test page.'
    )

@app.route('/shopping')
def shopping():
    """Renders the contact page."""
    return render_template(
        'shopping.html',
        title='購物情報',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='關於我們',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/user')
def user():
    """Renders the about page."""
    return render_template(
        'user.html',
        title='成為會員 / 登入',
        year=datetime.now().year,
        message='立即登入或註冊成為會員，開始使用 中山國際轉運 服務！'
    )