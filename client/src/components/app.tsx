import React from 'react';
import { CssBaseline, ThemeProvider } from '@mui/material';
import { RouterProvider } from 'react-router-dom';

import { theme } from '~/lib/theme';
import router from '~/lib/router';
import AppBarComponent from './appBar';

function App() {
  return (
    <>
      <CssBaseline />
      <ThemeProvider theme={theme}>
        <AppBarComponent />

        <RouterProvider router={router} />
      </ThemeProvider>
    </>
  );
}

export default App;
