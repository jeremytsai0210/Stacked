from app.models import db, Avatar, environment, SCHEMA
from sqlalchemy.sql import text

# Adds a demo avatar, you can add other avatars here if you want
def seed_avatars():
    avatar1 = Avatar(
        avatar_image="/static/avatars/bat.png",
        description="Bat",
        is_default=True,
        selected=False,
        user_id=None
    )
    avatar2 = Avatar(
        avatar_image="/static/avatars/bear.png",
        description="Bear",
        is_default=True,
        selected=False,
        user_id=None
    )
    avatar3 = Avatar(
        avatar_image="/static/avatars/cat.png",
        description="Cat",
        is_default=True,
        selected=False,
        user_id=None
    )
    avatar4 = Avatar(
        avatar_image="/static/avatars/cow.png",
        description="Cow",
        is_default=True,
        selected=False,
        user_id=None
    )
    avatar5 = Avatar(
        avatar_image="/static/avatars/deer.png",
        description="Deer",
        is_default=True,
        selected=False,
        user_id=None
    )
    avatar6 = Avatar(
        avatar_image="/static/avatars/fox.png",
        description="Fox",
        is_default=True,
        selected=False,
        user_id=None
    )
    avatar7 = Avatar(
        avatar_image="/static/avatars/frog.png",
        description="Frog",
        is_default=True,
        selected=False,
        user_id=None
    )
    avatar8 = Avatar(
        avatar_image="/static/avatars/koala.png",
        description="Koala",
        is_default=True,
        selected=False,
        user_id=None
    )
    avatar9 = Avatar(
        avatar_image="/static/avatars/octopus.png",
        description="Octopus",
        is_default=True,
        selected=False,
        user_id=None
    )

    db.session.add(avatar1)
    db.session.add(avatar2)
    db.session.add(avatar3)
    db.session.add(avatar4)
    db.session.add(avatar5)
    db.session.add(avatar6)
    db.session.add(avatar7)
    db.session.add(avatar8)
    db.session.add(avatar9)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_avatars():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.avatars RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM avatars"))

    db.session.commit()
