import React from 'react';
import { Box } from '@mui/material';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

import 'leaflet/dist/leaflet.css';

function MapPage() {
  return (
    <Box>
      <MapContainer
        // eslint-disable-next-line
        // @ts-ignore
        attributionControl={false}
        center={[51.505, -0.09]}
        zoom={13}
        scrollWheelZoom
        style={{
          width: '100vw',
          height: '100vh',
        }}
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        <TileLayer url="https://a.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png" />

        <Marker position={[51.505, -0.09]}>
          <Popup>
            A pretty CSS3 popup. <br /> Easily customizable.
          </Popup>
        </Marker>
      </MapContainer>
    </Box>
  );
}

export default MapPage;
