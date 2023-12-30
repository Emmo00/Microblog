from flask import Flask
from flask_status import FlaskStatus
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
FlaskStatus(app)

from app import routes, models
