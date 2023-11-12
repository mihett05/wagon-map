import React from 'react';
import {
  Drawer,
  Box,
  ListItem,
  List,
  ListItemIcon,
  ListItemText,
  Typography,
  TableContainer,
  Table,
  TableHead,
  TableCell,
  TableBody,
  TableRow,
} from '@mui/material';

import LocationIcon from '~/assets/location.svg?react';
import StStartIcon from '~/assets/st_start.svg?react';
import StEndIcon from '~/assets/st_end.svg?react';
import TrainIcon from '~/assets/train.svg?react';
import TimetableIcon from '~/assets/timetable.svg?react';

import { Station } from '~/ws/station';

interface StationDrawerProps {
  station: Station | null;
  open: boolean;
  onClose: () => void;
}

function StationDrawer({ open, onClose, station }: StationDrawerProps) {
  return (
    <Drawer anchor="right" open={open} onClose={onClose}>
      <Box
        sx={{
          width: 400,
        }}
      >
        <Typography variant="h5" align="center">
          Станция
        </Typography>
        <Typography variant="h4" align="center">
          {station?.name || 'Неизвестно'}
        </Typography>
        <List>
          <ListItem>
            <ListItemIcon>
              <LocationIcon />
            </ListItemIcon>
            <ListItemText>
              Местоположение
              <Box
                sx={{
                  display: 'flex',
                  flexDirection: 'row',
                  gap: 2,
                }}
              >
                <b>{station?.lat.toFixed(6)} СШ</b>
                <b>{station?.lon.toFixed(6)} ВД</b>
              </Box>
            </ListItemText>
          </ListItem>
          <ListItem>
            <ListItemIcon>
              <TimetableIcon />
            </ListItemIcon>
            <ListItemText>
              Расписание
              <TableContainer>
                <Table>
                  <TableHead>
                    <TableCell>Поезд</TableCell>
                    <TableCell>Время</TableCell>
                  </TableHead>
                  <TableBody>
                    <TableRow>
                      <TableCell>5334-343-4321</TableCell>
                      <TableCell>12:34</TableCell>
                    </TableRow>
                    <TableRow>
                      <TableCell>8931-731-61</TableCell>
                      <TableCell>12:38</TableCell>
                    </TableRow>
                    <TableRow>
                      <TableCell>4827-389-87</TableCell>
                      <TableCell>12:53</TableCell>
                    </TableRow>
                  </TableBody>
                </Table>
              </TableContainer>
            </ListItemText>
          </ListItem>
        </List>
      </Box>
    </Drawer>
  );
}

export default StationDrawer;
