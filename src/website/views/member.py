from flask import Blueprint, render_template, request, redirect, g
from .. import db
from .. import mylogger
import json

blueprint = Blueprint('member', __name__)

@blueprint.route('/')
def index():
  # To do
  members = db.members.find()
  
  return render_template('member/list.html', members = members)

@blueprint.route('/<userid>', methods = ['DELETE'])
def remove(userid):
  # To do
  mylogger.info(userid + ' is deleted')

  result = {
    "status" : "success"
  }

  try:
    db.members.delete_one({"userid":userid})
  except Exception as e:
    mylogger.error(e)
    result['status'] = 'fail'

  return json.dumps(result)


