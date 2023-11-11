import React, { useState, useEffect } from 'react';
import { Box, useTheme } from '@mui/material';
import { Map as LeafletMap, Polyline, polyline, circle, canvas } from 'leaflet';
import { MapContainer, TileLayer, Marker, Popup, Circle, LayerGroup } from 'react-leaflet';

import 'leaflet/dist/leaflet.css';
import { queryWay, Node, Way } from '~/geo/overpass';
import MapSearch from '~/components/mapSearch';

import railways from '~/assets/railways.json';
import stations from '~/assets/stations.json';
import { useWs } from '~/ws/useWs';

type Station = {
  id: number;
  lat: number;
  lon: number;
  name: string;
  type: string;
};

type Railway = {
  id1: number;
  id2: number;
  dist: number;
};

const train = {
  position: [48.4683, 42.3162],
  route: {
    start: [48.4272, 42.2162],
    end: [48.491, 42.361],
  },
};

function MapPage() {
  const theme = useTheme();
  const [map, setMap] = useState<LeafletMap | null>(null);
  const ws = useWs();
  const [currentPath, setCurrentPath] = useState<Polyline | null>(null);

  useEffect(() => {
    if (map !== null) {
      (stations as Station[]).forEach((station) => {
        circle([station.lat, station.lon], {
          radius: 200,
          color: theme.palette.primary.main,
        }).addTo(map);
      });
    }
  }, [map]);

  useEffect(() => {
    if (map !== null && ws !== null) {
      map.on('zoom', (event) => {
        const bounds = map.getBounds();
        const request = {
          south_west: Object.values(bounds.getSouthWest()),
          north_east: Object.values(bounds.getNorthEast()),
        };
        ws?.send('UPDATE_BOUNDS', request);
      });
    }
    // return () => void map?.off();
  }, [map, ws]);

  return (
    <Box>
      <MapContainer
        // eslint-disable-next-line
        // @ts-ignore
        attributionControl={false}
        center={train.position as [number, number]}
        minZoom={4}
        zoom={13}
        scrollWheelZoom
        style={{
          width: '100vw',
          height: '100vh',
        }}
        ref={setMap}
        renderer={canvas()}
        worldCopyJump={true}
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        <TileLayer url="https://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png" />

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
