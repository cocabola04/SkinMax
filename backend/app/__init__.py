from flask import Flask
from app.extensions import db
from app.config import Config
def create_app():
    app=Flask(__name__)
#setngs from config file
    app.config.from_object(Config)
    #connect to db
    db.init_app(app)

    #imp shit to do laterr
    #from app.blueprints.analysis import analysis_bp
    #app.register_blueprint(analysis_bp)
    with app.app_context():
        db.create_all()
    return app