import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';
import * as bookActions from '../../redux/book';
import * as reviewActions from '../../redux/review';
import { FaStar } from 'react-icons/fa6';
import ReviewForm from './ReviewForm';
import OpenModalButton from '../OpenModalButton';
import DeleteReviewModal from '../DeleteReviewModal';
import UpdateReviewModal from '../UpdateReviewModal';
import './BookDetailPage.css';

function BookDetailPage() {
    const dispatch = useDispatch();
    const { bookId } = useParams();

    const book = useSelector((state) => state.books[bookId]);
    const user = useSelector((state) => state.session.user);
    const reviews = useSelector((state) => Object.values(state.reviews));

    useEffect(() => {
        dispatch(bookActions.thunkGetSingleBook(bookId));
        dispatch(reviewActions.thunkGetBookReviews(bookId));
    }, [dispatch, bookId]);

    const totalReviews = reviews.length;
    const averageRating = totalReviews
        ? (reviews.reduce((sum, review) => sum + review.stars, 0) / totalReviews).toFixed(1)
        : null;

    return (
        <div className="book-detail">
            <h1>{book?.title} - {averageRating} <FaStar className="big-star"/></h1>
            <div className="book-detail-content">
                <img src={book?.cover_image} alt={book?.title} className="cover-image" />
                <div className="book-information">
                    <p>
                        <span className="book-information-label">Author:</span>
                        {book?.author}
                    </p>
                    <p>
                        <span className="book-information-label">Genre:</span>
                        {book?.genre}
                    </p>
                    <p>
                        <span className="book-information-label">Year published:</span>
                        {book?.published_year}
                    </p>
                    <p>
                        <span className="book-information-label">Description:</span>
                        {book?.description}
                    </p>
                    <p>
                        <span className="book-information-label">Available copies:</span>
                        <span
                            className={`available-copies ${book?.available_copies === 0 ? 'no-copies' : ''}`}
                        >
                            {book?.available_copies}
                        </span>
                    </p>
                    <p>
                        <span className="book-information-label">Total rating:</span>
                        {averageRating} <FaStar className="small-star"/>
                    </p>
                    <p>
                        <span className="book-information-label">Total reviews:</span>
                        {totalReviews}
                    </p>

                    <button
                        className="borrow-button"
                        disabled={!user || book?.available_copies === 0}
                        title={
                            !user 
                                ? 'You need to log in to borrow a book!' 
                                : book?.available_copies === 0 
                                    ? 'No copies available.' 
                                    : ''
                        }
                        onClick={() => {
                            if (user) {
                                alert('Borrow button clicked!');
                            }
                        }}
                    >
                        Borrow
                    </button>
                    <p>
                        {!user ? '- Log in to borrow a book!' : ''}
                    </p>
                </div>
            </div>

            <div className="reviews-content">
                <h2>Reviews</h2>
                {!reviews.some((review) => review.user.id === user?.id) && user && (
                    <ReviewForm bookId={bookId} />
                )}
                {reviews.map((review) => {
                    const reviewDate = new Date(review.updated_at).toLocaleDateString();
                    const isUserReview = review.user.id === user?.id;
                    return (
                        <div key={review.id} className={`review-tile ${isUserReview ? 'user-review' : ''}`}>
                            <div className="review-header">
                                <p className="review-user">{review.user.username}</p>
                                <p className="review-date">{reviewDate}</p>
                            </div>
                            <div className="review-stars">
                                {[...Array(review.stars)].map((_, i) => (
                                    <FaStar key={i} />
                                ))}
                            </div>
                            <p className="review-text">{review.review_text}</p>
                            {isUserReview && (
                                <div className="review-actions">
                                    <OpenModalButton
                                        className="update-button"
                                        buttonText="Update"
                                        modalComponent={<UpdateReviewModal review={review} />}
                                    />
                                    <OpenModalButton
                                        className="delete-button"
                                        buttonText="Delete"
                                        modalComponent={<DeleteReviewModal reviewId={review.id}/>}
                                    />
                                </div>
                            )}
                            <hr/>
                        </div>
                    );
                })}
            </div>
        </div>
    );
}

export default BookDetailPage;