from app import db 
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    songs = db.relationship('Song', backref='listener', lazy='dynamic')

    def __repr__(self):

        return f'<user {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Song(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    title = db.Column(db.String(40),index=True),  
    artist = db.Column(db.String(40), index=True),
    album = db.Column(db.String(40), index=True)
    url = db.Column(db.String(40), index=True, unique=True)
    

    def __repr__(self):

        return f'<Song {self.title}>'