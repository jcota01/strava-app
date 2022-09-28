from flask_login import LoginManager, UserMixin
from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    refresh_token = db.Column(db.String(100))
    access_token = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password


def init_db():
    db.drop_all()
    db.create_all()
    new_user = User(username="admin", password="hello")
    db.session.add(new_user)
    db.session.commit()
