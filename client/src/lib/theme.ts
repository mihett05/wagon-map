import { createTheme } from '@mui/material';

export const theme = createTheme({
  palette: {
    primary: {
      main: '#AE5555',
    },
  },
  typography: {
    fontSize: 14,
    fontFamily: 'Montserrat',
    h1: {
      fontWeight: 500,
      fontSize: 32,
    },
    body1: {
      fontWeight: 500,
    },
    button: {
      fontSize: 16,
      fontWeight: 500,
      textTransform: 'capitalize',
    },
  },
  shape: {
    borderRadius: 12,
  },
  components: {
    MuiButtonBase: {
      defaultProps: {
        sx: { height: 60 },
      },
    },
    MuiTextField: {
      defaultProps: {
        inputProps: {
          style: {
            fontSize: 14,
            height: '26px',
          },
        },
      },
    },
  },
});
