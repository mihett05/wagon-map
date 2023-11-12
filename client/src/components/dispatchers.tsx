import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid, GridActionsCellItem, GridColDef } from '@mui/x-data-grid';
import ClearIcon from '@mui/icons-material/Clear';
import SettingsBackupRestoreIcon from '@mui/icons-material/SettingsBackupRestore';

interface DispatchersGridProps {
  rows: any[];
  setRows: (state: any) => any;
}

export default function DispatchersGrid({ rows, setRows }: DispatchersGridProps) {
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
      field: 'actions',
      type: 'actions',
      headerName: 'Действия',
      width: 100,
      cellClassName: 'actions',
      getActions: ({ id }) => {
        return [
          <GridActionsCellItem
            icon={<SettingsBackupRestoreIcon />}
            label="Сбросить пароль"
            onClick={() => {}}
          />,
          <GridActionsCellItem
            icon={<ClearIcon />}
            label="Удалить"
            onClick={() => {
              setRows((state) => state.filter((r) => r.id !== id));
            }}
          />,
        ];
      },
    },
  ];

  return (
    <Box sx={{ height: 400, width: '100%' }}>
      <DataGrid rows={rows} columns={columns} checkboxSelection disableRowSelectionOnClick />
    </Box>
  );
}
