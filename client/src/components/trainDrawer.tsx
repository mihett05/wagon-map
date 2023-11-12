import React from 'react';
import {
  Drawer,
  Box,
  ListItem,
  List,
  ListItemIcon,
  ListItemText,
  Typography,
  Link,
  Tooltip,
} from '@mui/material';

import LocationIcon from '~/assets/location.svg?react';
import StStartIcon from '~/assets/st_start.svg?react';
import StEndIcon from '~/assets/st_end.svg?react';
import TrainIcon from '~/assets/train.svg?react';
import TimetableIcon from '~/assets/timetable.svg?react';

import stations from '~/assets/stations.json';

import { Train, Wagon } from '~/ws/train';
import { Map } from 'leaflet';

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

interface TrainDrawerProps {
  map: Map | null;
  train: Train | null;
  open: boolean;
  onClose: () => void;
}

function TrainDrawer({ open, onClose, train, map }: TrainDrawerProps) {
  const findStation = (id: number) => {
    return stations.find((st) => st.id === id);
  };

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
                <Link
                  sx={{
                    cursor: 'pointer',
                  }}
                >
                  <b
                    onClick={() => {
                      if (train?.route.start) {
                        const st = findStation(train?.route.start);
                        if (st) {
                          map?.panTo([st.lat, st.lon]);
                        }
                      }
                    }}
                  >
                    {train?.route.start}
                  </b>
                </Link>
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
                <Link
                  sx={{
                    cursor: 'pointer',
                  }}
                >
                  <b
                    onClick={() => {
                      if (train?.route.end) {
                        const st = findStation(train?.route.end);
                        if (st) {
                          map?.panTo([st.lat, st.lon]);
                        }
                      }
                    }}
                  >
                    {train?.route.end}
                  </b>
                </Link>
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
                  chunkify(train?.wagons, 4, true).map((list: Wagon[]) => (
                    <List>
                      {list.map((w) => (
                        <ListItem key={w.wagon_id}>
                          <ListItemText>
                            <Tooltip title={`${w.st_id_disl} -> ${w.st_id_dest}`}>
                              <Link
                                sx={{
                                  cursor: 'pointer',
                                }}
                              >
                                {w.wagon_id}
                              </Link>
                            </Tooltip>
                          </ListItemText>
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

export default TrainDrawer;
