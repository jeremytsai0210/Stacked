import { useDispatch } from 'react-redux';
import { useModal } from '../../context/Modal';
import * as reviewActions from '../../redux/review';
import './DeleteReviewModal.css';

function DeleteReviewModal(reviewId) {
    const dispatch = useDispatch();

    const { closeModal } = useModal();

    const handleDelete = () => {
        dispatch(reviewActions.thunkDeleteReview(reviewId.reviewId));
        closeModal();
    }

    return (
        <div className="delete-modal">
            <h2>Delete Review</h2>
            <p>Are you sure you want to delete this review?</p>
            <div className="delete-buttons">
                <button className="confirm-delete" onClick={handleDelete}>Delete</button>
                <button onClick={closeModal}>Cancel</button>
            </div>
        </div>
    )
}

export default DeleteReviewModal;