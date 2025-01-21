import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import './AdminPage.css';

function AdminPage() {
    const dispatch = useDispatch();
    const user = useSelector((state) => state.session.user);

    if (!user || !user.is_admin) {
        return <h1>Unauthorized</h1>;
    }

    return (
        <div>
            <h1>Admin Page</h1>
        </div>
    );
}

export default AdminPage;