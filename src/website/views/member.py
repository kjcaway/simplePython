from flask import Blueprint, render_template, request, redirect

# from .. import database

blueprint = Blueprint('member', __name__)

@blueprint.route('/')
def index():
  # To do
  
  return render_template('member/list.html')


