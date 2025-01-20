import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import * as bookActions from '../../redux/book';
import * as borrowingTransactionActions from '../../redux/borrowing_transaction';
import './Library.css';

function Library() {
    const dispatch = useDispatch();

    const user = useSelector((state) => state.session.user);
    const books = useSelector((state) => Object.values(state.books));
    const transactions = useSelector((state) => Object.values(state.borrowingTransactions));
    const state = useSelector((state) => state);

    console.log('state:', state);
    console.log('transactions:', transactions);

    useEffect(() => {
        dispatch(bookActions.thunkGetUserBooks(user.id));
        dispatch(borrowingTransactionActions.thunkGetUserTransactions(user.id));
    }, [dispatch, user.id]);

    return (
        <>
            <h1>My Library</h1>

            <div className="user-book-grid">
                {books.map((book) => {
                    const transaction = transactions.find((transaction) => transaction.book_id === book.id);
                    return (
                        <div className="user-book-block" key={book.id}>
                            <Link 
                                to={`/books/${book.id}`} 
                                className="user-book-tile">
                                <h3 className="user-book-title">{book.title}</h3>
                                <img src={book.cover_image} alt={book.title} className="user-cover-image"/>
                                <span className="user-book-information">
                                    <p className="borrow-date">
                                        Borrow Date: {transaction?.borrow_date}
                                    </p>
                                    <p className="due-date">
                                        Due Date: {transaction?.due_date}
                                    </p>
                                    <p className="status">
                                        Status: {transaction?.status}
                                    </p>
                                </span>
                            </Link>
                            {transaction?.status === 'BORROWED' && (
                                <button className="return-button">Return Book</button>
                            )}
                        </div>
                    )
                })}
            </div>
        </>       
    )
}

export default Library;