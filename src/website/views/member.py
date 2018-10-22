from flask import Blueprint, render_template, request, redirect, g
from .. import db
from .. import mylogger
import json
from pymongo import ReturnDocument

blueprint = Blueprint('member', __name__)

@blueprint.route('/')
def index():
  members = db.members.find()
  
  return render_template('member/list.html', members = members)

@blueprint.route('/<userid>', methods = ['GET'])
def getMember(userid):
  member = {
    'userid': '',
    'username' : '',
  }

  try:
    ret = db.members.find_one({"userid":userid})

    member['userid'] = ret['userid']
    member['username'] = ret['username']
  except Exception as e:
    mylogger.error(e)
  
  return json.dumps(member)


@blueprint.route('/modify', methods = ['POST'])
def modifyMember():
  result = {
    'status': 'success'
  }
  try:
    ret = db.members.find_one_and_update({"userid":request.form['userid']}, 
      {'$set' : {"username":request.form['username']}
      }, return_document=ReturnDocument.AFTER)

  except Exception as e:
    mylogger.error(e)
    result['status'] = 'fail'
  
  members = db.members.find()

  return render_template('member/list.html', members = members)


@blueprint.route('/<userid>', methods = ['DELETE'])
def remove(userid):
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


