import {
  Autocomplete,
  Box,
  FormControl,
  Grid,
  InputLabel,
  MenuItem,
  Select,
  SelectChangeEvent,
  TextField,
  autocompleteClasses,
} from '@mui/material';
import React, { useState } from 'react';

import PlaceIcon from '@mui/icons-material/Place';
import TrainIcon from '@mui/icons-material/Train';
import CategoryIcon from '@mui/icons-material/Category';
import SearchIcon from '@mui/icons-material/Search';

function MapSearch() {
  const [icon, setIcon] = useState('0');

  const handleChange = (event: SelectChangeEvent) => {
    setIcon(event.target.value);
  };

  return (
    <Box
      sx={{
        position: 'absolute',
        bottom: 40,
        left: 60,
        zIndex: 'tooltip',
      }}
    >
      <Grid container>
        <Grid item xs={3}>
          <FormControl fullWidth>
            <InputLabel id="demo-simple-select-label"></InputLabel>
            <Select
              labelId="demo-simple-select-label"
              id="demo-simple-select"
              value={icon}
              label=""
              sx={{ width: 60, bgcolor: 'white', borderRadius: 2, borderColor: 'none' }}
              onChange={handleChange}
              inputProps={{ IconComponent: () => null }}
            >
              <MenuItem value={0}>
                <PlaceIcon />
              </MenuItem>
              <MenuItem value={1}>
                <TrainIcon />
              </MenuItem>
              <MenuItem value={2}>
                <CategoryIcon />
              </MenuItem>
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={5}>
          <Autocomplete
            disablePortal
            id="combo-box-demo"
            options={stations}
            getOptionLabel={(option) => option.id}
            popupIcon={<SearchIcon />}
            sx={{
              width: 300,
              borderRadius: 1,
              bgcolor: 'white',
              [`& .${autocompleteClasses.popupIndicator}`]: {
                transform: 'none',
              },
            }}
            renderInput={(params) => <TextField {...params} label="" variant="outlined" />}
          />
        </Grid>
      </Grid>
    </Box>
  );
}

export default MapSearch;

const stations = [
  { id: '1' },
  { id: '2' },
  { id: '3' },
  { id: '4' },
  { id: '5' },
  { id: '6' },
  { id: '7' },
];
