from .db import db, environment, SCHEMA, add_prefix_for_prod


class BorrowingTransaction(db.Model):
    __tablename__ = 'borrowing_transactions'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), name="fk_booking_transactions_user_id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('books.id'), name="fk_booking_transactions_book_id"), nullable=False)
    borrow_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String, nullable=False)

    user = db.relationship('User', back_populates='borrowing_transactions')
    book = db.relationship('Book', back_populates='borrowing_transactions')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'borrow_date': self.borrow_date.isoformat() if self.borrow_date else None,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'return_date': self.return_date.isoformat() if self.return_date else None,
            'status': self.status,
            'user': {
                'id': self.user.id,
                'username': self.user.username,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
            },
            'book': {
                'id': self.book.id,
                'title': self.book.title,
                'author': self.book.author,
            }
        }