import React, { useState } from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import AccountModal from '~/components/accountModal';
import DispatchersGrid from '~/components/dispatchers';

export default function Account() {
  const [rows, setRows] = useState(() => [
    {
      id: 1,
      firstName: 'Кирилл',
      lastName: 'Смирновский',
      patronymic: 'Филиппович',
      email: 'kirill1994@outlook.com',
      login: 'kirill1994',
      password: 'ba17ae1c9',
    },
    {
      id: 2,
      firstName: 'Давид',
      lastName: 'Корепанов',
      patronymic: 'Аркадьевич',
      email: 'david60@yandex.ru',
      login: 'david60',
      password: 'fd776488f',
    },
    {
      id: 3,
      firstName: 'Кирилл',
      lastName: 'Грибов',
      patronymic: 'Кириллович',
      email: 'kirill1969@hotmail.com',
      login: 'kirill1969',
      password: '23dab1acf',
    },
    {
      id: 4,
      firstName: 'Екатерина',
      lastName: 'Янишпольская',
      patronymic: 'Игнатевна',
      email: 'ekaterina09011978@ya.ru',
      login: 'ekaterina09011978',
      password: 'd7a548e7c',
    },
    {
      id: 5,
      firstName: 'Лаврентий',
      lastName: 'Прибылов',
      patronymic: 'Сергеевич',
      email: 'lavrentiy24@hotmail.com',
      login: 'lavrentiy24',
      password: '500847ea3',
    },
  ]);
  return (
    <div>
      <Container maxWidth="sm">
        <CssBaseline />
        <AccountModal rows={rows} setRows={setRows} />
      </Container>
      <Container fixed>
        <DispatchersGrid rows={rows} setRows={setRows} />
      </Container>
    </div>
  );
}
