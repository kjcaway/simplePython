from flask import Flask, render_template, g
import logging
from pymongo import MongoClient

app = Flask(__name__)

mylogger = logging.getLogger("mylogger")
mylogger.setLevel(logging.INFO)

stream_hander = logging.StreamHandler()
mylogger.addHandler(stream_hander)


client = MongoClient('mongodb://192.168.0.2:27017/')
db = client.test


@app.errorhandler(404)
def not_found(error):
  return render_template('404.html') ,404

@app.before_request
def before_request():
  g.db = db

@app.teardown_request
def teardown_request(exception):
  if hasattr(g, 'db'):
    pass

from .views import home
from .views import auth
from .views import member

app.register_blueprint(home.blueprint, url_prefix='/')
app.register_blueprint(auth.blueprint, url_prefix='/auth')
app.register_blueprint(member.blueprint, url_prefix='/member')





