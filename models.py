
import datetime
from flask_mongoengine import MongoEngine

db = MongoEngine()

class DataType(db.EmbeddedDocument):
    light = db.ListField()
    standard = db.ListField()


class Prompt(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(max_length=50)
    type = db.IntField(max_length=50)
    play_beep = db.BooleanField()
    can_omit = db.BooleanField()
    show_hmi = db.BooleanField()
    barge_in = db.BooleanField()
    data = db.EmbeddedDocumentField(DataType)
    simple_data = db.EmbeddedDocumentField(DataType)
    replace = db.DictField()