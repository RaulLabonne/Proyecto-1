from flask import Flask


def create_app():
    """ Create an app and register the blueprints.

    The blueprints are controllers and routes.

    Returns
    -------
    Flask
        The app with blueprints ready for their execution
    """

    app = Flask(__name__)

    from .routes import public
    app.register_blueprint(public)
    from .controlers import resource
    app.register_blueprint(resource)
    return app
