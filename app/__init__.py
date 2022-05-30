from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect



csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Inicie sesión para acceder a esta página!'
bootstrap = Bootstrap()


def create_app(config_class=Config):

    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_class)
    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app


from app import models
