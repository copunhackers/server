from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://teal.basilehenry.com/copunhacksDB'
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Name %r>' % self.name

# Set "homepage" to index.html
@app.route('/')
def index():
    return "Hello world"

# Save e-mail to database and send to success page
@app.route('/test', methods=['GET'])
def prereg():
    name = None
    if request.method == 'GET':
        name = request.args['name']
        if not db.session.query(User).filter(User.name == name).count():
            reg = User(name)
            db.session.add(reg)
            db.session.commit()
            return ('Success: ' + reg)
    return 'Failure'

if __name__ == '__main__':
    app.debug = True
    app.run()
