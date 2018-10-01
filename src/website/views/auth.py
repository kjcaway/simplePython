from flask import Blueprint, render_template, request, redirect

blueprint = Blueprint('auth', __name__)

loc = 'Sign In'

@blueprint.route('/signin')
def signin():
  return render_template('auth/signin.html', loc=loc)

@blueprint.route('/signup')
def signup():
  loc = 'Sign Up'

  return render_template('auth/signup.html', loc=loc)

