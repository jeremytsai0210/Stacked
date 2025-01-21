const LOAD_BOOKS = 'books/loadBooks';
const LOAD_USER_BOOKS = 'books/loadUserBooks';
const LOAD_SINGLE_BOOK = 'books/loadSingleBook';
const ADD_BOOK = 'books/addBook';
const UPDATE_BOOK = 'books/updateBook';
const DELETE_BOOK = 'books/deleteBook';

// Action Creators
const loadBooks = (books) => ({
    type: LOAD_BOOKS,
    payload: books,
});

const loadUserBooks = (books) => ({
    type: LOAD_USER_BOOKS,
    payload: books,
});

const loadSingleBook = (book) => ({
    type: LOAD_SINGLE_BOOK,
    payload: book,
});

const addBook = (book) => ({
    type: ADD_BOOK,
    payload: book,
});

const updateBook = (book) => ({
    type: UPDATE_BOOK,
    payload: book,
});

const deleteBook = (bookId) => ({
    type: DELETE_BOOK,
    payload: bookId,
});

// Action Thunks
export const thunkGetBooks = () => async (dispatch) => {
    const response = await fetch('/api/books');
    if (response.ok) {
        const data = await response.json();
        dispatch(loadBooks(data.books));
    }
};

export const thunkGetUserBooks = (userId) => async (dispatch) => {
    const response = await fetch(`/api/books/user/${userId}`);
    if (response.ok) {
        const data = await response.json();
        dispatch(loadUserBooks(data.books));
    }
}

export const thunkGetSingleBook = (bookId) => async (dispatch) => {
    const response = await fetch(`/api/books/${bookId}`);
    if (response.ok) {
        const data = await response.json();
        dispatch(loadSingleBook(data.book));
    }
};

export const thunkAddBook = (book) => async (dispatch) => {
    console.log("before response");
    console.log("book", book);

    const response = await fetch('/api/books', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(book),
    });

    console.log("after response");
    console.log("response", response);

    if (response.ok) {
        const data = await response.json();
        dispatch(addBook(data.book));
    }
};

export const thunkUpdateBook = (book) => async (dispatch) => {
    const response = await fetch(`/api/books/${book.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(book),
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(updateBook(data.book));
    }
};

export const thunkDeleteBook = (bookId) => async (dispatch) => {
    const response = await fetch(`/api/books/${bookId}`, {
        method: 'DELETE',
    });

    if (response.ok) {
        dispatch(deleteBook(bookId));
    }
};

// Initial State
const initialState = {};

// Reducer
export default function booksReducer(state = initialState, action) {
    switch (action.type) {
        case LOAD_BOOKS: {
            const newState = {};
            action.payload.forEach((book) => {
                newState[book.id] = book;
            });
            return newState;
        }

        case LOAD_USER_BOOKS: {
            const newState = {};
            action.payload.forEach((book) => {
                newState[book.id] = book;
            });
            return newState;
        }

        case LOAD_SINGLE_BOOK:
            return { ...state, [action.payload.id]: action.payload };

        case ADD_BOOK:
            return { ...state, [action.payload.id]: action.payload };

        case UPDATE_BOOK:
            return { ...state, [action.payload.id]: action.payload };

        case DELETE_BOOK: {
                const newState = { ...state };
                delete newState[action.payload];
                return newState;
            }

        default:
            return state;
    }
}
