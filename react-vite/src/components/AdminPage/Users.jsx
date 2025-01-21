import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import * as userActions from '../../redux/user';

function Users() {
    const dispatch = useDispatch();

    const users = useSelector((state) => Object.values(state.users));

    useEffect(() => {
        dispatch(userActions.thunkGetUsers());
    }, [dispatch]);
    
    console.log("THIS IS FROM USERS");
    console.log('users', users);

    return (
        <div>
            <h1>Users</h1>
            <table>
                <thead>
                    <tr>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Username</th>
                        <th>Email</th>
                        <th>Tier</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map((user) => (
                        <tr key={user.id}>
                            <td>{user.first_name}</td>
                            <td>{user.last_name}</td>
                            <td>{user.username}</td>
                            <td>{user.email}</td>
                            <td>{user.tier}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Users;