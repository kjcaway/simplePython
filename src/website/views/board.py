from flask import Blueprint, render_template, request, redirect

blueprint = Blueprint('board', __name__)

@blueprint.route('/')
def index():
  return render_template('board/list.html')

