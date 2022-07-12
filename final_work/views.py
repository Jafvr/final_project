
from flask import Flask, render_template, Blueprint, redirect, url_for


my_view = Blueprint("my_view", __name__)
@my_view.route('/')
def index():
    return render_template("index.html")

@my_view.route('/rose.html')
def rose():
    return render_template("page1.html")