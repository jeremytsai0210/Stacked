import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import * as borrowingTransactionActions from '../../redux/borrowing_transaction';

function BorrowingTransactions() {
    const dispatch = useDispatch();

    const borrowingTransactions = useSelector((state) => Object.values(state.borrowingTransactions));
    const user = useSelector((state) => state.session.user);

    useEffect(() => {
        if(!user || !user.is_admin) {
            dispatch(borrowingTransactionActions.thunkGetTransactions());
        }
    }, [dispatch, user]);

    return (
        <div>
            <h1>Borrowing Transactions</h1>
            <table>
                <thead>
                    <tr>
                        <th>User</th>
                        <th>Book</th>
                        <th>Start Date</th>
                        <th>End Date</th>
                        <th>Return Date</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {borrowingTransactions.map((borrowingTransaction) => (
                        <tr key={borrowingTransaction.id}>
                            <td>{borrowingTransaction.user.username}</td>
                            <td>{borrowingTransaction.book.title}</td>
                            <td>{borrowingTransaction.borrow_date}</td>
                            <td>{borrowingTransaction.due_date}</td>
                            <td>{borrowingTransaction.return_date}</td>
                            <td>{borrowingTransaction.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default BorrowingTransactions;