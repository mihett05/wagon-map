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
  wagons: number[];
};

export const train: Train = {
  index: '1268-677-1663',
  position: [61.6620369, 40.2061615],
  route: {
    start: 1268,
    end: 1655,
  },
  velocity: {
    x: 0.001,
    y: 0.001,
  },
  wagons: [6516, 5100, 1234, 1231, 3432, 9239],
};
