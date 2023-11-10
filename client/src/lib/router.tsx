import React from 'react';
import { createBrowserRouter } from 'react-router-dom';

import LoginPage from '~/pages/login';
import MapPage from '~/pages/map';

const router = createBrowserRouter([
  {
    path: '/',
    element: <LoginPage />,
  },
  {
    path: '/map',
    element: <MapPage />,
  },
]);

export default router;
