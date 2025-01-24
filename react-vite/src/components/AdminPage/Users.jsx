import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import * as userActions from '../../redux/user';
import './Table.css';

function Users() {
    const dispatch = useDispatch();

    const users = useSelector((state) => Object.values(state.users));

    useEffect(() => {
        dispatch(userActions.thunkGetUsers());
    }, [dispatch]);
    
    // console.log("THIS IS FROM USERS");
    // console.log('users', users);

    return (
        <div className="admin-components">
            <h1 className="title">Users</h1>
            <table className="table">
                <thead className="table-header">
                    <tr className="table-columns-header">
                        <th className="table-column-name">First Name</th>
                        <th className="table-column-name">Last Name</th>
                        <th className="table-column-name">Username</th>
                        <th className="table-column-name">Email</th>
                        <th className="table-column-name">Tier</th>
                    </tr>
                </thead>
                <tbody className="table-body">
                    {users.map((user) => (
                        <tr key={user.id} className="table-row">
                            <td className="table-cell">{user.first_name}</td>
                            <td className="table-cell">{user.last_name}</td>
                            <td className="table-cell">{user.username}</td>
                            <td className="table-cell">{user.email}</td>
                            <td className="table-cell">{user.tier}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Users;
