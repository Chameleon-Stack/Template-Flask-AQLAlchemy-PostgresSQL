from flask_login import LoginManager

from kanban.database import Session
from kanban.user.model.user_model import User


def init_app(app):
    login_manager = LoginManager()

    @login_manager.user_loader
    def load_user(user_id):
        with Session() as session:
            return session.get(User, int(user_id))

    login_manager.init_app(app)