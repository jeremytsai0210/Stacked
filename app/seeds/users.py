from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', 
        email='demo@aa.io', 
        password='password',
        first_name='Demo',
        last_name='User',
        tier='BASIC',
        is_admin=False,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    marnie = User(
        username='marnie',
        email='marnie@aa.io', 
        password='password',
        first_name='Marnie',
        last_name='Smith',
        tier='PREMIUM',
        is_admin=False,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    bobbie = User(
        username='bobbie', 
        email='bobbie@aa.io',
        password='password',
        first_name='Bobbie',
        last_name='Johnson',
        tier='VIP',
        is_admin=False,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    alice = User(
        username='alice', 
        email='alice@aa.io', 
        password='password', 
        first_name='Alice', 
        last_name='Wonder', 
        tier='BASIC', 
        is_admin=False, 
        created_at=datetime.utcnow(), 
        updated_at=datetime.utcnow()
    )
    charlie = User(
        username='charlie', 
        email='charlie@aa.io', 
        password='password', 
        first_name='Charlie', 
        last_name='Brown', 
        tier='BASIC', 
        is_admin=False, 
        created_at=datetime.utcnow(), 
        updated_at=datetime.utcnow()
    )
    admin_user = User(
        username='admin_user', 
        email='admin@aa.io', 
        password='password', 
        first_name='Admin', 
        last_name='User', 
        tier='VIP', 
        is_admin=True, 
        created_at=datetime.utcnow(), 
        updated_at=datetime.utcnow()
    )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(alice)
    db.session.add(charlie)
    db.session.add(admin_user)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
