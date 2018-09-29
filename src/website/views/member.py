from flask import Blueprint, render_template, request, redirect, g

# from .. import database

blueprint = Blueprint('member', __name__)

@blueprint.route('/')
def index():
  # To do
  db = getattr(g, 'db', None)
  members = db.members.find()

  return render_template('member/list.html', members = members)


