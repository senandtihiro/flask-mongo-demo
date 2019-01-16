import os
import sys
import flask

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../../')))


app = flask.Flask(__name__)
app.config.from_object(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'prompt'}
app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'flask+mongoengine=<3'
app.debug = True


from models import db
db.init_app(app)


from views import index
app.add_url_rule('/', view_func=index)
# app.add_url_rule('/pagination', view_func=pagination)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
