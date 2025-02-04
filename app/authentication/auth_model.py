from app.extensions import db, bcrypt
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = 'users_new'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

# class Transaction(db.Model):
#     __tablename__ = 'transactions'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     amount = db.Column(db.Float, nullable=False)
#     category = db.Column(db.String(50), nullable=False)
#     transaction_date = db.Column(db.Date, nullable=False)
#     date_added = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
