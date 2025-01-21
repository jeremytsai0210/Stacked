import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import * as reviewActions from '../../redux/review';
import './Table.css';

function Reviews() {
    const dispatch = useDispatch();

    const reviews = useSelector((state) => Object.values(state.reviews));

    useEffect(() => {
        dispatch(reviewActions.thunkGetReviews());
    }, [dispatch]);

    return (
        <div className="admin-components">
            <h1 className="title">Reviews</h1>
            <table className="table">
                <thead className="table-header">
                    <tr className="table-columns-header">
                        <th className="table-column-name">User</th>
                        <th className="table-column-name">Book</th>
                        <th className="table-column-name">Stars</th>
                        <th className="table-column-name">Review</th>
                    </tr>
                </thead>
                <tbody className="table-body">
                    {reviews.map((review) => (
                        <tr key={review.id} className="table-row">
                            <td className="table-cell">{review.user.username}</td>
                            <td className="table-cell">{review.book.title}</td>
                            <td className="table-cell">{review.stars}</td>
                            <td className="table-cell">{review.review_text}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Reviews;
