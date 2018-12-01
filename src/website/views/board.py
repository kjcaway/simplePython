from flask import Blueprint, render_template, request, redirect, url_for, current_app
from ..model.board import Board
from datetime import datetime
from werkzeug import secure_filename
import os
from .. import mylogger

blueprint = Blueprint('board', __name__)

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1] in current_app.config['allow_extensions']


def make_dir(path):
  if os.path.exists(path) is False:
    try:
        mylogger.info('make dir : ' + path)
        original_umask = os.umask(0)
        os.makedirs(path, 0777)
    finally:
        os.umask(original_umask)

  return True


@blueprint.route('/')
def index():
  return render_template('board/list.html', collection=Board.objects.order_by('-date'))


@blueprint.route('/form', methods=['GET'])
def form():
  return render_template('/board/form.html')


@blueprint.route('/form', methods=['POST'])
def form_post():
  file = request.files['file1']
  if file and allowed_file(file.filename):
    mylogger.info('file is allowed!')
    filename = secure_filename(file.filename)
    mylogger.info('uploaded file name : ' + filename)
    mylogger.info('uploaded file path : ' + current_app.config['upload_file_path'])
    make_dir(current_app.config['upload_file_path'])
    file.save(os.path.join(current_app.config['upload_file_path'], filename))

  if request.form['writer'] is not None:
    post = Board(writer=request.form['writer']
                , title=request.form['title']
                , contents=request.form['contents']
                )
    post.save()

  return redirect(url_for('board.index'))