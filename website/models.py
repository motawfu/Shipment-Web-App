from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Freightproperty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transportation_type = db.Column(db.String(20))
    count = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    length = db.Column(db.Integer)
    breadth = db.Column(db.Integer)
    height = db.Column(db.Integer)
    source = db.Column(db.String(150))
    source_pincode =db.Column(db.String(150),default=None)
    destination = db.Column(db.String(150))
    destination_pincode = db.Column(db.String(150),default=None)

