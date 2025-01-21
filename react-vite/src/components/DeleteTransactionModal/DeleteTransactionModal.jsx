import { useDispatch } from 'react-redux';
import { useModal } from '../../context/Modal';
import * as borrowingTransactionActions from '../../redux/borrowing_transaction';
import './DeleteTransactionModal.css';

function DeleteTransactionModal(transactionId) {
    const dispatch = useDispatch();

    const { closeModal } = useModal();

    const handleDelete = () => {
        dispatch(borrowingTransactionActions.thunkDeleteTransaction(transactionId.transactionId));
        closeModal();
    }

    return (
        <div className="delete-modal">
            <h2>Delete Transaction</h2>
            <p>Are you sure you want to delete this transaction?</p>
            <div className="delete-buttons">
                <button className="confirm-delete" onClick={handleDelete}>Delete</button>
                <button onClick={closeModal}>Cancel</button>
            </div>
        </div>
    )
}

export default DeleteTransactionModal;