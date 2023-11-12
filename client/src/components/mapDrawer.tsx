import React from 'react';
import { Drawer, Box, ListItem, List, ListItemIcon, ListItemText, Typography } from '@mui/material';
import _ from 'lodash';

import LocationIcon from '~/assets/location.svg?react';
import StStartIcon from '~/assets/st_start.svg?react';
import StEndIcon from '~/assets/st_end.svg?react';
import TrainIcon from '~/assets/train.svg?react';
import TimetableIcon from '~/assets/timetable.svg?react';

import { Train } from '~/ws/train';

function chunkify(a, n, balanced) {
  if (n < 2) return [a];

  const len = a.length;
  const out = [];
  let i = 0;
  let size;

  if (len % n === 0) {
    size = Math.floor(len / n);
    while (i < len) {
      out.push(a.slice(i, (i += size)));
    }
  } else if (balanced) {
    while (i < len) {
      size = Math.ceil((len - i) / n--);
      out.push(a.slice(i, (i += size)));
    }
  } else {
    n--;
    size = Math.floor(len / n);
    if (len % size === 0) size--;
    while (i < size * n) {
      out.push(a.slice(i, (i += size)));
    }
    out.push(a.slice(size * n));
  }

  return out;
}

interface MapDrawer {
  train: Train | null;
  open: boolean;
  onClose: () => void;
}

function MapDrawer({ open, onClose, train }: MapDrawer) {
  return (
    <Drawer anchor="right" open={open} onClose={onClose}>
      <Box
        sx={{
          width: 400,
        }}
      >
        <Typography variant="h5" align="center">
          Поезд
        </Typography>
        <Typography variant="h4" align="center">
          {train?.index}
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
                <b>{train?.position[1].toFixed(6)} СШ</b>
                <b>{train?.position[1].toFixed(6)} ВД</b>
              </Box>
            </ListItemText>
          </ListItem>
          <ListItem>
            <ListItemIcon>
              <StStartIcon />
            </ListItemIcon>
            <ListItemText>
              Станция отправки
              <Box>
                <b>{train?.route.start}</b>
              </Box>
            </ListItemText>
          </ListItem>
          <ListItem>
            <ListItemIcon>
              <StEndIcon />
            </ListItemIcon>
            <ListItemText>
              Станция прибытия
              <Box>
                <b>{train?.route.end}</b>
              </Box>
            </ListItemText>
          </ListItem>
          <ListItem>
            <ListItemIcon>
              <TrainIcon />
            </ListItemIcon>
            <ListItemText>
              Состав
              <Box
                sx={{
                  display: 'flex',
                }}
              >
                {train &&
                  chunkify(train?.wagons, 4, true).map((list: number[]) => (
                    <List>
                      {list.map((w) => (
                        <ListItem>
                          <ListItemText>{w}</ListItemText>
                        </ListItem>
                      ))}
                    </List>
                  ))}
              </Box>
            </ListItemText>
          </ListItem>
        </List>
      </Box>
    </Drawer>
  );
}

export default MapDrawer;
