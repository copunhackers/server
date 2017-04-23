from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from stringAnalyzer.analyzer import theAnalyzer
from sqlalchemy import func
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://copunhackers:hack@localhost/copunhackersDB"
db = SQLAlchemy(app)

class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    creation_time = db.Column(db.BigInteger)
    expiry_time = db.Column(db.BigInteger)
    content_type = db.Column(db.Text)
    content = db.Column(db.Text)
    username = db.Column(db.Text)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    
    def __init__(self, creation_time, expiry_time, content_type, content, username, lat, lng):
        self.creation_time = creation_time
        self.expiry_time = expiry_time
        self.content_type = content_type
        self.username = username
        self.lat = lat
        self.lng = lng

    def create_json(self):
        obj = {}
        obj["creationTime"] = self.creation_time
        obj["expiryTime"] = self.expiry_time
        obj["contentType"] = "text"
        obj["content"] = self.content
        obj["username"] = self.username
        obj["location"] = {}
        obj["location"]["latitude"] = self.lat
        obj["location"]["longitude"] = self.lng

# Set "homepage" to index.html
@app.route("/")
def index():
    return "Hello world"

@app.route("/drop", methods=["POST"])
def dropMessage():
    obj = request.json
    (msg, allowed) = theAnalyzer(obj["content"])
    if allowed:
        message = Message(obj["creationTime"], obj["expiryTime"], "text", obj["content"], obj["username"], obj["location"]["latitude"], obj["location"]["longitude"])
        db.session.add(message)
        db.session.commit()
        print("Add to database: " + str(message))
        return ""
    return msg

@app.route("/message", methods=["POST"])
def gatherMessages():
    obj = request.json
    msgs = db.session.query(Message).filter(func.abs(Message.lat - obj["location"]["latitude"]) < 1).filter(func.abs(Message.lng - obj["location"]["longitude"]) < 1 ).filter(Message.expiry_time > obj["currentTime"])
    return json.dumps(map(lambda m: m.create_json(), msgs))

if __name__ == "__main__":
    app.debug = True
    app.run(host= "0.0.0.0")
