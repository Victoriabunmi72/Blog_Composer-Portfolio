from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'hdffdf22979d'

with app.app_context():
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    login_manager = LoginManager(app)
    login_manager.login_view = 'login'

    from app import routes, models  # noqa: E402

    @login_manager.user_loader
    def load_user(user_id):
        return models.User.query.get(int(user_id))
