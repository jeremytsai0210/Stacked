import { useState } from 'react';
import { useDispatch } from 'react-redux';
import * as reviewActions from '../../redux/review';
import { FaStar } from 'react-icons/fa6';
import './ReviewForm.css';

function ReviewForm({ bookId }) {
    const dispatch = useDispatch();

    const [stars, setStars] = useState(0);
    const [activeStars, setActiveStars] = useState(stars);
    const [reviewText, setReviewText] = useState('');
    const [errors, setErrors] = useState({});

    const handleMouseEnter = (index) => {
        setActiveStars(index);
    };

    const handleMouseLeave = () => {
        setActiveStars(stars);
    };

    const handleClick = (index) => {
        setStars(index);
    };
    
    const handleSubmit = async (e) => {
        e.preventDefault();

        setErrors({});

        const newReview = {
            review_text: reviewText,
            stars
        };

        try {
            const data = await dispatch(reviewActions.thunkAddReview(newReview, bookId));
            if (data?.message) {
                // Show backend error messages here
                setErrors({ message: data.message });
            } else {
                // Reset form after successful submission
                setStars(1);
                setReviewText('');
            }
        } catch (err) {
            setErrors({ message: 'An error occurred while submitting your review.' });
        }
    };

    return (
        <form className="review-form-container" onSubmit={handleSubmit}>
            <h3>Submit a Review</h3>
            {errors.message && <p className="error-message">{errors.message}</p>}

            <div className="review-form">
                <label>
                    <textarea
                        placeholder="Write your review here..."
                        name="review_text"
                        value={reviewText}
                        onChange={(e) => setReviewText(e.target.value)}
                        required
                    />
                </label>

                <label>
                    <div className="stars">
                        {/* <label htmlFor="rating">Rating</label> */}
                        {[1, 2, 3, 4, 5].map((index) => (
                        <div
                            key={index}
                            className={index <= activeStars ? "filled" : "empty"}
                            onMouseEnter={() => handleMouseEnter(index)}
                            onMouseLeave={handleMouseLeave}
                            onClick={() => handleClick(index)}
                        >
                            <FaStar />
                        </div>
                        ))}
                        {errors.stars && <p>{errors.stars}</p>}
                    </div>
                </label>
                <button className="review-submit-button" type="submit">Submit Review</button>
            </div>
        </form>
    );
}

export default ReviewForm;
