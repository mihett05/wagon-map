import React from 'react';
import BackgroundImage from '../assets/images/background.png';
import LoginForm from '~/components/loginForm';

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
  return (
    <div style={styles.header}>
      <div style={styles.content}>
        <LoginForm />
      </div>
    </div>
  );
}

export default LoginPage;
