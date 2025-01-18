import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';
import * as bookActions from '../../redux/book';
import './BookDetailPage.css';

function BookDetailPage() {
    const dispatch = useDispatch();
    const { bookId } = useParams();

    const book = useSelector((state) => state.books[bookId]);

    useEffect(() => {
        dispatch(bookActions.thunkGetSingleBook(bookId));
    }, [dispatch, bookId]);

    return (
        <div className="book-detail">
            <h1>{book?.title}</h1>
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
                    <button
                        className="borrow-button"
                        disabled={book?.available_copies === 0}
                        onClick={() => alert('Borrow button clicked!')}
                    >
                        Borrow
                    </button>
                </div>
            </div>
        </div>
    );
}

export default BookDetailPage;