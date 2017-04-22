from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2.types import Geometry
from stringAnalyzer.analyzer import theAnalyzer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://copunhackers:hack@localhost/copunhackersDB'
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Name %r>' % self.name

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    creation_time = db.Column(db.BigInteger)
    expiry_time = db.Column(db.BigInteger)
    content_type = db.Column(db.Text)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer)
    location = db.Column(Geometry(geometry_type='POINT', srid=4326))

# Set "homepage" to index.html
@app.route('/')
def index():
    return 'Hello world'

@app.route('/drop', methods=['POST'])
def dropMessage():
    obj = request.json
    (msg, allowed) = theAnalyzer(obj["content"])
    if allowed:
        print('Add to database')
    #  db.session.add()
    #  db.session.commit()
    return '("{}",{})'.format(msg, allowed)

# Save e-mail to database and send to success page@app.route('/test', methods=['GET'])
def prereg():
    name = None
    if request.method == 'GET':
        name = request.args['name']
        if not db.session.query(User).filter(User.name == name).count():
            reg = User(name)
            db.session.add(reg)
            db.session.commit()
            return ('Success: ' + str(reg))
    return 'Failure'

if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0')
