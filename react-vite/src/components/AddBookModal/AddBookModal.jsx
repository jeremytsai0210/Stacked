import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useModal } from '../../context/Modal';
import * as bookActions from '../../redux/book';
import './AddBookModal.css';

function AddBookModal() {
    const dispatch = useDispatch();
    const [title, setTitle] = useState('');
    const [author, setAuthor] = useState('');
    const [description, setDescription] = useState('');
    const [genre, setGenre] = useState('');
    const [coverImage, setCoverImage] = useState('');
    const [totalCopies, setTotalCopies] = useState('');
    const [availableCopies, setAvailableCopies] = useState('');
    const [publishedYear, setPublishedYear] = useState('');
    const [errors, setErrors] = useState([]);

    const { closeModal } = useModal();

    // Handle form submission
    const handleAddBook = async (e) => {
        e.preventDefault();
    
        // Clear previous errors
        setErrors({
            title: '',
            author: '',
            description: '',
            genre: '',
            coverImage: '',
            totalCopies: '',
            availableCopies: '',
            publishedYear: ''
        });
    
        const validationErrors = {};
    
        if (!title) validationErrors.title = 'Title is required.';
        if (!author) validationErrors.author = 'Author is required.';
        if (!description) validationErrors.description = 'Description is required.';
        if (!genre) validationErrors.genre = 'Genre is required.';
        if (!totalCopies || totalCopies <= 0) validationErrors.totalCopies = 'Total copies must be a positive number.';
        if (!availableCopies || availableCopies < 0) validationErrors.availableCopies = 'Available copies must be 0 or a positive number.';
        if (!publishedYear || publishedYear.length !== 4) validationErrors.publishedYear = 'Published year must be a valid year (4 digits).';
        if (parseInt(availableCopies, 10) > parseInt(totalCopies, 10)) validationErrors.availableCopies = 'Available copies cannot be greater than total copies.';
    
        if (Object.keys(validationErrors).length > 0) {
            setErrors(validationErrors);
            return;
        }
    
        // Dispatch action to add book
        const newBook = {
            title,
            author,
            description,
            genre,
            cover_image: coverImage,
            total_copies: parseInt(totalCopies, 10),
            available_copies: parseInt(availableCopies, 10),
            published_year: parseInt(publishedYear, 10),
        };
    
        await dispatch(bookActions.thunkAddBook(newBook));
        closeModal();  // Close the modal after successful submission
    };
    
    return (
        <div className="add-book-modal">
            <h2>Add a Book</h2>
            {errors.length > 0 && (
                <div className="error">
                    <ul>
                        {errors.map((error, idx) => (
                            <li key={idx}>{error}</li>
                        ))}
                    </ul>
                </div>
            )}

            <form className="add-book-form" onSubmit={handleAddBook}>
                <div className="add-book-form-group">
                    <input
                        placeholder="Title"
                        type="text"
                        id="title"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        required
                    />
                    {errors.title && <p className="error">{errors.title}</p>}

                    <input
                        placeholder="Author"
                        type="text"
                        id="author"
                        value={author}
                        onChange={(e) => setAuthor(e.target.value)}
                        required
                    />
                    {errors.author && <p className="error">{errors.author}</p>}

                    <textarea
                        placeholder="Description"
                        id="description"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        required
                    />
                    {errors.description && <p className="error">{errors.description}</p>}

                    <select
                        id="genre"
                        value={genre}
                        onChange={(e) => setGenre(e.target.value)}
                    >
                        <option value="">Select Genre</option>
                        <option value="FICTION">Fiction</option>
                        <option value="NON_FICTION">Non-Fiction</option>
                        <option value="FANTASY">Fantasy</option>
                        <option value="SCIENCE_FICTION">Science Fiction</option>
                        <option value="MYSTERY">Mystery</option>
                        <option value="HORROR">Horror</option>
                        <option value="ROMANCE">Romance</option>
                        <option value="THRILLER">Thriller</option>
                        <option value="HISTORICAL_FICTION">Historical Fiction</option>
                        <option value="BIOGRAPHY">Biography</option>
                        <option value="AUTOBIOGRAPHY">Auto Biography</option>
                        <option value="SELF_HELP">Self Help</option>
                        <option value="COOKBOOK">Cookbook</option>
                        <option value="POETRY">Poetry</option>
                        <option value="GRAPHIC_NOVEL">Graphic Novel</option>
                        <option value="COMIC_BOOK">Comic Book</option>
                        <option value="OTHER">Other</option>
                    </select>
                    {errors.genre && <p className="error">{errors.genre}</p>}

                    <input
                        placeholder="Cover Image URL"
                        type="text"
                        id="coverImage"
                        value={coverImage}
                        onChange={(e) => setCoverImage(e.target.value)}
                    />
                    {errors.coverImage && <p className="error">{errors.coverImage}</p>}

                    <div className="book-copies">
                        <input
                            placeholder="Total Copies"
                            type="number"
                            id="totalCopies"
                            value={totalCopies}
                            onChange={(e) => setTotalCopies(e.target.value)}
                        />

                        <input
                            placeholder="Available Copies"
                            type="number"
                            id="availableCopies"
                            value={availableCopies}
                            onChange={(e) => setAvailableCopies(e.target.value)}
                        />
                    </div>
                    {errors.totalCopies && <p className="error">{errors.totalCopies}</p>}
                    {errors.availableCopies && <p className="error">{errors.availableCopies}</p>}

                    <input
                        placeholder="Published Year"
                        type="text"
                        id="publishedYear"
                        value={publishedYear}
                        onChange={(e) => setPublishedYear(e.target.value)}
                    />
                    {errors.publishedYear && <p className="error">{errors.publishedYear}</p>}

                    <button type="submit" className="submit-button">Add Book</button>
                </div>
            </form>

        </div>
    );
}

export default AddBookModal;

/*
Sample Data:
Title: Lord of the Flies
Author: William Golding
Description: The plot concerns a group of British boys who are stranded on an uninhabited island and their disastrous attempts to govern themselves. The novel's themes include morality, leadership, and the tension between civility and chaos.
Genre: FICTION
Cover Image URL: https://plus.unsplash.com/premium_photo-1664303959273-21d18b87b88a?q=80&w=2061&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
Total Copies: 10
Available Copies: 10
Published Year: 1954
*/