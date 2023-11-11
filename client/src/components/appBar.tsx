import React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import MapOutlinedIcon from '@mui/icons-material/MapOutlined';
import PersonOutlineOutlinedIcon from '@mui/icons-material/PersonOutlineOutlined';

import Logo from '../assets/images/logo.png';

function AppBarComponent() {
  const [auth, setAuth] = React.useState(true);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setAuth(event.target.checked);
  };

  return (
    <>
      <Box>
        <AppBar position="static" sx={{ bgcolor: 'white' }}>
          <Toolbar>
            <Box sx={{ flexGrow: 1 }}>
              <Box
                component="img"
                sx={{
                  width: 100
                }}
                alt="Logo"
                src={Logo}
              />
            </Box>
            {auth && (
              <Box>
                <IconButton
                  size="large"
                  aria-label="map"
                  aria-controls="menu-appbar"
                  aria-haspopup="true"
                  color="primary"
                  href={`/map`}
                >
                  <MapOutlinedIcon />
                </IconButton>

                <IconButton
                  size="large"
                  aria-label="account of admin"
                  aria-controls="menu-appbar"
                  aria-haspopup="true"
                  color="primary"
                  href={`/account`}
                >
                  <PersonOutlineOutlinedIcon />
                </IconButton>
              </Box>
            )}
          </Toolbar>
        </AppBar>
      </Box>
    </>
  );
}

export default AppBarComponent;
