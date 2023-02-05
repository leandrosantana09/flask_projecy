from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db' # /// arquivo local 
db = SQLAlchemy(app)

app = Flask(__name__)

from app.controllers import default 