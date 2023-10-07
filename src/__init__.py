from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes import public
    app.register_blueprint(public)
    from .controlers import resource
    app.register_blueprint(resource)
    return app
