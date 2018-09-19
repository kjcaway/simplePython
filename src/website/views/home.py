from flask import Blueprint, render_template, request, redirect

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def index():
  return render_template('home/home.html')
