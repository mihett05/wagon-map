import React from 'react';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import BackgroundImage from '../assets/images/background.png';
import { Card, CardContent } from '@mui/material';

// import { ThemeProvider } from '@mui/material/styles';
// import { theme } from '~/lib/theme';

const styles = {
  header: {
    backgroundImage: `url(${BackgroundImage})`,
    height: '100vh',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
    backgroundSize: 'cover',
  },

  content: {
    height: '100%',
    width: '100%',
    backgroundColor: 'rgba(255, 255, 255, 0.8)',
    padding: 50,
  },
};

function LoginPage() {
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      email: data.get('email'),
      password: data.get('password'),
    });
  };

  return (
    <div style={styles.header}>
      <div style={styles.content}>
        <Container component="main" maxWidth="xs">
          <CssBaseline />
          <Card>
            <CardContent
              sx={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                padding: 3,
              }}
            >
              <Typography component="h1" variant="h1">
                Вход
              </Typography>
              <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                <TextField
                  margin="normal"
                  required
                  fullWidth
                  id="email"
                  label="Email"
                  name="email"
                  autoComplete="email"
                  autoFocus
                />
                <TextField
                  margin="normal"
                  required
                  fullWidth
                  name="password"
                  label="Пароль"
                  type="password"
                  id="password"
                  autoComplete="current-password"
                />
                <Button fullWidth variant="contained" sx={{ mt: 2 }} href={`/map`}>
                  Войти
                </Button>
                <Button fullWidth variant="outlined" sx={{ mt: 1, mb: 2 }} href={`/signup`}>
                  Создать аккаунт
                </Button>
                <Grid container>
                  <Grid container justifyContent="center">
                    <Link href="#" variant="body2" underline="hover">
                      Забыли пароль?
                    </Link>
                  </Grid>
                </Grid>
              </Box>
            </CardContent>
          </Card>
        </Container>
      </div>
    </div>
  );
}

export default LoginPage;
