import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useModal } from '../../context/Modal';
import * as reviewActions from '../../redux/review';
import { FaStar } from 'react-icons/fa6';
import './UpdateReviewModal.css';

function UpdateReviewModal(review) {
    const dispatch = useDispatch();
    const [stars, setStars] = useState(review.review.stars);
    const [activeStars, setActiveStars] = useState(stars);
    const [reviewText, setReviewText] = useState(review.review.review_text);
    const [errors, setErrors] = useState(null);

    const { closeModal } = useModal();

    const handleMouseEnter = (index) => {
        setActiveStars(index);
    };

    const handleMouseLeave = () => {
        setActiveStars(stars);
    };

    const handleClick = (index) => {
        setStars(index);
    };

    const handleUpdate = (e) => {
        e.preventDefault();

        setErrors({});

        if (stars < 1 || stars > 5) {
            setErrors('Stars must be between 1 and 5');
            return;
        }

        if (!reviewText) {
            setErrors('Review cannot be empty');
            return;
        }

        const updatedReview = {
            ...review.review,
            stars,
            review_text: reviewText,
        }

        setErrors(null);

        dispatch(reviewActions.thunkUpdateReview(updatedReview));
        closeModal();
    }

    return (
        <div className="update-modal">
            <h2>Update Review</h2>
            {errors && <p className="error">{errors}</p>}

            <div className="review-stars">
                {[1, 2, 3, 4, 5].map((index) => {
                    return (
                        <FaStar
                            key={index}
                            className={index <= (activeStars || stars) ? 'active' : 'inactive'}
                            onMouseEnter={() => handleMouseEnter(index)}
                            onMouseLeave={handleMouseLeave}
                            onClick={() => handleClick(index)}
                        />
                    );
                })}
            </div>
            
            <textarea
                className="review-text"
                placeholder="Write your review here..."
                value={reviewText}
                onChange={(e) => setReviewText(e.target.value)}
            />
            
            <div className="update-buttons">
                <button className="confirm-update" onClick={handleUpdate}>Update</button>
                <button onClick={closeModal}>Cancel</button>
            </div>
        </div>
    );
}

export default UpdateReviewModal;