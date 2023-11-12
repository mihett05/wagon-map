import { api } from './api';

export const login = async (email: string, password: string): Promise<'user' | 'admin'> => {
  const response = await api.post('/auth/login', {
    email,
    password,
  });
  const data = response.data;
  localStorage.setItem('access_token', data.access_token);
  return 'user';
};
