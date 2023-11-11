import { useState, useEffect } from 'react';
import { Ws } from './ws';

const WS_URl = 'ws://localhost:8000/websocket/';

export function useWs() {
  const [ws, setWs] = useState<Ws | null>(null);
  useEffect(() => {
    const socket = new WebSocket(WS_URl);
    const createdWs = new Ws(socket);
    setWs(createdWs);
    return () => createdWs.close();
  }, []);

  return ws;
}
