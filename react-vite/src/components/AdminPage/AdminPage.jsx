import { useState } from 'react';
import { useSelector } from 'react-redux';
import Books from './Books';
import Users from './Users';
import Reviews from './Reviews';
import Transactions from './BorrowingTransactions';
import './AdminPage.css';

function AdminPage() {
    const user = useSelector((state) => state.session.user);
    const [activeTab, setActiveTab] = useState('users');
    
    if (!user || !user.is_admin) {
        return <h1>Unauthorized</h1>;
    }

    const renderContent = () => {
        switch (activeTab) {
            case 'library':
                return (
                    <Users />
                );

            case 'reviews':
                return (
                    <Reviews />
                );

            case 'transactions':
                return (
                    <Transactions />
                );

            case 'books':
                return (
                    <Books />
                );

            default:
                return (
                    <Users />
                );
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