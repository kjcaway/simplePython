from flask import Blueprint, render_template, request, redirect

blueprint = Blueprint('auth', __name__)

@blueprint.route('/signin')
def signin():
  return render_template('auth/signin.html')

@blueprint.route('/signup')
def signup():
  return render_template('auth/signup.html')

