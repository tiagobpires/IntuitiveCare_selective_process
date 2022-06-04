from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from spectree import SpecTree


db = SQLAlchemy()
migrate = Migrate()
api = SpecTree(
    "flask",
    title="Intuitive Care Selective Process",
    path="docs",
)


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from routes import relatorio_cadop_controller

    app.register_blueprint(relatorio_cadop_controller)

    api.register(app)

    return app
