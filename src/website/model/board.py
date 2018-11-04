from mongoengine import *
from datetime import datetime
from .. import config

connect('connect1', host='mongodb://' + config['mongodb_host'] + ':' + config['mongodb_port'] + '/' + config['mongodb_name'])

class Board(Document):
    title = StringField(required=True, max_length=200)
    contents = StringField(required=True, max_length=3000)
    writer = StringField(required=True, max_length=100)
    date = DateTimeField(default=datetime.utcnow)
    tags = ListField(StringField(max_length=50))
    meta = {'allow_inheritance': True}
