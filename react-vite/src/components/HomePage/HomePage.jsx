import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import * as bookActions from '../../redux/book';
import './HomePage.css';

function HomePage() {
    const dispatch = useDispatch();
    const books = useSelector((state) => {
        return Object.values(state.books);
    });

    useEffect(() => {
        dispatch(bookActions.thunkGetBooks());
    }, [dispatch]);

    return (
        <>
            <h1>Home Page</h1>

            <div className="book-grid">
                {books.map((book) => {
                    return (
                        <Link 
                            to={`/books/${book.id}`}
                            key={book.id} 
                            className="book-tile">
                            <h3 className="book-title">{book.title}</h3>
                            <img src={book.cover_image} alt={book.title} className="cover-image"/>
                            <span className="book-information">
                                <p className="book-author">Author: {book.author}</p>
                                <p className="book-genre">{book.genre}</p>
                                <p className="book-year">Year published: {book.published_year}</p>
                            </span>
                        </Link>
                    )
                })}
            </div>
            
        </>
    )
}

export default HomePage;