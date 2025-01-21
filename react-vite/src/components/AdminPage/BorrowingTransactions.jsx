import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import * as borrowingTransactionActions from '../../redux/borrowing_transaction';
// import FaTrash from 'react-icons/fa6';
import './Table.css';

function BorrowingTransactions() {
    const dispatch = useDispatch();

    const borrowingTransactions = useSelector((state) => Object.values(state.borrowingTransactions));

    useEffect(() => {
        dispatch(borrowingTransactionActions.thunkGetTransactions());
    }, [dispatch]);

    // Function to handle delete button click (alert for now)
    const handleDeleteClick = (transactionId) => {
        alert(`Transaction with ID ${transactionId} will be deleted`);
        // Here, you could dispatch an action to delete the transaction later
    };

    return (
        <div className="admin-components">
            <h1 className="title">Borrowing Transactions</h1>
            <table className="table">
                <thead className="table-header">
                    <tr className="table-columns-header">
                        <th className="table-column-name">User</th>
                        <th className="table-column-name">Book</th>
                        <th className="table-column-name">Start Date</th>
                        <th className="table-column-name">End Date</th>
                        <th className="table-column-name">Return Date</th>
                        <th className="table-column-name">Status</th>
                        <th className="table-column-name"></th>
                    </tr>
                </thead>
                <tbody className="table-body">
                    {borrowingTransactions.map((borrowingTransaction) => (
                        <tr key={borrowingTransaction.id} className="table-row">
                            <td className="table-cell">{borrowingTransaction.user.username}</td>
                            <td className="table-cell">{borrowingTransaction.book.title}</td>
                            <td className="table-cell">{borrowingTransaction.borrow_date}</td>
                            <td className="table-cell">{borrowingTransaction.due_date}</td>
                            <td className="table-cell">{borrowingTransaction.return_date}</td>
                            <td className="table-cell">{borrowingTransaction.status}</td>
                            <td className="table-cell">
                                <span 
                                    onClick={() => alert(`Book with ID ${book.id} will be deleted`)}>
                                    <FaTrash className="delete-button" />
                                </span>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default BorrowingTransactions;
