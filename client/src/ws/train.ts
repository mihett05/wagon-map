export type Wagon = {
  wagon_id: number;
  operdate: number;
  st_id_disl: number;
  st_id_dest: number;
  train_index: string;
};

export type Train = {
  index: string;
  position: [number, number];
  route: {
    start: number;
    end: number;
  };
  velocity: {
    x: number;
    y: number;
  }; // градусы в секунду
  wagons: Wagon[];
};

export const train: Train = {
  index: '1268-677-1663',
  position: [61.6620369, 40.2061615],
  route: {
    start: 1268,
    end: 1655,
  },
  velocity: {
    x: -2.630669021790703e-11 * 10000000,
    y: +1.536934098508053e-11 * 10000000,
  },
  wagons: [
    {
      wagon_id: 5904,
      operdate: 1699762860.069021,
      st_id_disl: 1798,
      st_id_dest: 2326,
      train_index: '3849-438-1836',
    },
    {
      wagon_id: 4658,
      operdate: 1699762860.065831,
      st_id_disl: 1798,
      st_id_dest: 2326,
      train_index: '3849-438-1836',
    },
    {
      wagon_id: 3425,
      operdate: 1699762860.061598,
      st_id_disl: 1798,
      st_id_dest: 2326,
      train_index: '3849-438-1836',
    },
  ],
};
