from flask import Blueprint, render_template, request, redirect

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def index():
  return render_template('home/home.html')


@blueprint.route('about')
def about():
  return render_template('home/about.html')