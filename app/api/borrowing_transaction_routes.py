from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, BorrowingTransaction, Book
from datetime import datetime, timedelta

borrowing_transaction_routes = Blueprint('borrowing_transactions', __name__)

# Get all borrowing transactions
@borrowing_transaction_routes.route('/')
@login_required
def borrowing_transactions():
    """
    Query for all borrowing transactions and returns them in a list of transaction dictionaries
    """
    if not current_user.is_admin:
        return jsonify({'message': 'You are not authorized to view these transactions'}), 403

    borrowing_transactions = BorrowingTransaction.query.all()
    if not borrowing_transactions:
        return jsonify({'message': 'No borrowing transactions found'}), 404

    return jsonify({'borrowing_transactions': [transaction.to_dict() for transaction in borrowing_transactions]}), 200

# Get all borrowing transactions of current user
@borrowing_transaction_routes.route('/current')
@login_required
def current_user_borrowing_transactions():
    """
    Query for all borrowing transactions of the current user and returns them in a list of transaction dictionaries
    """
    borrowing_transactions = BorrowingTransaction.query.filter_by(user_id=current_user.id).all()
    if not borrowing_transactions:
        return jsonify({'message': 'You did not borrow any books'}), 404

    return jsonify({'borrowing_transactions': [transaction.to_dict() for transaction in borrowing_transactions]}), 200

# Get all borrowing transactions of a specific user
@borrowing_transaction_routes.route('/user/<int:user_id>')
@login_required
def user_borrowing_transactions(user_id):
    """
    Query for all borrowing transactions of a specific user and returns them in a list of transaction dictionaries
    """
    if user_id != current_user.id and not current_user.is_admin:
        return jsonify({'message': 'You are not authorized to view these transactions'}), 403

    borrowing_transactions = BorrowingTransaction.query.filter_by(user_id=user_id).all()
    if not borrowing_transactions:
        return jsonify({'message': 'User did not borrow any books'}), 404

    return jsonify({'borrowing_transactions': [transaction.to_dict() for transaction in borrowing_transactions]}), 200

# Get a specific borrowing transaction
@borrowing_transaction_routes.route('/<int:transaction_id>')
@login_required
def borrowing_transaction(transaction_id):
    """
    Query for a specific borrowing transaction and returns it as a transaction dictionary
    """
    transaction = BorrowingTransaction.query.get(transaction_id)
    if not transaction:
        return jsonify({'message': 'Borrowing transaction not found'}), 404
    
    if transaction.user_id != current_user.id and not current_user.is_admin:
        return jsonify({'message': 'You are not authorized to view this transaction'}), 403

    return jsonify({'borrowing_transaction': transaction.to_dict()}), 200

# Create a new borrowing transaction
# Borrowing transactions are created when a user borrows a book
# This route will be under the books route

# Return a book
# Update a borrowing transaction
@borrowing_transaction_routes.route('/<int:transaction_id>/return', methods=['PATCH'])
@login_required
def return_book(transaction_id):
    """
    Updates a borrowing transaction to mark a book as returned
    """
    transaction = BorrowingTransaction.query.get(transaction_id)
    if not transaction:
        return jsonify({'message': 'Borrowing transaction not found'}), 404
    
    if transaction.user_id != current_user.id and not current_user.is_admin:
        return jsonify({'message': 'You are not authorized to return this book'}), 403

    if transaction.return_date:
        return jsonify({'message': 'Book has already been returned'}), 400
    
    book = Book.query.get(transaction.book_id)
    transaction.return_date = datetime.now().date()
    if transaction.return_date > transaction.due_date:
        transaction.status = 'OVERDUE'
    else:
        transaction.status = 'RETURNED'

    book.available_copies += 1

    db.session.commit()

    return jsonify({'borrowing_transaction': transaction.to_dict()}), 200

# Renew a book
# Update a borrowing transaction
@borrowing_transaction_routes.route('/<int:transaction_id>/renew', methods=['PATCH'])
@login_required
def renew_book(transaction_id):
    """
    Updates a borrowing transaction to renew a book
    """
    transaction = BorrowingTransaction.query.get(transaction_id)
    if not transaction:
        return jsonify({'message': 'Borrowing transaction not found'}), 404
    
    if not current_user.is_admin:
        return jsonify({'message': 'You are not authorized to renew this book'}), 403

    if transaction.return_date:
        return jsonify({'message': 'Book has already been returned'}), 400

    new_due_date = (transaction.due_date + timedelta(weeks=2))
    transaction.due_date = new_due_date

    db.session.commit()

    return jsonify({'borrowing_transaction': transaction.to_dict()}), 200

# Delete a borrowing transaction
@borrowing_transaction_routes.route('/<int:transaction_id>', methods=['DELETE'])
@login_required
def delete_borrowing_transaction(transaction_id):
    """
    Delete a borrowing transaction by ID
    """
    transaction = BorrowingTransaction.query.get(transaction_id)
    if not transaction:
        return jsonify({'message': 'Borrowing transaction not found'}), 404
    
    if not current_user.is_admin:
        return jsonify({'message': 'You are not authorized to delete this transaction'}), 403

    db.session.delete(transaction)
    db.session.commit()

    return jsonify({'message': 'Borrowing transaction deleted successfully'}), 200