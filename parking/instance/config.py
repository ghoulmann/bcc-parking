# instance/config.py
import os

SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'mysql://parking:parking@localhost/parking_db'
