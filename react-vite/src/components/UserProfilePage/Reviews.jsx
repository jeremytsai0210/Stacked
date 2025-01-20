import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import * as reviewActions from '../../redux/review';
import { FaStar } from 'react-icons/fa6';
import './Reviews.css';

function Reviews() {
    const dispatch = useDispatch();

    const user = useSelector((state) => state.session.user);
    const reviews = useSelector((state) => Object.values(state.reviews));

    useEffect(() => {
        dispatch(reviewActions.thunkGetUserReviews(user.id));
    }, [dispatch, user.id]);

    return (
        <>
            <h1>My Reviews</h1>
            <div className="user-review-grid">
                {reviews.map((review) => {
                    const reviewDate = new Date(review.updated_at).toLocaleDateString();

                    return (
                        <div key={review.id} className={`user-review-tile`}>
                            <div className="user-review-header">
                                <div className="user-review-book">
                                    <Link to={`/books/${review.book.id}`}>
                                        <img src={review.book.cover_image} alt={review.book.title} className="user-review-cover-image" />
                                    </Link>
                                    <div className="user-review-header-text">
                                        <Link to={`/books/${review.book.id}`}>
                                            <h3 className="book-title">{review.book.title}</h3>
                                        </Link>
                                        <h6 className="book-author">{review.book.author}</h6>
                                    </div>
                                </div>
                                <div className="user-review-actions">
                                    <button onClick={() => alert('Update button clicked!')}>Update</button>
                                    <button onClick={() => alert('Delete button clicked!')}>Delete</button>
                                </div>
                            </div>
                            <div className="user-review-content">
                                <div className="review-stars">
                                    {[...Array(review.stars)].map((_, i) => (
                                        <FaStar key={i} />
                                    ))}
                                </div>
                                <p className="review-text">{review.review_text}</p>
                                <p className="review-date">{reviewDate}</p>
                            </div>
                            <hr />
                        </div>
                    );
                })}            
            </div>

        </>
    );
}

export default Reviews;
