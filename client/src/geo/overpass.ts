const OVERPASS_API_INTERPRETER = 'https://maps.mail.ru/osm/tools/overpass/api/interpreter';

export const osmQuery = async (ql: string, bbox?: [number, number, number, number]) => {
  if (ql.includes('{{bbox}}')) {
    if (bbox === undefined)
      throw new TypeError("{{bbox}} was found in query, but it wasn't provided");
    ql = ql.replace('{{bbox}}', bbox.join(', '));
  }

  return (
    await (
      await fetch(OVERPASS_API_INTERPRETER, {
        method: 'POST',
        body: 'data=' + encodeURIComponent('[out:json];' + ql),
      })
    ).json()
  ).elements;
};

export type Way = {
  type: 'way';
  id: number;
  nodes: number[];
};

export type Node = {
  type: 'node';
  id: number;
  lat: number;
  lon: number;
};

export const queryWay = async (
  start: [number, number],
  end: [number, number],
): Promise<(Way | Node)[]> => {
  return osmQuery(`
  way
    [railway=rail]
    [usage=main]
    (${[...start, ...end].join(', ')});
  (._;>;);
  out body;
  `);
};
