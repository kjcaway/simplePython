from flask import Blueprint, render_template, request, redirect, g

blueprint = Blueprint('member', __name__)
nav = 'admin'
loc = 'Admin'

@blueprint.route('/')
def index():
  # To do
  db = getattr(g, 'db', None)
  members = db.members.find()


  return render_template('member/list.html', members = members, nav = nav, loc=loc + ' > ' + 'Members List')


