import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import * as bookActions from '../../redux/book';
import * as reviewActions from '../../redux/review';
// import * as avatarActions from '../../redux/avatar';
import OpenModalButton from '../OpenModalButton';
import UpdateUserModal from '../UpdateUserModal';
import Library from './Library';
import Reviews from './Reviews';
import './UserProfilePage.css';

function UserProfilePage() {
    const dispatch = useDispatch();

    const user = useSelector((state) => state.session.user);
    const books = useSelector((state) => Object.values(state.books));
    const reviews = useSelector((state) => Object.values(state.reviews));
    // const defaultAvatars = useSelector((state) => Object.values(state.avatars.defaultAvatars));
    // const userAvatars = useSelector((state) => state.avatars.userAvatars);

    const [activeTab, setActiveTab] = useState('library');

    console.log('user', user);
    console.log('books', books);
    console.log('reviews', reviews);
    // console.log('defaultAvatars[0].avatar_image', defaultAvatars[0]?.avatar_image);
    // console.log('userAvatars', userAvatars);

    useEffect(() => {
        dispatch(bookActions.thunkGetUserBooks(user.id));
        dispatch(reviewActions.thunkGetUserReviews(user.id));
        // dispatch(avatarActions.thunkGetDefaultAvatars());
        // dispatch(avatarActions.thunkGetUserAvatars(user.id));
    }, [dispatch, user.id]);

    const startDate = new Date(user.updated_at).toLocaleDateString();

    const renderContent = () => {
        switch (activeTab) {
            case 'library':
                return (
                    <Library />
                );

            case 'reviews':
                return (
                    <Reviews />
                );

            default:
                return (
                    <Library />
                );
        }
    }

    return (
        <div className="user-profile">
            
            <div className="user-profile-container">
                <div className="user-header">
                    <h1>Hello {user?.first_name}!</h1>
                    <div className="user-avatar">
                        <img src="https://images.pexels.com/photos/102155/pexels-photo-102155.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="User avatar" />
                    </div>
                </div>

                <div className="user-information">
                    <p>
                        <span className="user-information-label">Name: </span>
                        {user?.first_name} {user?.last_name}
                    </p>
                    <p>
                        <span className="user-information-label">Username: </span>
                        {user?.username}
                    </p>
                    <p>
                        <span className="user-information-label">Email: </span>
                        {user?.email}
                    </p>
                    <p>
                        <span className="user-information-label">Member since: </span>
                        {startDate}
                    </p>
                    <p>
                        <span className="user-information-label">Books borrowed: </span>
                        {books.length}
                    </p>
                </div>

                <hr/>

                <div className="user-actions">
                    <button onClick={() => setActiveTab('library')}>My Library</button>
                    <button onClick={() => setActiveTab('reviews')}>My Reviews</button>
                    <OpenModalButton
                        className="edit-profile-button"
                        buttonText="Edit Profile"
                        modalComponent={<UpdateUserModal user={user}/>}
                    />
                </div>
            </div>

            <div className="user-profile-content">
                {renderContent()}
            </div>
        </div>
    );
}

export default UserProfilePage;