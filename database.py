from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    role = db.Column(db.String(20), nullable=False) # 'Tenant' or 'Owner'
    
    properties = db.relationship('Property', backref='owner', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)
    roommate_posts = db.relationship('RoommatePost', backref='user', lazy=True)

class Property(db.Model):
    __tablename__ = 'properties'
    property_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    rent = db.Column(db.Float, nullable=False)
    deposit = db.Column(db.Float)
    description = db.Column(db.Text)
    rooms = db.Column(db.Integer)
    furnishing = db.Column(db.String(50))
    bachelor_allowed = db.Column(db.Boolean, default=True)
    wifi = db.Column(db.Boolean, default=False)
    food = db.Column(db.Boolean, default=False)
    image_path = db.Column(db.String(300))
    
    reviews = db.relationship('Review', backref='property', lazy=True)

class Review(db.Model):
    __tablename__ = 'reviews'
    review_id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.property_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False) # 1 to 5
    comment = db.Column(db.Text)
    is_suspicious = db.Column(db.Boolean, default=False) # For AI detection
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class RoommatePost(db.Model):
    __tablename__ = 'roommate_posts'
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    profession = db.Column(db.String(100))
    food_preference = db.Column(db.String(50))
    sleep_schedule = db.Column(db.String(50))
    smoking_preference = db.Column(db.String(50), default='No')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Message(db.Model):
    __tablename__ = 'messages'
    message_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
