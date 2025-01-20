const LOAD_REVIEWS = 'reviews/loadReviews';
const LOAD_USER_REVIEWS = 'reviews/loadUserReviews';
const LOAD_BOOK_REVIEWS = 'reviews/loadBookReviews';
const LOAD_SINGLE_REVIEW = 'reviews/loadSingleReview';
const ADD_REVIEW = 'reviews/addReview';
const UPDATE_REVIEW = 'reviews/updateReview';
const DELETE_REVIEW = 'reviews/deleteReview';

// Action Creators
const loadReviews = (reviews) => ({
    type: LOAD_REVIEWS,
    payload: reviews,
});

const loadUserReviews = (reviews) => ({
    type: LOAD_USER_REVIEWS,
    payload: reviews,
});

const loadBookReviews = (reviews) => ({
    type: LOAD_BOOK_REVIEWS,
    payload: reviews,
});

const loadSingleReview = (review) => ({
    type: LOAD_SINGLE_REVIEW,
    payload: review,
});

const addReview = (review) => ({
    type: ADD_REVIEW,
    payload: review,
});

const updateReview = (review) => ({
    type: UPDATE_REVIEW,
    payload: review,
});

const deleteReview = (reviewId) => ({
    type: DELETE_REVIEW,
    payload: reviewId,
});

// Action Thunks
export const thunkGetReviews = () => async (dispatch) => {
    const response = await fetch('/api/reviews');
    if (response.ok) {
        const data = await response.json();
        dispatch(loadReviews(data.reviews));
    }
};

export const thunkGetUserReviews = (userId) => async (dispatch) => {
    const response = await fetch(`/api/reviews/user/${userId}`);
    if (response.ok) {
        const data = await response.json();
        dispatch(loadUserReviews(data.reviews));
    }
}

export const thunkGetBookReviews = (bookId) => async (dispatch) => {
    const response = await fetch(`/api/reviews/book/${bookId}`);
    if (response.ok) {
        const data = await response.json();
        dispatch(loadBookReviews(data.reviews));
    }
}

export const thunkGetSingleReview = (reviewId) => async (dispatch) => {
    const response = await fetch(`/api/reviews/${reviewId}`);
    if (response.ok) {
        const data = await response.json();
        dispatch(loadSingleReview(data.review));
    }
}

export const thunkAddReview = (review, bookId) => async (dispatch) => {
    const response = await fetch(`/api/books/${bookId}/review`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(review),
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(addReview(data.review));
        return data;
    }
}

export const thunkUpdateReview = (review) => async (dispatch) => {
    const response = await fetch(`/api/reviews/${review.id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(review),
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(updateReview(data.review));
        return data;
    }
}

export const thunkDeleteReview = (reviewId) => async (dispatch) => {
    const response = await fetch(`/api/reviews/${reviewId}`, {
        method: 'DELETE',
    });

    if (response.ok) {
        dispatch(deleteReview(reviewId));
    }
}

// Reducer
const initialState = {};

export default function reviewsReducer(state = initialState, action) {
    switch (action.type) {
        case LOAD_REVIEWS: {
            const newState = {};
            action.payload.forEach((review) => {
                newState[review.id] = review;
            });
            return newState;
        }

        case LOAD_USER_REVIEWS: {
            const newState = {};
            action.payload.forEach((review) => {
                newState[review.id] = review;
            });
            return newState;
        }

        case LOAD_BOOK_REVIEWS: {
            const newState = {};
            action.payload.forEach((review) => {
                newState[review.id] = review;
            });
            return newState;
        }

        case LOAD_SINGLE_REVIEW:
            return { ...state, [action.payload.id]: action.payload };

        case ADD_REVIEW:
            return { ...state, [action.payload.id]: action.payload };

        case UPDATE_REVIEW:
            return { ...state, [action.payload.id]: action.payload };

        case DELETE_REVIEW: {
            const newState = { ...state };
            delete newState[action.payload];
            return newState;
        }

        default:
            return state;
    }
}