from flask import Blueprint, render_template, request, redirect, url_for, current_app
from ..model.board import Board
from datetime import datetime
from werkzeug import secure_filename
import os
from .. import mylogger
import cuid
import json
import base64

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
  board = Board.objects.order_by('-date')
  mapper = {}
  for one in board:
    if one.attached.filename :
      with open(os.path.join(current_app.config['upload_file_path'], one.attached.filename_cuid + '.' + one.attached.file_ext)) as image_file:
        encoded_string = base64.b64encode(image_file.read())
      mapper[one.attached.filename_cuid]= encoded_string
  
  return render_template('board/list.html', collection=board, mapper=mapper)


@blueprint.route('/form', methods=['GET'])
def form():
  return render_template('/board/form.html')


@blueprint.route('/form', methods=['POST'])
def form_post():
  file = None
  if request.files:
    file = request.files['file1']
  
  attached = {}

  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    filename_cuid = cuid.cuid()
    file_ext = filename.rsplit('.', 1)[1]

    mylogger.info('uploaded file name : ' + filename)
    mylogger.info('uploaded file name cuid : ' + filename_cuid)
    mylogger.info('uploaded file path : ' + current_app.config['upload_file_path'])

    make_dir(current_app.config['upload_file_path'])

    file.save(os.path.join(current_app.config['upload_file_path'], filename_cuid + '.' + file_ext))

    attached['filename'] = filename
    attached['filename_cuid'] = filename_cuid
    attached['file_ext'] = file_ext


  if request.form['writer'] is not None:
    post = Board(writer=request.form['writer']
                , title=request.form['title']
                , contents=request.form['contents']
                , attached = attached
                )
    post.save()

  return redirect(url_for('board.index'))

