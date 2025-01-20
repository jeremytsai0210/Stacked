const LOAD_TRANSACTIONS = 'borrowing_transaction/loadTransactions';
const LOAD_USER_TRANSACTIONS = 'borrowing_transaction/loadUserTransactions';
const LOAD_BOOK_TRANSACTIONS = 'borrowing_transaction/loadBookTransactions';
const LOAD_SINGLE_TRANSACTION = 'borrowing_transaction/loadSingleTransaction';
const ADD_TRANSACTION = 'borrowing_transaction/addTransaction';
const UPDATE_TRANSACTION = 'borrowing_transaction/updateTransaction';
const DELETE_TRANSACTION = 'borrowing_transaction/deleteTransaction';

// Action Creators
const loadTransactions = (transactions) => ({
    type: LOAD_TRANSACTIONS,
    payload: transactions,
});

const loadUserTransactions = (transactions) => ({
    type: LOAD_USER_TRANSACTIONS,
    payload: transactions,
});

const loadBookTransactions = (transactions) => ({
    type: LOAD_BOOK_TRANSACTIONS,
    payload: transactions,
});

const loadSingleTransaction = (transaction) => ({
    type: LOAD_SINGLE_TRANSACTION,
    payload: transaction,
});

const addTransaction = (transaction) => ({
    type: ADD_TRANSACTION,
    payload: transaction,
});

const updateTransaction = (transaction) => ({
    type: UPDATE_TRANSACTION,
    payload: transaction,
});

const deleteTransaction = (transactionId) => ({
    type: DELETE_TRANSACTION,
    payload: transactionId,
});

// Action Thunks
export const thunkGetTransactions = () => async (dispatch) => {
    const response = await fetch('/api/borrowing_transactions');
    if (response.ok) {
        const data = await response.json();
        dispatch(loadTransactions(data.borrowing_transactions));
    }
};

export const thunkGetUserTransactions = (userId) => async (dispatch) => {
    const response = await fetch(`/api/borrowing_transactions/user/${userId}`);
    if (response.ok) {
        const data = await response.json();
        dispatch(loadUserTransactions(data.borrowing_transactions));
    }
}

export const thunkGetBookTransactions = (bookId) => async (dispatch) => {
    const response = await fetch(`/api/borrowing_transactions/book/${bookId}`);
    if (response.ok) {
        const data = await response.json();
        dispatch(loadBookTransactions(data.borrowing_transactions));
    }
}

export const thunkGetSingleTransaction = (transactionId) => async (dispatch) => {
    const response = await fetch(`/api/borrowing_transactions/${transactionId}`);
    if (response.ok) {
        const data = await response.json();
        dispatch(loadSingleTransaction(data.borrowing_transaction));
    }
}

export const thunkAddTransaction = (transaction) => async (dispatch) => {
    const response = await fetch('/api/borrowing_transactions/new', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(transaction),
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(addTransaction(data.borrowing_transaction));
    }
}

export const thunkUpdateTransaction = (transaction) => async (dispatch) => {
    const response = await fetch(`/api/borrowing_transactions/${transaction.id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(transaction),
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(updateTransaction(data.borrowing_transaction));
    }
}

export const thunkDeleteTransaction = (transactionId) => async (dispatch) => {
    const response = await fetch(`/api/borrowing_transactions/${transactionId}`, {
        method: 'DELETE',
    });
    if (response.ok) {
        dispatch(deleteTransaction(transactionId));
    }
}

const initialState = {};

// Reducer
const borrowingTransactionsReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_TRANSACTIONS: {
            const newState = {};
            action.payload.forEach((transaction) => {
                newState[transaction.id] = transaction;
            });
            return newState;
        }

        case LOAD_USER_TRANSACTIONS: {
            const newState = {};
            action.payload.forEach((transaction) => {
                newState[transaction.id] = transaction;
            });
            return newState;
        }

        case LOAD_BOOK_TRANSACTIONS: {
            const newState = {};
            action.payload.forEach((transaction) => {
                newState[transaction.id] = transaction;
            });
            return newState;
        }

        case LOAD_SINGLE_TRANSACTION:
            return { ...state, [action.payload.id]: action.payload };

        case ADD_TRANSACTION:
            return { ...state, [action.payload.id]: action.payload };

        case UPDATE_TRANSACTION:
            return { ...state, [action.payload.id]: action.payload };

        case DELETE_TRANSACTION: {
            const newState = { ...state };
            delete newState[action.payload];
            return newState;
        }
            
        default:
            return state;
    }
}

export default borrowingTransactionsReducer;