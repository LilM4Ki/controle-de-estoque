from flask import render_template, Blueprint

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template("index.html")