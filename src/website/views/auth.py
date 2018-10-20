from flask import Blueprint, render_template
from flask import request, redirect, flash, session, g
from .. import db

blueprint = Blueprint('auth', __name__)

@blueprint.route('/signin', methods=['GET'])
def signin():
  return render_template('auth/signin.html')

@blueprint.route('/signin', methods=['POST'])
def signin_post():

  if db is not None:
    user = db.members.find_one({'userid':request.form['userid']})
    if user is None:
      error = 'invalid userid'
      flash('Invalid userid!')
      return render_template('auth/signin.html', error=error )

    elif user['password'] != request.form['passwd']:
      error = 'invalid password'
      flash('Invalid password')
      return render_template('auth/signin.html', error=error)

    else:
        session['userid'] = user['userid']
        flash('You were logged in')
        return redirect('/')  


@blueprint.route('/signup')
def signup():
  return render_template('auth/signup.html')

@blueprint.route('/logout')
def logout():
    session.pop('userid', None)
    flash('You were logged out')
    return redirect('/')
