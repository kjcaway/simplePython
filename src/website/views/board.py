from flask import Blueprint, render_template, request, redirect
from ..model.board import Board

blueprint = Blueprint('board', __name__)

@blueprint.route('/')
def index():

  for board in Board.objects:
    print board
  
  return render_template('board/list.html')

