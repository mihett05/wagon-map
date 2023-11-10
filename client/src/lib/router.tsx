import React from 'react';

import { createBrowserRouter } from 'react-router-dom';
import LoginPage from '~/pages/login';

const router = createBrowserRouter([
  {
    path: '/',
    element: <LoginPage />,
  },
]);

export default router;
