import React from 'react';
import BackgroundImage from '../assets/images/background.png';
import LoginForm from '~/components/loginForm';

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
  // const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
  //   event.preventDefault();
  //   const data = new FormData(event.currentTarget);
  //   console.log({
  //     email: data.get('email'),
  //     password: data.get('password'),
  //   });
  // };

  return (
    <div style={styles.header}>
      <div style={styles.content}>
        <LoginForm />
      </div>
    </div>
  );
}

export default LoginPage;
