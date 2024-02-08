"""Main application file"""
from flask import Flask

from app.config import DevelopmentConfig, TestingConfig
from app.db.sqla import db
from app.db.create_db import create_models
from app.views.views import view
from app.exceptions import exp


def create_app(env='development'):

    config_map = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
    }

    app = Flask(__name__)

    app.config.from_object(config_map[env])
    app.register_blueprint(view)
    app.register_blueprint(exp)
    db.init_app(app)

    with app.app_context():
        create_models()

    return app


if __name__ == '__main__':
    app = create_app('development')
    app.run(port=8001, host="0.0.0.0")
