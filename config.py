import os


DEBUG = True
port = os.environ.get('PORT', 5000)
host = '0.0.0.0'
SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True