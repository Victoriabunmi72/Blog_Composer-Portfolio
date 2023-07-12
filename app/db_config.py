from app import db
from app.models import User


class Database:
    def __init__(self):
        db.create_all()

    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def save_user(self, user):
        db.session.add(user)
        db.session.commit()

    def update_user_password(self, user, new_password):
        user.update_password(new_password)
