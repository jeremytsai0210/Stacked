import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import HomePage from '../components/HomePage';
import BookDetailPage from '../components/BookDetailPage';
import UserProfilePage from '../components/UserProfilePage';
import Layout from './Layout';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <HomePage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "books/:bookId",
        element: <BookDetailPage />,
      },
      {
        path: "users/current",
        element: <UserProfilePage />,
      }
    ],
  },
]);