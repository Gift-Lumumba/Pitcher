from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    the_pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
    the_comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    the_upvotes = db.relationship('Upvote', backref = 'user', lazy = 'dynamic')
    the_downvotes = db.relationship('Downvote', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitchs'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category = db.Column(db.String(255))
    details = db.Column(db.String(255))
    the_comment = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')
    the_upvotes = db.relationship('Upvote', backref = 'pitch', lazy = 'dynamic')
    the_downvotes = db.relationship('Downvote', backref = 'pitch', lazy = 'dynamic')

    def __repr__(self):
        return f'Pitch {self.details}'


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitchs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    information = db.Column(db.String(255))

    def __repr__(self):
        return f'Comment {self.information}'

class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitchs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    upvote = db.Column(db.Integer,default=1)

    def __repr__(self):
        return f'Upvote {self.upvote}'


class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitchs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    downvote = db.Column(db.Integer,default=1)

    def __repr__(self):
        return f'Downvote {self.downvote}'
