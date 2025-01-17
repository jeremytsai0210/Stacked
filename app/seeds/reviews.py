from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime, timedelta


# Adds a demo review, you can add other reviews here if you want
def seed_reviews():
    review1 = Review(
        user_id=1,
        book_id=1,
        review_text="A captivating and beautifully written story. Highly recommended!",
        stars=5,
        created_at=datetime.utcnow() - timedelta(days=30),
        updated_at=datetime.utcnow() - timedelta(days=30),
    )
    review2 = Review(
        user_id=2,
        book_id=2,
        review_text="An interesting read, but it was a bit slow in some parts.",
        stars=3,
        created_at=datetime.utcnow() - timedelta(days=25),
        updated_at=datetime.utcnow() - timedelta(days=25),
    )
    review3 = Review(
        user_id=3,
        book_id=3,
        review_text="An absolute masterpiece. One of my all-time favorites!",
        stars=5,
        created_at=datetime.utcnow() - timedelta(days=20),
        updated_at=datetime.utcnow() - timedelta(days=20),
    )
    review4 = Review(
        user_id=4,
        book_id=4,
        review_text="I struggled to finish this book. It wasn’t for me.",
        stars=2,
        created_at=datetime.utcnow() - timedelta(days=15),
        updated_at=datetime.utcnow() - timedelta(days=15),
    )
    review5 = Review(
        user_id=5,
        book_id=5,
        review_text="A solid book with some great insights and valuable lessons.",
        stars=4,
        created_at=datetime.utcnow() - timedelta(days=10),
        updated_at=datetime.utcnow() - timedelta(days=10),
    )
    review6 = Review(
        user_id=2,
        book_id=1,
        review_text="This book left a lasting impression on me. Highly recommend to everyone.",
        stars=5,
        created_at=datetime.utcnow() - timedelta(days=5),
        updated_at=datetime.utcnow() - timedelta(days=5),
    )
    review7 = Review(
        user_id=3,
        book_id=6,
        review_text="A truly innovative story with a compelling narrative. Couldn't put it down!",
        stars=5,
        created_at=datetime.utcnow() - timedelta(days=28),
        updated_at=datetime.utcnow() - timedelta(days=28),
    )
    review8 = Review(
        user_id=4,
        book_id=7,
        review_text="It was an okay read. Some parts were great, but others dragged on too much.",
        stars=3,
        created_at=datetime.utcnow() - timedelta(days=22),
        updated_at=datetime.utcnow() - timedelta(days=22),
    )
    review9 = Review(
        user_id=1,
        book_id=8,
        review_text="Not my favorite, but I can see why others might like it. Too predictable for me.",
        stars=2,
        created_at=datetime.utcnow() - timedelta(days=18),
        updated_at=datetime.utcnow() - timedelta(days=18),
    )
    review10 = Review(
        user_id=5,
        book_id=9,
        review_text="An inspiring and thought-provoking story that kept me hooked till the end.",
        stars=4,
        created_at=datetime.utcnow() - timedelta(days=14),
        updated_at=datetime.utcnow() - timedelta(days=14),
    )
    review11 = Review(
        user_id=2,
        book_id=10,
        review_text="A thrilling tale that had me on the edge of my seat. Excellent pacing and characters.",
        stars=5,
        created_at=datetime.utcnow() - timedelta(days=12),
        updated_at=datetime.utcnow() - timedelta(days=12),
    )
    review12 = Review(
        user_id=4,
        book_id=11,
        review_text="While the world-building was fantastic, the story itself lacked depth in my opinion.",
        stars=3,
        created_at=datetime.utcnow() - timedelta(days=9),
        updated_at=datetime.utcnow() - timedelta(days=9),
    )
    review13 = Review(
        user_id=3,
        book_id=12,
        review_text="An underrated gem! I loved the themes and the characters’ growth throughout the story.",
        stars=4,
        created_at=datetime.utcnow() - timedelta(days=6),
        updated_at=datetime.utcnow() - timedelta(days=6),
    )
    review14 = Review(
        user_id=1,
        book_id=13,
        review_text="A haunting tale that left me questioning everything. The suspense was incredible.",
        stars=5,
        created_at=datetime.utcnow() - timedelta(days=4),
        updated_at=datetime.utcnow() - timedelta(days=4),
    )
    review15 = Review(
        user_id=5,
        book_id=14,
        review_text="This book was a complete letdown. I couldn't connect with the plot or the characters.",
        stars=1,
        created_at=datetime.utcnow() - timedelta(days=2),
        updated_at=datetime.utcnow() - timedelta(days=2),
    )
    review16 = Review(
        user_id=2,
        book_id=15,
        review_text="A page-turner from start to finish! The twists were absolutely brilliant.",
        stars=5,
        created_at=datetime.utcnow() - timedelta(days=10),
        updated_at=datetime.utcnow() - timedelta(days=10),
    )
    review17 = Review(
        user_id=3,
        book_id=16,
        review_text="The premise was intriguing, but the execution fell flat. Not my favorite.",
        stars=2,
        created_at=datetime.utcnow() - timedelta(days=8),
        updated_at=datetime.utcnow() - timedelta(days=8),
    )
    review18 = Review(
        user_id=1,
        book_id=17,
        review_text="A wonderfully crafted story with rich characters and an emotional punch.",
        stars=4,
        created_at=datetime.utcnow() - timedelta(days=7),
        updated_at=datetime.utcnow() - timedelta(days=7),
    )
    review19 = Review(
        user_id=4,
        book_id=18,
        review_text="This book is overrated. The plot was too convoluted for me to enjoy.",
        stars=2,
        created_at=datetime.utcnow() - timedelta(days=3),
        updated_at=datetime.utcnow() - timedelta(days=3),
    )
    review20 = Review(
        user_id=5,
        book_id=19,
        review_text="Absolutely stunning. This is one of those books that stays with you long after you finish.",
        stars=5,
        created_at=datetime.utcnow() - timedelta(days=1),
        updated_at=datetime.utcnow() - timedelta(days=1),
    )
    review21 = Review(
        user_id=3,
        book_id=1,
        review_text="An unforgettable story. It’s a book everyone should read at least once.",
        stars=5,
        created_at=datetime.utcnow() - timedelta(days=12),
        updated_at=datetime.utcnow() - timedelta(days=12),
    )
    review22 = Review(
        user_id=4,
        book_id=2,
        review_text="The ideas presented were interesting, but the narrative style didn’t work for me.",
        stars=3,
        created_at=datetime.utcnow() - timedelta(days=9),
        updated_at=datetime.utcnow() - timedelta(days=9),
    )
    review23 = Review(
        user_id=5,
        book_id=3,
        review_text="A brilliant take on humanity’s evolution. Eye-opening and thought-provoking.",
        stars=5,
        created_at=datetime.utcnow() - timedelta(days=14),
        updated_at=datetime.utcnow() - timedelta(days=14),
    )
    review24 = Review(
        user_id=2,
        book_id=4,
        review_text="I was hooked by the writing style, but the characters lacked depth.",
        stars=3,
        created_at=datetime.utcnow() - timedelta(days=8),
        updated_at=datetime.utcnow() - timedelta(days=8),
    )
    review25 = Review(
        user_id=1,
        book_id=5,
        review_text="This memoir was deeply inspiring. Michelle Obama’s journey is incredible.",
        stars=5,
        created_at=datetime.utcnow() - timedelta(days=6),
        updated_at=datetime.utcnow() - timedelta(days=6),
    )
    review26 = Review(
        user_id=3,
        book_id=6,
        review_text="A chilling story that kept me up at night. Horror fans, don’t miss this one.",
        stars=4,
        created_at=datetime.utcnow() - timedelta(days=11),
        updated_at=datetime.utcnow() - timedelta(days=11),
    )
    review27 = Review(
        user_id=4,
        book_id=7,
        review_text="The romance was heartfelt, but the plot was somewhat predictable.",
        stars=3,
        created_at=datetime.utcnow() - timedelta(days=7),
        updated_at=datetime.utcnow() - timedelta(days=7),
    )
    review28 = Review(
        user_id=5,
        book_id=8,
        review_text="A clever mystery with plenty of twists. I couldn’t put it down!",
        stars=4,
        created_at=datetime.utcnow() - timedelta(days=10),
        updated_at=datetime.utcnow() - timedelta(days=10),
    )
    review29 = Review(
        user_id=1,
        book_id=10,
        review_text="This thriller was intense! The pacing and suspense were perfectly executed.",
        stars=5,
        created_at=datetime.utcnow() - timedelta(days=4),
        updated_at=datetime.utcnow() - timedelta(days=4),
    )
    review30 = Review(
        user_id=2,
        book_id=9,
        review_text="The science fiction elements were creative, but the characters fell flat.",
        stars=3,
        created_at=datetime.utcnow() - timedelta(days=2),
        updated_at=datetime.utcnow() - timedelta(days=2),
    )

    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.add(review6)
    db.session.add(review7)
    db.session.add(review8)
    db.session.add(review9)
    db.session.add(review10)
    db.session.add(review11)
    db.session.add(review12)
    db.session.add(review13)
    db.session.add(review14)
    db.session.add(review15)
    db.session.add(review16)
    db.session.add(review17)
    db.session.add(review18)
    db.session.add(review19)
    db.session.add(review20)
    db.session.add(review21)
    db.session.add(review22)
    db.session.add(review23)
    db.session.add(review24)
    db.session.add(review25)
    db.session.add(review26)
    db.session.add(review27)
    db.session.add(review28)
    db.session.add(review29)
    db.session.add(review30)
    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f'TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;')
    else:
        db.session.execute(text('DELETE FROM reviews'))

    db.session.commit()