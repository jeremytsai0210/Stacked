import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import * as bookActions from '../../redux/book';
import './Table.css';

function Books() {
    const dispatch = useDispatch();

    const books = useSelector((state) => Object.values(state.books));

    useEffect(() => {
        dispatch(bookActions.thunkGetBooks());
    }, [dispatch]);

    return (
        <div className="admin-components">
            <h1 className="title">Books</h1>
            <table className="table">
                <thead className="table-header">
                    <tr className="table-columns-header">
                        <th className="table-column-name">Title</th>
                        <th className="table-column-name">Author</th>
                        <th className="table-column-name">Genre</th>
                        <th className="table-column-name">Published Year</th>
                        <th className="table-column-name">Description</th>
                        <th className="table-column-name">Available Copies</th>
                        <th className="table-column-name">Total Copies</th>
                    </tr>
                </thead>
                <tbody className="table-body">
                    {books.map((book) => (
                        <tr key={book.id} className="table-row">
                            <td className="table-cell">{book.title}</td>
                            <td className="table-cell">{book.author}</td>
                            <td className="table-cell">{book.genre}</td>
                            <td className="table-cell">{book.published_year}</td>
                            <td className="table-cell">{book.description}</td>
                            <td className="table-cell">{book.available_copies}</td>
                            <td className="table-cell">{book.total_copies}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Books;