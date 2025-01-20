from app.models import db, BorrowingTransaction, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime, timedelta


# Adds a borrowing transaction, you can add other transactions here if you want
def seed_borrowing_transactions():
    transaction1 = BorrowingTransaction(
        user_id=1,
        book_id=5,
        borrow_date=(datetime.utcnow() - timedelta(days=5)).date(),
        due_date=(datetime.utcnow() + timedelta(days=5)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction2 = BorrowingTransaction(
        user_id=2,
        book_id=10,
        borrow_date=(datetime.utcnow() - timedelta(days=12)).date(),
        due_date=(datetime.utcnow() + timedelta(days=3)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction3 = BorrowingTransaction(
        user_id=3,
        book_id=15,
        borrow_date=(datetime.utcnow() - timedelta(days=7)).date(),
        due_date=(datetime.utcnow() + timedelta(days=7)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction4 = BorrowingTransaction(
        user_id=4,
        book_id=20,
        borrow_date=(datetime.utcnow() - timedelta(days=20)).date(),
        due_date=(datetime.utcnow() - timedelta(days=10)).date(),
        return_date=(datetime.utcnow() - timedelta(days=5)).date(),
        status='OVERDUE'
    )
    transaction5 = BorrowingTransaction(
        user_id=5,
        book_id=1,
        borrow_date=(datetime.utcnow() - timedelta(days=25)).date(),
        due_date=(datetime.utcnow() - timedelta(days=15)).date(),
        return_date=(datetime.utcnow() - timedelta(days=10)).date(),
        status='OVERDUE'
    )
    transaction6 = BorrowingTransaction(
        user_id=1,
        book_id=4,
        borrow_date=(datetime.utcnow() - timedelta(days=8)).date(),
        due_date=(datetime.utcnow() + timedelta(days=2)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction7 = BorrowingTransaction(
        user_id=2,
        book_id=9,
        borrow_date=(datetime.utcnow() - timedelta(days=15)).date(),
        due_date=(datetime.utcnow() - timedelta(days=5)).date(),
        return_date=(datetime.utcnow() - timedelta(days=3)).date(),
        status='OVERDUE'
    )
    transaction8 = BorrowingTransaction(
        user_id=3,
        book_id=14,
        borrow_date=(datetime.utcnow() - timedelta(days=10)).date(),
        due_date=(datetime.utcnow() + timedelta(days=5)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction9 = BorrowingTransaction(
        user_id=4,
        book_id=19,
        borrow_date=(datetime.utcnow() - timedelta(days=18)).date(),
        due_date=(datetime.utcnow() - timedelta(days=8)).date(),
        return_date=(datetime.utcnow() - timedelta(days=10)).date(),
        status='RETURNED'
    )
    transaction10 = BorrowingTransaction(
        user_id=5,
        book_id=2,
        borrow_date=(datetime.utcnow() - timedelta(days=10)).date(),
        due_date=(datetime.utcnow() + timedelta(days=7)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction11 = BorrowingTransaction(
        user_id=1,
        book_id=11,
        borrow_date=(datetime.utcnow() - timedelta(days=13)).date(),
        due_date=(datetime.utcnow() - timedelta(days=3)).date(),
        return_date=(datetime.utcnow() - timedelta(days=3)).date(),
        status='RETURNED'
    )
    transaction12 = BorrowingTransaction(
        user_id=2,
        book_id=16,
        borrow_date=(datetime.utcnow() - timedelta(days=25)).date(),
        due_date=(datetime.utcnow() - timedelta(days=15)).date(),
        return_date=(datetime.utcnow() - timedelta(days=10)).date(),
        status='OVERDUE'
    )
    transaction13 = BorrowingTransaction(
        user_id=3,
        book_id=7,
        borrow_date=(datetime.utcnow() - timedelta(days=5)).date(),
        due_date=(datetime.utcnow() + timedelta(days=5)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction14 = BorrowingTransaction(
        user_id=4,
        book_id=13,
        borrow_date=(datetime.utcnow() - timedelta(days=9)).date(),
        due_date=(datetime.utcnow() + timedelta(days=8)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction15 = BorrowingTransaction(
        user_id=5,
        book_id=6,
        borrow_date=(datetime.utcnow() - timedelta(days=30)).date(),
        due_date=(datetime.utcnow() - timedelta(days=20)).date(),
        return_date=(datetime.utcnow() - timedelta(days=15)).date(),
        status='OVERDUE'
    )
    transaction16 = BorrowingTransaction(
        user_id=1,
        book_id=1,
        borrow_date=(datetime.utcnow() - timedelta(days=10)).date(),
        due_date=(datetime.utcnow() + timedelta(days=10)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction17 = BorrowingTransaction(
        user_id=2,
        book_id=2,
        borrow_date=(datetime.utcnow() - timedelta(days=20)).date(),
        due_date=(datetime.utcnow() - timedelta(days=10)).date(),
        return_date=(datetime.utcnow() - timedelta(days=15)).date(),
        status='RETURNED'
    )
    transaction18 = BorrowingTransaction(
        user_id=3,
        book_id=3,
        borrow_date=(datetime.utcnow() - timedelta(days=15)).date(),
        due_date=(datetime.utcnow() - timedelta(days=5)).date(),
        return_date=None,
        status='OVERDUE'
    )
    transaction19 = BorrowingTransaction(
        user_id=4,
        book_id=1,
        borrow_date=(datetime.utcnow() - timedelta(days=5)).date(),
        due_date=(datetime.utcnow() + timedelta(days=15)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction20 = BorrowingTransaction(
        user_id=5,
        book_id=4,
        borrow_date=(datetime.utcnow() - timedelta(days=25)).date(),
        due_date=(datetime.utcnow() - timedelta(days=5)).date(),
        return_date=(datetime.utcnow() - timedelta(days=5)).date(),
        status='RETURNED'
    )
    transaction21 = BorrowingTransaction(
        user_id=1,
        book_id=8,
        borrow_date=(datetime.utcnow() - timedelta(days=6)).date(),
        due_date=(datetime.utcnow() + timedelta(days=4)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction22 = BorrowingTransaction(
        user_id=2,
        book_id=17,
        borrow_date=(datetime.utcnow() - timedelta(days=18)).date(),
        due_date=(datetime.utcnow() - timedelta(days=8)).date(),
        return_date=(datetime.utcnow() - timedelta(days=4)).date(),
        status='RETURNED'
    )
    transaction23 = BorrowingTransaction(
        user_id=3,
        book_id=12,
        borrow_date=(datetime.utcnow() - timedelta(days=2)).date(),
        due_date=(datetime.utcnow() + timedelta(days=10)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction24 = BorrowingTransaction(
        user_id=4,
        book_id=3,
        borrow_date=(datetime.utcnow() - timedelta(days=12)).date(),
        due_date=(datetime.utcnow() - timedelta(days=2)).date(),
        return_date=(datetime.utcnow() - timedelta(days=1)).date(),
        status='RETURNED'
    )
    transaction25 = BorrowingTransaction(
        user_id=5,
        book_id=18,
        borrow_date=(datetime.utcnow() - timedelta(days=7)).date(),
        due_date=(datetime.utcnow() + timedelta(days=7)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction26 = BorrowingTransaction(
        user_id=1,
        book_id=16,
        borrow_date=(datetime.utcnow() - timedelta(days=30)).date(),
        due_date=(datetime.utcnow() - timedelta(days=10)).date(),
        return_date=(datetime.utcnow() - timedelta(days=5)).date(),
        status='RETURNED'
    )
    transaction27 = BorrowingTransaction(
        user_id=2,
        book_id=11,
        borrow_date=(datetime.utcnow() - timedelta(days=20)).date(),
        due_date=(datetime.utcnow() - timedelta(days=5)).date(),
        return_date=(datetime.utcnow() - timedelta(days=15)).date(),
        status='RETURNED'
    )
    transaction28 = BorrowingTransaction(
        user_id=3,
        book_id=19,
        borrow_date=(datetime.utcnow() - timedelta(days=14)).date(),
        due_date=(datetime.utcnow() + timedelta(days=3)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction29 = BorrowingTransaction(
        user_id=4,
        book_id=6,
        borrow_date=(datetime.utcnow() - timedelta(days=9)).date(),
        due_date=(datetime.utcnow() + timedelta(days=8)).date(),
        return_date=None,
        status='BORROWED'
    )
    transaction30 = BorrowingTransaction(
        user_id=5,
        book_id=13,
        borrow_date=(datetime.utcnow() - timedelta(days=12)).date(),
        due_date=(datetime.utcnow() - timedelta(days=2)).date(),
        return_date=(datetime.utcnow() - timedelta(days=7)).date(),
        status='RETURNED'
    )

    db.session.add(transaction1)
    db.session.add(transaction2)
    db.session.add(transaction3)
    db.session.add(transaction4)
    db.session.add(transaction5)
    db.session.add(transaction6)
    db.session.add(transaction7)
    db.session.add(transaction8)
    db.session.add(transaction9)
    db.session.add(transaction10)
    db.session.add(transaction11)
    db.session.add(transaction12)
    db.session.add(transaction13)
    db.session.add(transaction14)
    db.session.add(transaction15)
    db.session.add(transaction16)
    db.session.add(transaction17)
    db.session.add(transaction18)
    db.session.add(transaction19)
    db.session.add(transaction20)
    db.session.add(transaction21)
    db.session.add(transaction22)
    db.session.add(transaction23)
    db.session.add(transaction24)
    db.session.add(transaction25)
    db.session.add(transaction26)
    db.session.add(transaction27)
    db.session.add(transaction28)
    db.session.add(transaction29)
    db.session.add(transaction30)
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
