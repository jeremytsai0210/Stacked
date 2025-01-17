from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Book, BorrowingTransaction
from app.forms import BookForm

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
            title=form.title.data,
            author=form.author.data,
            description=form.description.data,
            genre=form.genre.data,
            cover_image=form.cover_image.data,
            total_copies=form.total_copies.data,
            available_copies=form.available_copies.data,
            published_year=form.published_year.data,
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