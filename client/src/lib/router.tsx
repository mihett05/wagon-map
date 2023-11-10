import React from 'react';
import { createBrowserRouter } from 'react-router-dom';

import LoginPage from '~/pages/login';
import SignUp from '~/pages/signup';
import MapPage from '~/pages/map';

const router = createBrowserRouter([
  {
    path: '/',
    element: <LoginPage />,
  },
  {
    path: "/signup",
    element: <SignUp />,
  },
  {
    path: '/map',
    element: <MapPage />,
  },
]);

export default router;
