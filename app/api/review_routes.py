from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Review
from app.forms import ReviewForm

review_routes = Blueprint('reviews', __name__)

# Get all reviews
@review_routes.route('/')
def reviews():
    """
    Query for all reviews and returns them in a list of review dictionaries
    """
    reviews = Review.query.all()
    if not reviews:
        return jsonify({'message': 'No reviews found'}), 404

    return jsonify({'reviews': [review.to_dict() for review in reviews]}), 200

# Get all reviews of the current user
@review_routes.route('/user/<int:user_id>')
@login_required
def user_reviews(user_id):
    """
    Query for all reviews of the current user and returns them in a list of review dictionaries
    """
    if user_id != current_user.id:
        return jsonify({'message': 'You are not authorized to view these reviews'}), 403
    
    reviews = Review.query.filter_by(user_id=user_id).all()
    if not reviews:
        return jsonify({'message': 'User did not write any reviews'}), 200

    return jsonify({'reviews': [review.to_dict() for review in reviews]}), 200

# Get all reviews of a specific book
@review_routes.route('/book/<int:book_id>')
def book_reviews(book_id):
    """
    Query for all reviews of a specific book and returns them in a list of review dictionaries
    """
    reviews = Review.query.filter_by(book_id=book_id).all()
    if not reviews:
        return jsonify({'message': 'No reviews found for the book'}), 404

    return jsonify({'reviews': [review.to_dict() for review in reviews]}), 200

# Get a specific review
@review_routes.route('/<int:review_id>')
def review(review_id):
    """
    Query for a specific review and returns it as a review dictionary
    """
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'message': 'Review not found'}), 404

    return jsonify({'review': review.to_dict()}), 200

# Create a new review
# Reviews are created when a user reviews a book
# This route will be under the books route

# Update a review
@review_routes.route('/<int:review_id>', methods=['PUT'])
@login_required
def update_review(review_id):
    """
    Update a review for a book
    """
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'message': 'Review not found'}), 404

    if review.user_id != current_user.id:
        return jsonify({'message': 'You are not authorized to update this review'}), 403

    data = request.get_json()
    existing_data = review.to_dict()
    form = ReviewForm(data={**existing_data, **data})
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():

        review.review_text = form.review_text.data
        review.stars = form.stars.data

        db.session.commit()

        return jsonify({
            'message': 'Review updated successfully',
            'review': review.to_dict()
        }), 200
    
    return jsonify({
        'message': 'Invalid data',
        'errors': form.errors
    }), 400

# Delete a review
@review_routes.route('/<int:review_id>', methods=['DELETE'])
@login_required
def delete_review(review_id):
    """
    Delete a review for a book
    """
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'message': 'Review not found'}), 404

    if review.user_id != current_user.id:
        return jsonify({'message': 'You are not authorized to delete this review'}), 403

    db.session.delete(review)
    db.session.commit()

    return jsonify({'message': 'Review deleted successfully'}), 200