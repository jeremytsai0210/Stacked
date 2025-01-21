import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useModal } from '../../context/Modal';
import * as bookActions from '../../redux/book';
import './UpdateBookModal.css';

function UpdateBookModal(book) {
    const dispatch = useDispatch();
    const [description, setDescription] = useState('');
    const [available_copies, setAvailableCopies] = useState('');
    const [total_copies, setTotalCopies] = useState('');
    const [errors, setErrors] = useState(null);

    const { closeModal } = useModal();

    const handleUpdate = (e) => {
        e.preventDefault();

        setErrors({});

        if (!description) {
            setErrors('Description cannot be empty');
            return;
        }

        if (!available_copies) {
            setErrors('Available copies cannot be empty');
            return;
        }

        if (!total_copies) {
            setErrors('Total copies cannot be empty');
            return;
        }

        if (available_copies > total_copies) {
            setErrors('Available copies cannot be greater than total copies');
            return;
        }

        const updatedBook = {
            ...book.book,
            description,
            available_copies,
            total_copies,
        }

        setErrors(null);

        dispatch(bookActions.thunkUpdateBook(updatedBook));
        closeModal();
    }

    return (
        <div className="update-book-modal">
            <h2>Update {book.book.title}</h2>
            {errors && <p className="error">{errors}</p>}

            <form className="update-book-form" onSubmit={handleUpdate}>
                <label className="update-label">
                    Description:
                    <textarea
                        className="update-input"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                    />
                </label>

                <div className="update-numbers">
                    <label className="update-label">
                        Available Copies:
                        <input
                            className="update-input"
                            type="number"
                            value={available_copies}
                            onChange={(e) => setAvailableCopies(e.target.value)}
                        />
                    </label>

                    <label className="update-label">
                        Total Copies:
                        <input
                            className="update-input"
                            type="number"
                            value={total_copies}
                            onChange={(e) => setTotalCopies(e.target.value)}
                        />
                    </label>
                </div>


                <button className="update-button" type="submit">Update Book</button>
            </form>
        </div>
    );
}

export default UpdateBookModal;