from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Book, BorrowingTransaction, Review
from app.forms import BookForm, ReviewForm
from datetime import datetime, timedelta

book_routes = Blueprint('books', __name__)

# Get all books
@book_routes.route('/')
def books():
    """
    Query for all books and returns them in a list of book dictionaries
    """
    books = Book.query.all()
    if not books:
        return jsonify({'message': 'No books found'}), 404

    return jsonify({'books': [book.to_dict() for book in books]}), 200

# Get all books of the current user
@book_routes.route('/user/<int:user_id>')
@login_required
def user_books(user_id):
    """
    Query for all books of the current user and returns them in a list of book dictionaries
    """
    if user_id != current_user.id:
        return jsonify({'message': 'You are not authorized to view these books'}), 403
    
    borrowing_transactions = BorrowingTransaction.query.filter_by(user_id=user_id).all()
    if not borrowing_transactions:
        return jsonify({'message': 'User did not borrow any books'}), 404
    
    book_ids = {transaction.book_id for transaction in borrowing_transactions if transaction.return_date is None}
    if not book_ids:
        return jsonify({'message': 'User has no currently borrowed books'}), 200

    books = Book.query.filter(Book.id.in_(book_ids)).all()
    if not books:
        return jsonify({'message': 'No books found for the borrowed transactions'}), 404
    
    return jsonify({'books': [book.to_dict() for book in books]}), 200

# Get a specific book
@book_routes.route('/<int:book_id>')
def book(book_id):
    """
    Query for a specific book and returns it as a book dictionary
    """
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    return jsonify({'book': book.to_dict()}), 200

# Create a new book
@book_routes.route('/new', methods=['POST'])
@login_required
def new_book():
    """
    Creates a new book
    """
    if not current_user.is_admin:
        return jsonify({'message': 'You are not authorized to create a new book'}), 403

    form = BookForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():

        new_book = Book(
            title = form.title.data,
            author = form.author.data,
            description = form.description.data,
            genre = form.genre.data,
            cover_image = form.cover_image.data,
            total_copies = form.total_copies.data,
            available_copies = form.available_copies.data,
            published_year = form.published_year.data,
        )

        db.session.add(new_book)
        db.session.commit()

        return jsonify({
            'message': 'Book created successfully',
            'book': new_book.to_dict()
        }), 200
    
    return jsonify({
        'message': 'Invalid data',
        'errors': form.errors
    }), 400

# Update a book
@book_routes.route('/<int:book_id>', methods=['PUT'])
@login_required
def update_book(book_id):
    """
    Update a book by ID
    """
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    
    if not current_user.is_admin:
        return jsonify({'message': 'You are not authorized to update this book'}), 403
    
    data = request.get_json()
    existing_data = book.to_dict()
    form = BookForm(data={**existing_data, **data})
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.description = form.description.data
        book.genre = form.genre.data
        book.cover_image = form.cover_image.data
        book.total_copies = form.total_copies.data
        book.available_copies = form.available_copies.data
        book.published_year = form.published_year.data

        db.session.commit()

        return jsonify({ 
            'message': 'Book updated successfully', 
            'book': book.to_dict() 
        }), 200
    
    return jsonify({ 
        'message': 'Validation error', 
        'errors': form.errors
    }), 400

# Delete a book
@book_routes.route('/<int:book_id>', methods=['DELETE'])
@login_required
def delete_book(book_id):
    """
    Delete a book by ID
    """
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    
    if not current_user.is_admin:
        return jsonify({'message': 'You are not authorized to delete this book'}), 403
    
    db.session.delete(book)
    db.session.commit()

    return jsonify({ 'message': 'Book deleted successfully' }), 200

# Other routes will be added here

# Borrow a book
# Create a new borrowing transaction
@book_routes.route('/<int:book_id>/borrow', methods=['POST'])
@login_required
def borrow_book(book_id):
    """
    Borrow a book
    """
    # Check if book exists
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    
    # Check if there are available copies
    if book.available_copies == 0:
        return jsonify({'message': 'No available copies of this book'}), 400
    
    # Prevent duplicate borrowing
    existing_borrow = BorrowingTransaction.query.filter_by(
        user_id=current_user.id,
        book_id=book_id,
        status='BORROWED'
    ).first()
    if existing_borrow:
        return jsonify({'message': 'You have already borrowed this book'}), 400
    
    # Check borrowing limit
    tier_limits = {
        'BASIC': 5,
        'PREMIUM': 10,
        'VIP': 20
    }
    borrowed_books = BorrowingTransaction.query.filter_by(
        user_id=current_user.id,
        status='BORROWED'
    ).count()
    if borrowed_books >= tier_limits.get(current_user.tier, 2):
        return jsonify({'message': f'Maximum borrowing limit reached for {current_user.tier} tier'}), 400
    
    # Borrow length based on tier
    borrow_length = 14
    if current_user.tier == 'PREMIUM':
        borrow_length = 60
    elif current_user.tier == 'VIP':
        borrow_length = 180

    borrow_date = datetime.utcnow()
    due_date = (borrow_date + timedelta(days=borrow_length)).date()

    # Create borrowing transaction
    borrowing_transaction = BorrowingTransaction(
        user_id=current_user.id,
        book_id=book_id,
        borrow_date=borrow_date,
        due_date=due_date,
        status='BORROWED'
    )
    book.available_copies -= 1

    db.session.add(borrowing_transaction)
    db.session.commit()

    return jsonify({
        'message': 'Book borrowed successfully',
        'book': book.title,
        'borrow_date': borrowing_transaction.borrow_date,
        'due_date': borrowing_transaction.due_date
    }), 200

# Create a new review
@book_routes.route('/<int:book_id>/review', methods=['POST'])
@login_required
def review_book(book_id):
    """
    Create a new review for a book
    """
    # Check if book exists
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    
    # Check if user already reviewed the book
    existing_review = Review.query.filter_by(
        user_id=current_user.id,
        book_id=book_id
    ).first()
    if existing_review:
        return jsonify({'message': 'You have already reviewed this book'}), 400

    data = request.get_json()
    review_text = data.get('review_text')
    stars = data.get('stars')

    # Validate the review data
    if not review_text or not stars:
        return jsonify({'message': 'Review text and stars are required'}), 400

    # Create and save the new review
    new_review = Review(
        user_id=current_user.id,
        book_id=book_id,
        review_text=review_text,
        stars=stars
    )

    db.session.add(new_review)
    db.session.commit()

    return jsonify({
        'message': 'Review created successfully',
        'review': new_review.to_dict()
    }), 200

# THIS CODE IS COMMENTED OUT BECAUSE THE REVIEW FORM IS NOT BEING USED ANYMORE
# VALIDATION IS DONE IN THE FRONTEND
    # form = ReviewForm()
    # form['csrf_token'].data = request.cookies['csrf_token']

    # if form.validate_on_submit():
    #     review_text = form.review_text.data
    #     stars = form.stars.data
    
    #     new_review = Review(
    #         user_id = current_user.id,
    #         book_id = book_id,
    #         review_text = review_text,
    #         stars = stars
    #     )

    #     db.session.add(new_review)
    #     db.session.commit()

    #     return jsonify({
    #         'message': 'Review created successfully',
    #         'review': new_review.to_dict()
    #     }), 200
    
    # return jsonify({
    #     'message': 'Invalid data',
    #     'errors': form.errors
    # }), 400