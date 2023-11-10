import React from 'react';

import { createBrowserRouter } from 'react-router-dom';
import LoginPage from '~/pages/login';
import SignUp from '~/pages/signup';

const router = createBrowserRouter([
  {
    path: '/',
    element: <LoginPage />,
  },
  {
    path: "/signup",
    element: <SignUp />,
  },
]);

export default router;
