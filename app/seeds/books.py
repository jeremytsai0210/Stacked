from app.models import db, Book, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_books():
    book1 = Book(
        title='To Kill a Mockingbird',
        author='Harper Lee',
        description='A novel about the serious issues of rape and racial inequality told through the eyes of young Scout Finch.',
        genre='FICTION',
        cover_image='https://plus.unsplash.com/premium_photo-1667239429860-f7195c1123ff?q=80&w=2143&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=10,
        available_copies=8,
        published_year=1960,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book2 = Book(
        title='1984',
        author='George Orwell',
        description='A dystopian social science fiction novel and cautionary tale about the dangers of totalitarianism.',
        genre='FICTION',
        cover_image='https://images.unsplash.com/photo-1523981354642-fa01e6c05c77?q=80&w=2101&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=15,
        available_copies=12,
        published_year=1949,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book3 = Book(
        title='Sapiens: A Brief History of Humankind',
        author='Yuval Noah Harari',
        description='An exploration of the history and impact of Homo sapiens from the Stone Age to the modern day.',
        genre='NON_FICTION',
        cover_image='https://images.unsplash.com/photo-1505664194779-8beaceb93744?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=20,
        available_copies=20,
        published_year=2011,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book4 = Book(
        title='The Great Gatsby',
        author='F. Scott Fitzgerald',
        description='A critique of the American Dream in the Jazz Age, narrated by Nick Carraway about Jay Gatsby.',
        genre='FICTION',
        cover_image='https://plus.unsplash.com/premium_photo-1669077046748-6eabc790b495?q=80&w=2080&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=8,
        available_copies=6,
        published_year=1925,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book5 = Book(
        title='Becoming',
        author='Michelle Obama',
        description='The memoir of former First Lady Michelle Obama, chronicling her personal and professional life.',
        genre='BIOGRAPHY',
        cover_image='https://images.unsplash.com/photo-1544650039-22886fbb4323?q=80&w=2080&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=12,
        available_copies=10,
        published_year=2018,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book6 = Book(
        title='The Catcher in the Rye',
        author='J.D. Salinger',
        description='A story about teenage rebellion and alienation as narrated by the iconic Holden Caulfield.',
        genre='FICTION',
        cover_image='https://images.unsplash.com/photo-1595757816291-ab4c1cba0fc2?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=10,
        available_copies=9,
        published_year=1951,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book7 = Book(
        title='The Alchemist',
        author='Paulo Coelho',
        description='A novel following a young shepherd on a journey to discover his personal legend.',
        genre='FICTION',
        cover_image='https://plus.unsplash.com/premium_photo-1661891622579-bee76e28c304?q=80&w=2081&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=15,
        available_copies=14,
        published_year=1988,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book8 = Book(
        title='Educated',
        author='Tara Westover',
        description='A memoir of a woman who grows up in a strict and abusive household in rural Idaho and seeks education as a means of escape.',
        genre='BIOGRAPHY',
        cover_image='https://images.unsplash.com/photo-1604866830893-c13cafa515d5?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=8,
        available_copies=7,
        published_year=2018,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book9 = Book(
        title='Atomic Habits',
        author='James Clear',
        description='A guide to building good habits and breaking bad ones using practical strategies.',
        genre='SELF_HELP',
        cover_image='https://images.unsplash.com/photo-1655993810480-c15dccf9b3a0?q=80&w=2080&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=18,
        available_copies=16,
        published_year=2018,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book10 = Book(
        title='Dune',
        author='Frank Herbert',
        description='A science fiction epic about politics, religion, and survival set on the desert planet of Arrakis.',
        genre='SCIENCE_FICTION',
        cover_image='https://images.unsplash.com/photo-1541615060331-ca684e62c5d3?q=80&w=1980&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=12,
        available_copies=12,
        published_year=1965,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book11 = Book(
        title='Ender’s Game',
        author='Orson Scott Card',
        description='A young genius is trained at a battle school in space to defend Earth from an alien invasion.',
        genre='SCIENCE_FICTION',
        cover_image='https://images.unsplash.com/photo-1651421569877-9f714e7822ba?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=14,
        available_copies=12,
        published_year=1985,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book12 = Book(
        title='The Martian',
        author='Andy Weir',
        description='An astronaut stranded on Mars must rely on his ingenuity to survive and signal for rescue.',
        genre='SCIENCE_FICTION',
        cover_image='https://images.unsplash.com/photo-1571769267292-e24dfadebbdc?q=80&w=2090&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=10,
        available_copies=9,
        published_year=2011,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book13 = Book(
        title='The Girl with the Dragon Tattoo',
        author='Stieg Larsson',
        description='A journalist and a hacker team up to solve a decades-old missing person case.',
        genre='MYSTERY',
        cover_image='https://images.unsplash.com/photo-1690136813822-8decbac1465e?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=8,
        available_copies=7,
        published_year=2005,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book14 = Book(
        title='Gone Girl',
        author='Gillian Flynn',
        description='A woman’s mysterious disappearance puts her husband in the spotlight as dark secrets are revealed.',
        genre='MYSTERY',
        cover_image='https://images.unsplash.com/photo-1534088568595-a066f410bcda?q=80&w=1951&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=12,
        available_copies=10,
        published_year=2012,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book15 = Book(
        title='The Shining',
        author='Stephen King',
        description='A family is isolated in a haunted hotel where the father descends into madness.',
        genre='HORROR',
        cover_image='https://images.unsplash.com/photo-1699631760911-a3be71d80390?q=80&w=1949&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=10,
        available_copies=8,
        published_year=1977,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book16 = Book(
        title='Dracula',
        author='Bram Stoker',
        description='A tale of the legendary vampire Count Dracula and his quest to spread the undead curse.',
        genre='HORROR',
        cover_image='https://images.unsplash.com/photo-1618590067592-a867d8b44403?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=8,
        available_copies=7,
        published_year=1897,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book17 = Book(
        title='Pride and Prejudice',
        author='Jane Austen',
        description='A classic story of love and misunderstanding between Elizabeth Bennet and Mr. Darcy.',
        genre='ROMANCE',
        cover_image='https://plus.unsplash.com/premium_photo-1699566453610-fc493eab7da7?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=14,
        available_copies=13,
        published_year=1813,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book18 = Book(
        title='The Notebook',
        author='Nicholas Sparks',
        description='A tale of an enduring romance between two lovers separated by social differences.',
        genre='ROMANCE',
        cover_image='https://images.unsplash.com/photo-1501691223387-dd0500403074?q=80&w=2127&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=12,
        available_copies=11,
        published_year=1996,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book19 = Book(
        title='The Silence of the Lambs',
        author='Thomas Harris',
        description='A young FBI trainee seeks the help of an imprisoned cannibalistic serial killer to catch another murderer.',
        genre='THRILLER',
        cover_image='https://plus.unsplash.com/premium_photo-1724501850239-d9f167960c05?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=10,
        available_copies=8,
        published_year=1988,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    book20 = Book(
        title='The Girl on the Train',
        author='Paula Hawkins',
        description='A woman becomes entangled in a missing persons investigation that promises to send shockwaves throughout her life.',
        genre='THRILLER',
        cover_image='https://images.unsplash.com/photo-1544455658-080caada663c?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        total_copies=8,
        available_copies=6,
        published_year=2015,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.add(book4)
    db.session.add(book5)
    db.session.add(book6)
    db.session.add(book7)
    db.session.add(book8)
    db.session.add(book9)
    db.session.add(book10)
    db.session.add(book11)
    db.session.add(book12)
    db.session.add(book13)
    db.session.add(book14)
    db.session.add(book15)
    db.session.add(book16)
    db.session.add(book17)
    db.session.add(book18)
    db.session.add(book19)
    db.session.add(book20)
    db.session.commit()

def undo_books():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.books RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM books"))
        
    db.session.commit()