from flask import Blueprint, render_template, request, redirect, url_for
from ..model.board import Board
from datetime import datetime

blueprint = Blueprint('board', __name__)

@blueprint.route('/')
def index():

  return render_template('board/list.html', collection=Board.objects.order_by('-date'))


@blueprint.route('/form', methods=['GET'])
def form():
  return render_template('/board/form.html')


@blueprint.route('/form', methods=['POST'])
def form_post():
  post = Board(writer=request.form['writer']
            , title=request.form['title']
            , contents=request.form['contents']
            )
  post.save()

  return redirect(url_for('board.index'))