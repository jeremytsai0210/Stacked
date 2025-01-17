from app.models import db, BorrowingTransaction, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime, timedelta


# Adds a borrowing transaction, you can add other transactions here if you want
def seed_borrowing_transactions():
    transaction1 = BorrowingTransaction(
        user_id=1,
        book_id=1,
        borrow_date=(datetime.utcnow() - timedelta(days=10)).date(),
        due_date=(datetime.utcnow() + timedelta(days=10)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction2 = BorrowingTransaction(
        user_id=2,
        book_id=2,
        borrow_date=(datetime.utcnow() - timedelta(days=20)).date(),
        due_date=(datetime.utcnow() - timedelta(days=10)).date(),
        return_date=(datetime.utcnow() - timedelta(days=5)).date(),
        status='RETURNED'
    )
    transaction3 = BorrowingTransaction(
        user_id=3,
        book_id=3,
        borrow_date=(datetime.utcnow() - timedelta(days=15)).date(),
        due_date=(datetime.utcnow() - timedelta(days=5)).date(),
        return_date=None,
        status='OVERDUE'
    )
    transaction4 = BorrowingTransaction(
        user_id=4,
        book_id=1,
        borrow_date=(datetime.utcnow() - timedelta(days=5)).date(),
        due_date=(datetime.utcnow() + timedelta(days=15)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction5 = BorrowingTransaction(
        user_id=5,
        book_id=4,
        borrow_date=(datetime.utcnow() - timedelta(days=25)).date(),
        due_date=(datetime.utcnow() - timedelta(days=5)).date(),
        return_date=(datetime.utcnow() - timedelta(days=2)).date(),
        status='RETURNED'
    )

    db.session.add(transaction1)
    db.session.add(transaction2)
    db.session.add(transaction3)
    db.session.add(transaction4)
    db.session.add(transaction5)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_borrowing_transactions():
    if environment == "production":
        db.session.execute(f'TRUNCATE table {SCHEMA}.borrowing_transactions RESTART IDENTITY CASCADE;')
    else:
        db.session.execute(text('DELETE FROM borrowing_transactions'))

    db.session.commit()
