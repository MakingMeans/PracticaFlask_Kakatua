from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Registro(db.Model):
    __tablename__ = 'registro'
    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Numeric(10, 2), nullable=False)
    num2 = db.Column(db.Numeric(10, 2), nullable=False)
    operacion = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)