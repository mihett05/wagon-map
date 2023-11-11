import React, { useState } from 'react';
import { Box } from '@mui/material';
import { Map as LeafletMap, Polyline, polyline } from 'leaflet';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

import 'leaflet/dist/leaflet.css';
import { queryWay, Node, Way } from '~/geo/overpass';
import MapSearch from '~/components/mapSearch';

const train = {
  position: [48.4683, 42.3162],
  route: {
    start: [48.4272, 42.2162],
    end: [48.491, 42.361],
  },
};

function MapPage() {
  const [map, setMap] = useState<LeafletMap | null>(null);
  const [currentPath, setCurrentPath] = useState<Polyline | null>(null);

  return (
    <Box>
      <MapContainer
        // eslint-disable-next-line
        // @ts-ignore
        attributionControl={false}
        center={train.position as [number, number]}
        zoom={13}
        scrollWheelZoom
        style={{
          width: '100vw',
          height: '100vh',
        }}
        ref={setMap}
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        <TileLayer url="https://a.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png" />
        <Marker
          position={train.position as [number, number]}
          eventHandlers={{
            click: async () => {
              if (!map) return;

              const ways = await queryWay(
                train.route.start as [number, number],
                train.route.end as [number, number],
              );
              const nodes = new Map<number, [number, number]>();
              (ways.filter((way) => way.type === 'node') as Node[]).forEach((node) => {
                nodes.set(node.id, [node.lat, node.lon]);
              });

              const pathes = (ways.filter((way) => way.type === 'way') as Way[]).map((way) =>
                way.nodes.map((nodeId) => nodes.get(nodeId)),
              ) as [number, number][][];

              setCurrentPath(polyline(pathes, {}).addTo(map));
            },
            popupclose: () => {
              if (currentPath !== null) {
                currentPath.remove();
                setCurrentPath(null);
              }
            },
          }}
        >
          <Popup>Поезд 1-1-2</Popup>
        </Marker>

        <MapSearch />
      </MapContainer>
    </Box>
  );
}

export default MapPage;
