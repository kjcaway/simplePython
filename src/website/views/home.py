from flask import Blueprint, render_template, request, redirect

blueprint = Blueprint('home', __name__)
nav = 'home'
loc = 'Home'

@blueprint.route('/')
def index():

  return render_template('home/home.html', nav=nav, loc=loc)

@blueprint.route('/about/')
def about():
  nav = 'about'
  loc = 'About'

  return render_template('home/about.html', nav=nav, loc=loc)
