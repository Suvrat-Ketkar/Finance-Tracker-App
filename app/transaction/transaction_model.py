from app.extensions import db  # Import the db instance from __init__.py
from datetime import datetime
from uuid import uuid4
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(
        db.String(80), 
        db.ForeignKey('users_new.username'),  # Foreign key reference
        nullable=False
    )
    amount = db.Column(db.Float, nullable=False)  # Storing as float for numeric calculations
    category = db.Column(db.String(100), nullable=False)  # E.g., "Food", "Transport", etc.
    description = db.Column(db.String(255), nullable=True)  # Optional field for transaction details
    transaction_date = db.Column(
        db.Date, 
        nullable=False, 
        default=lambda: datetime.now(IST).date()
    )  # Default is the current date in IST
    @classmethod
    def get_user_transactions(cls, username):
        return cls.query.filter_by(username=username).all() 