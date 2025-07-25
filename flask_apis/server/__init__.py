from flask_cors import CORS
from flask import Flask
#import server configuration
# from . import server_config
#for database setting
from flask_migrate import Migrate
from server.models import db
#bcrypt for password hasing
from flask_bcrypt import Bcrypt
#authentication and authorization for jwt
from flask_jwt_extended import JWTManager
from datetime import timedelta
from server.server_config import Config

#declare bcrypt global instance
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    #configure cors
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(Config)
     #configure jwt        
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=10)  # Adjust as needed
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)  # Adjust as needed
    app.config['JWT_REFRESH_TOKEN_ENABLED'] = True
    app.config['JWT_COOKIE_CSRF_PROTECT'] = True
    app.config['JWT_COOKIE_SECURE']=True
    app.config['JWT_ACCESS_CSRF_HEADER_NAME'] = "X-CSRF-TOKEN-ACCESS"
    app.config['JWT_REFRESH_CSRF_HEADER_NAME'] = "X-CSRF-TOKEN-REFRESH"
    JWTManager(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_BINDS']['write']
    db.init_app(app)
    migrate = Migrate(app, db)
    bcrypt.init_app(app)
    return app

