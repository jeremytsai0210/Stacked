const LOAD_DEFAULT_AVATARS = 'avatar/loadDefaultAvatars';
const LOAD_USER_AVATARS = 'avatar/loadUserAvatars';
const ADD_AVATAR = 'avatar/addAvatar';
const UPDATE_AVATAR = 'avatar/updateAvatar';
const DELETE_AVATAR = 'avatar/deleteAvatar';

// Action Creators
const loadDefaultAvatars = (avatars) => ({
    type: LOAD_DEFAULT_AVATARS,
    payload: avatars,
});

const loadUserAvatars = (avatars) => ({
    type: LOAD_USER_AVATARS,
    payload: avatars,
});

const addAvatar = (avatar) => ({
    type: ADD_AVATAR,
    payload: avatar,
});

const updateAvatar = (avatar) => ({
    type: UPDATE_AVATAR,
    payload: avatar,
});

const deleteAvatar = (avatarId) => ({
    type: DELETE_AVATAR,
    payload: avatarId,
});

// Action Thunks
export const thunkGetDefaultAvatars = () => async (dispatch) => {
    const response = await fetch('/api/avatars');
    if (response.ok) {
        const data = await response.json();
        dispatch(loadDefaultAvatars(data.avatars));
    }
};

export const thunkGetUserAvatars = (userId) => async (dispatch) => {
    const response = await fetch(`/api/avatars/user/${userId}`);
    if (response.ok) {
        const data = await response.json();
        dispatch(loadUserAvatars(data.avatars));
    }
}

export const thunkAddAvatar = (avatar) => async (dispatch) => {
    const response = await fetch('/api/avatars/new', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(avatar),
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(addAvatar(data.avatar));
    }
}

export const thunkUpdateAvatar = (avatar) => async (dispatch) => {
    const response = await fetch(`/api/avatars/${avatar.id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(avatar),
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(updateAvatar(data.avatar));
    }
}

export const thunkDeleteAvatar = (avatarId) => async (dispatch) => {
    const response = await fetch(`/api/avatars/${avatarId}`, {
        method: 'DELETE',
    });
    if (response.ok) {
        dispatch(deleteAvatar(avatarId));
    }
}

const initialState = {
    defaultAvatars: {},
    userAvatars: {},
};

// Reducer
const avatarsReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_DEFAULT_AVATARS:
            const defaultAvatars = {};
            action.payload.forEach((avatar) => {
                defaultAvatars[avatar.id] = avatar;
            });
            return { ...state, defaultAvatars };

        case LOAD_USER_AVATARS:
            const userAvatars = {};
            action.payload.forEach((avatar) => {
                userAvatars[avatar.id] = avatar;
            });
            return { ...state, userAvatars };

        case ADD_AVATAR:
            return { ...state, userAvatars: { ...state.userAvatars, [action.payload.id]: action.payload } };

        case UPDATE_AVATAR:
            return { ...state, userAvatars: { ...state.userAvatars, [action.payload.id]: action.payload } };

        case DELETE_AVATAR:
            const updatedUserAvatars = { ...state.userAvatars };
            delete updatedUserAvatars[action.payload];
            return { ...state, userAvatars: updatedUserAvatars };
            
        default:
            return state;
    }
};

export default avatarsReducer;
