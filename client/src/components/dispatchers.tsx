import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid, GridColDef } from '@mui/x-data-grid';

const columns: GridColDef[] = [
  { field: 'id', headerName: 'ID', width: 90 },
  {
    field: 'firstName',
    headerName: 'Имя',
    width: 150,
  },
  {
    field: 'lastName',
    headerName: 'Фамилия',
    width: 200,
  },
  {
    field: 'patronymic',
    headerName: 'Отчество',
    width: 200,
  },
  {
    field: 'email',
    headerName: 'Email',
    width: 300,
  },
  {
    field: 'login',
    headerName: 'Логин',
    width: 110,
  },
  {
    field: 'password',
    headerName: 'Пароль',
    width: 110,
  },
];

const rows = [
  { id: 1, firstName: 'Кирилл', lastName: 'Смирновский', patronymic: 'Филиппович', email: 'kirill1994@outlook.com', login: 'kirill1994', password: 'ba17ae1c9'},
  { id: 2, firstName: 'Давид', lastName: 'Корепанов', patronymic: 'Аркадьевич', email: 'david60@yandex.ru', login: 'david60', password: 'fd776488f' },
  { id: 3, firstName: 'Кирилл', lastName: 'Грибов', patronymic: 'Кириллович', email: 'kirill1969@hotmail.com', login: 'kirill1969', password: '23dab1acf' },
  { id: 4, firstName: 'Екатерина', lastName: 'Янишпольская', patronymic: 'Игнатевна', email: 'ekaterina09011978@ya.ru', login: 'ekaterina09011978', password: 'd7a548e7c' },
  { id: 5, firstName: 'Лаврентий', lastName: 'Прибылов', patronymic: 'Сергеевич', email: 'lavrentiy24@hotmail.com', login: 'lavrentiy24', password: '500847ea3' },
];

export default function DispatchersGrid() {
  return (
    <Box sx={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        checkboxSelection
        disableRowSelectionOnClick
      />
    </Box>
  );
}
