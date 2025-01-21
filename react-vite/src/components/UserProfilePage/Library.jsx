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
    const allUserTransactions = useSelector((state) => Object.values(state.borrowingTransactions));
    // const state = useSelector((state) => state);

    // console.log('state:', state);
    // console.log('allUserTransactions:', allUserTransactions);

    const openTransactions = allUserTransactions.filter((transaction) => transaction.status === 'BORROWED');

    // console.log('openTransactions:', openTransactions);

    useEffect(() => {
        dispatch(bookActions.thunkGetUserBooks(user.id));
        dispatch(borrowingTransactionActions.thunkGetUserTransactions(user.id));
    }, [dispatch, user.id]);

    const formatDate = (dateString) => {
        const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
        const date = new Date(dateString);
        date.setHours(12);
        return date.toLocaleDateString(undefined, options);
    };

    const handleBorrowClick = async (transactionID) => {
        try {
            await dispatch(borrowingTransactionActions.thunkUpdateTransaction(transactionID));
            alert('Book returned successfully!');
            location.reload();
        } catch (error) {
            console.error('Error returning book:', error);
            alert('Error returning book. Please try again.');
        }
    }

    return (
        <>
            <h1>My Library</h1>

            <div className="user-book-grid">
                {books.map((book) => {
                    const transaction = openTransactions.find((transaction) => transaction.book_id === book.id);
                    

                    return (
                        <div className="user-book-block" key={book.id}>
                            <div className="user-book-tile">
                                <Link 
                                    to={`/books/${book.id}`}
                                    className="user-book-link"
                                >
                                    <h3 className="user-book-title">{book.title}</h3>
                                    <img src={book.cover_image} alt={book.title} className="user-cover-image"/>
                                </Link>
                                <span className="user-book-information">
                                    <p className="borrow-date">
                                        <span className="book-label">Borrow Date:</span> 
                                        <span className="book-label-information">{transaction ? formatDate(transaction.borrow_date) : 'N/A'}</span>
                                    </p>
                                    <p className="due-date">
                                        <span className="book-label">Due Date:</span>
                                        <span className="book-label-information">{transaction ? formatDate(transaction.due_date) : 'N/A'}</span>
                                    </p>
                                    <p className="status">
                                        Status: {transaction?.status}
                                    </p>
                                </span>
                            </div>
                            <button 
                                className="return-button"
                                onClick={() => handleBorrowClick(transaction.id)}
                            >Return Book</button>
                        </div>
                    )
                })}
            </div>
        </>       
    )
}

export default Library;