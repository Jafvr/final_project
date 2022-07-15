
from flask import Flask, render_template, Blueprint, redirect, url_for



my_view = Blueprint("my_view", __name__)
@my_view.route('/index')
def index():
    return render_template("index.html")

@my_view.route('/')
def homepage():
    return render_template("index.html")

@my_view.route('/javascript')
@my_view.route('/js')
@my_view.route('/home')
def index_redirect():
    return redirect(url_for("my_view.index"))

@my_view.route('/yusuf')
def yusuf():
    return render_template("yusuf.html")

@my_view.route('/rose')
def rose():
    return render_template("rose.html")

@my_view.route('/zak')
def zak():
    return render_template("zak.html")

@my_view.route('/contact')
def contact():
    return render_template("contact.html")

@my_view.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

# @my_view.route('/index.html')
# def index():
#     return render_template("index.html")