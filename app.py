from app import app, db
from app.models import User


@app.shell_context_processor
# for flask shell
def make_shell_context():
    return {'db': db, 'User': User}
