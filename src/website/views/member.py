from flask import Blueprint, render_template, request, redirect, g
from .. import db

blueprint = Blueprint('member', __name__)

@blueprint.route('/')
def index():
  # To do
  members = db.members.find()


  return render_template('member/list.html', members = members)


