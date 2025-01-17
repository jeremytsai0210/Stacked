from .db import db, environment, SCHEMA
from datetime import datetime


class Book(db.Model):
    __tablename__ = 'books'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    cover_image = db.Column(db.String, nullable=True)
    total_copies = db.Column(db.Integer, nullable=False)
    available_copies = db.Column(db.Integer, nullable=False)
    published_year = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    borrowing_transactions = db.relationship('BorrowingTransaction', back_populates='book', cascade='all, delete-orphan')
    reviews = db.relationship('Review', back_populates='book', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'genre': self.genre,
            'cover_image': self.cover_image,
            'total_copies': self.total_copies,
            'available_copies': self.available_copies,
            'published_year': self.published_year,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
