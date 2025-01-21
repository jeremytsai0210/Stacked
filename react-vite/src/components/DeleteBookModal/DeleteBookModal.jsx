import { useDispatch } from 'react-redux';
import { useModal } from '../../context/Modal';
import * as bookActions from '../../redux/book';
import './DeleteBookModal.css';

function DeleteBookModal(bookId) {
    const dispatch = useDispatch();

    const { closeModal } = useModal();

    const handleDelete = () => {
        dispatch(bookActions.thunkDeleteBook(bookId.bookId));
        closeModal();
    }

    return (
        <div className="delete-modal">
            <h2>Delete Review</h2>
            <p>Are you sure you want to delete this book?</p>
            <div className="delete-buttons">
                <button className="confirm-delete" onClick={handleDelete}>Delete</button>
                <button onClick={closeModal}>Cancel</button>
            </div>
        </div>
    )
}

export default DeleteBookModal;