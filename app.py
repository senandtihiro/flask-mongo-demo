from flask import Flask
from flask_mongoengine import MongoEngine
from flask import render_template


app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {
    'db': 'prompt',
    'host': '127.0.0.1',
    'port': 27017
}

db = MongoEngine(app)


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


@app.route('/')
def index():
    prompt_list = Prompt.objects.all()
    print('23333333333333333333333', prompt_list)
    for p in prompt_list:
        print('debug t.title:', p.title)
    return render_template('prompts.html', prompts=prompt_list)




if __name__ == '__main__':
    app.run(debug=True)