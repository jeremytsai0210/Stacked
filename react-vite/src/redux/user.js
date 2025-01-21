const LOAD_USERS = 'users/LOAD_USERS';
const UPDATE_USER = 'users/UPDATE_USER';
// const DELETE_USER = 'users/DELETE_USER'; 
// maybe later if we want to implement admin delete user, it can be use to deactivate accounts or something.

// Action Creators
const loadUsers = (users) => ({
    type: LOAD_USERS,
    payload: users,
});

const updateUser = (user) => ({
    type: UPDATE_USER,
    payload: user,
});

// Action Thunks
export const thunkGetUsers = () => async (dispatch) => {
    const response = await fetch('/api/users');
    if (response.ok) {
        const data = await response.json();
        dispatch(loadUsers(data.users));
    }
};

export const thunkUpdateUser = (user) => async (dispatch) => {
    const response = await fetch(`/api/users/${user.id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(updateUser(data.user));
        return data;
    }
};

// Reducer
const initialState = {};

const usersReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_USERS: {
            const newState = {};
            action.payload.forEach((user) => {
                newState[user.id] = user;
            });
            return newState;
        }

        case UPDATE_USER:
            return { ...state, [action.payload.id]: action.payload };

        default:
            return state;
    }
}

export default usersReducer;