import React from 'react';
import { createBrowserRouter } from 'react-router-dom';

import LoginPage from '~/pages/login';
import MapPage from '~/pages/map';
import AccountPage from '~/pages/account';

const router = createBrowserRouter([
  {
    path: '/',
    element: <LoginPage />,
  },
  {
    path: "/account",
    element: <AccountPage />,
  },
  {
    path: '/map',
    element: <MapPage />,
  },
]);

export default router;
