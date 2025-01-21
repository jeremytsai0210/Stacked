import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import * as reviewActions from '../../redux/review';

function Reviews() {
    const dispatch = useDispatch();

    const reviews = useSelector((state) => Object.values(state.reviews));

    console.log('reviews', reviews);

    useEffect(() => {
        dispatch(reviewActions.thunkGetReviews());
    }, [dispatch]);

    return (
        <div>
            <h1>Reviews</h1>
            <table>
                <thead>
                    <tr>
                        <th>User</th>
                        <th>Book</th>
                        <th>Stars</th>
                        <th>Review</th>
                    </tr>
                </thead>
                <tbody>
                    {reviews.map((review) => (
                        <tr key={review.id}>
                            <td>{review.user.username}</td>
                            <td>{review.book.title}</td>
                            <td>{review.stars}</td>
                            <td>{review.review_text}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Reviews;