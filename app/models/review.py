from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), name="fk_reviews_user_id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('books.id'), name="fk_reviews_book_id"), nullable=False)
    review_text = db.Column(db.String, nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', back_populates='reviews')
    book = db.relationship('Book', back_populates='reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'review_text': self.review_text,
            'stars': self.stars,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }