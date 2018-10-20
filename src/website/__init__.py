from flask import Flask, render_template, g, session
import logging
from pymongo import MongoClient
from datetime import datetime
import json
import os

app = Flask(__name__)

mylogger = logging.getLogger("mylogger")
mylogger.setLevel(logging.INFO)

stream_hander = logging.StreamHandler()
mylogger.addHandler(stream_hander)


websitedir = os.path.dirname(__file__)
configfile = 'config.json'
configfile_path = os.path.join(websitedir, configfile)

with open(configfile_path, 'r') as f:
  config = json.load(f)

app.secret_key = config['app_secret_key']


client = MongoClient('mongodb://' + config['mongodb_host'] + ':' + config['mongodb_port'] + '/')
db = client[config['mongodb_name']]


@app.errorhandler(404)
def not_found(error):
  return render_template('404.html') ,404


@app.context_processor
def context_processor():
  return {"session":session}

from .views import home
from .views import auth
from .views import member

app.register_blueprint(home.blueprint, url_prefix='/')
app.register_blueprint(auth.blueprint, url_prefix='/auth')
app.register_blueprint(member.blueprint, url_prefix='/member')




