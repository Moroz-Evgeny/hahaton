import base64
from datetime import datetime
from sqlalchemy import JSON
from app import db


def convert_image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    photo = db.Column(db.String, default=convert_image_to_base64('app/static/images/default.png'), nullable=True)

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String)
    ratio = db.Column(db.Float)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carbon_ratio = db.Column(db.Float, nullable=True)
    date = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

