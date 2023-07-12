from app.db_config import Database
from app.models import User
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from flask import flash

db_manager = Database()


class Authentication:
    def login(self, username, password):
        user = db_manager.get_user_by_username(username)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return True
        return False

    def signup(self, username, email, password):
        if db_manager.get_user_by_username(username):
            flash('Username already exists', 'error')
            return False
        if db_manager.get_user_by_email(email):
            flash('Email already exists', 'error')
            return False
        user = User(username, email, password)
        db_manager.save_user(user)
        # login_user(user)
        return True

    def logout(self):
        logout_user()

    def reset_password(self, user, new_password):
        db_manager.update_user_password(user, new_password)
