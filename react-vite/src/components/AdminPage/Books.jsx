import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import * as bookActions from '../../redux/book';
// import './Books.css';

function Books() {
    const dispatch = useDispatch();

    const books = useSelector((state) => Object.values(state.books));

    useEffect(() => {
        dispatch(bookActions.thunkGetBooks());
    }, [dispatch]);

    return (
        <div>
            <h1>Books</h1>
            <table>
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Author</th>
                        <th>Genre</th>
                        <th>Published Year</th>
                        <th>Description</th>
                        <th>Available Copies</th>
                        <th>Total Copies</th>
                    </tr>
                </thead>
                <tbody>
                    {books.map((book) => (
                        <tr key={book.id}>
                            <td>{book.title}</td>
                            <td>{book.author}</td>
                            <td>{book.genre}</td>
                            <td>{book.published_year}</td>
                            <td>{book.description}</td>
                            <td>{book.available_copies}</td>
                            <td>{book.total_copies}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Books;