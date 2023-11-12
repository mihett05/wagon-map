import React, { useState, useEffect, useMemo } from 'react';
import { Box, useTheme } from '@mui/material';
import { Map as LeafletMap, Polyline, circle, canvas } from 'leaflet';
import { MapContainer, TileLayer, LayerGroup, Circle } from 'react-leaflet';

import 'leaflet/dist/leaflet.css';
import { queryWay, Node, Way } from '~/geo/overpass';
import MapSearch from '~/components/mapSearch';
import TrainDrawer from '~/components/trainDrawer';
import StationDrawer from '~/components/stationDrawer';

import stations from '~/assets/stations.json';
import { useWs } from '~/ws/useWs';
import { train, Train } from '~/ws/train';
import { Station } from '~/ws/station';

function MapPage() {
  const theme = useTheme();
  const [map, setMap] = useState<LeafletMap | null>(null);
  const ws = useWs();
  const [selectedTrainIndex, setSelectedTrainIndex] = useState<string | null>(null);
  const [selecetdStationId, setSelectedStationId] = useState<number | null>(null);
  const [currentPath, setCurrentPath] = useState<Polyline | null>(null);
  const [trains, setTrains] = useState<Train[]>([]);

  const selectedTrain = useMemo<Train | null>(
    () =>
      selectedTrainIndex === null ? null : trains.filter((t) => t.index === selectedTrainIndex)[0],
    [selectedTrainIndex, trains],
  );

  const selectedStation = useMemo<Station | null>(
    () =>
      selecetdStationId === null ? null : stations.filter((s) => s.id === selecetdStationId)[0],
    [selecetdStationId],
  );

  // TODO: ws handler
  useEffect(() => {
    setTrains([train]);
    const interval = setInterval(() => {
      setTrains((state) =>
        state.map((t) => ({
          ...t,
          position: [t.position[0] + t.velocity.y * 1, t.position[1] + t.velocity.x * 1],
        })),
      );
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (map !== null && ws !== null) {
      map.on('zoom', () => {
        const bounds = map.getBounds();
        const request = {
          south_west: Object.values(bounds.getSouthWest()),
          north_east: Object.values(bounds.getNorthEast()),
        };
        ws?.send('UPDATE_BOUNDS', request);
      });
    }
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

        <LayerGroup>
          {(stations as Station[]).map((station) => (
            <Circle
              center={[station.lat, station.lon]}
              radius={200}
              color={theme.palette.primary.main}
              eventHandlers={{
                click: () => {
                  setSelectedStationId(station.id);
                },
              }}
            />
          ))}
        </LayerGroup>

        <LayerGroup>
          {trains.map((t) => (
            <Circle
              center={t.position as [number, number]}
              radius={100}
              eventHandlers={{
                click: () => {
                  setSelectedTrainIndex(t.index);
                },
              }}
            />
          ))}
        </LayerGroup>

        <MapSearch />
        <TrainDrawer
          open={selectedTrainIndex !== null}
          onClose={() => setSelectedTrainIndex(null)}
          train={selectedTrain}
          map={map}
        />
        <StationDrawer
          open={selecetdStationId !== null}
          onClose={() => setSelectedStationId(null)}
          station={selectedStation}
        />
      </MapContainer>
    </Box>
  );
}

export default MapPage;
