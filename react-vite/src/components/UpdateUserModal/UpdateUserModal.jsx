import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useModal } from '../../context/Modal';
import * as userActions from '../../redux/user';
import './UpdateUserModal.css';

function UpdateUserModal(user) {
    const dispatch = useDispatch();
    const [username, setUsername] = useState('');
    const [first_name, setFirstName] = useState('');
    const [last_name, setLastName] = useState('');
    const [errors, setErrors] = useState(null);

    const { closeModal } = useModal();

    const handleUpdate = (e) => {
        e.preventDefault();

        setErrors({});

        if (!username) {
            setErrors('Username cannot be empty');
            return;
        }

        if (!first_name) {
            setErrors('First name cannot be empty');
            return;
        }

        if (!last_name) {
            setErrors('Last name cannot be empty');
            return;
        }

        const updatedUser = {
            ...user.user,
            username,
            first_name,
            last_name,
        }

        setErrors(null);

        dispatch(userActions.thunkUpdateUser(updatedUser));
        closeModal();
        location.reload();
    }

    return (
        <div className="update-user-modal">
            <h2>Update My Profile</h2>
            {errors && <p className="error">{errors}</p>}

            <form onSubmit={handleUpdate}>
                <div className="update-form-group">
                    <label htmlFor="username">Username </label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </div>
                <div className="update-form-group">
                    <label htmlFor="first_name">First Name </label>
                    <input
                        type="text"
                        id="first_name"
                        value={first_name}
                        onChange={(e) => setFirstName(e.target.value)}
                    />
                </div>
                <div className="update-form-group">
                    <label htmlFor="last_name">Last Name </label>
                    <input
                        type="text"
                        id="last_name"
                        value={last_name}
                        onChange={(e) => setLastName(e.target.value)}
                    />
                </div>
                <button type="submit">Update</button>
            </form>
        </div>
    );
}

export default UpdateUserModal;