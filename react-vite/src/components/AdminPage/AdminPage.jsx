import { useState } from 'react';
import { useSelector } from 'react-redux';
import Books from './Books';
import Users from './Users';
import Reviews from './Reviews';
import Transactions from './BorrowingTransactions';
import './AdminPage.css';

function AdminPage() {
    const state = useSelector((state) => state);
    const current_user = useSelector((state) => state.session.user);

    const [activeTab, setActiveTab] = useState('users');
    
    if (!current_user || !current_user.is_admin) {
        return <h1>Unauthorized</h1>;
    }

    // console.log("THIS IS FROM ADMINPAGE");
    // console.log('current_user', current_user);
    // console.log('state', state);
    // console.log("THIS IS END OF ADMINPAGE");

    const renderContent = () => {
        switch (activeTab) {
            case 'users':
                return <Users />;

            case 'books':
                return <Books />;

            case 'transactions':
                return <Transactions />;

            case 'reviews':
                return <Reviews />;
        }
    }

    return (
        <div>
            <div className="admin-nav">
                <button onClick={() => setActiveTab('users')}>Users</button>
                <button onClick={() => setActiveTab('books')}>Books</button>
                <button onClick={() => setActiveTab('transactions')}>Transactions</button>
                <button onClick={() => setActiveTab('reviews')}>Reviews</button>
            </div>

            <div className="admin-content">
                {renderContent()}
            </div>
        </div>
    );
}

export default AdminPage;