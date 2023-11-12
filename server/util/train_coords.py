import json
import os

AVG_TRAIN_SPEED = 0.013  # km/s (средняя техническая скорость, которая учитывает разгон и торможение — 48 км/ч)


with open(f"{os.path.dirname(os.path.realpath(__file__))}/../static_data/times_travelled.json") as time_file:
    data = json.load(time_file)
    data = {tuple(d["pair"]): d["times"] for d in data}


def get_mean_time(node_1: int, node_2: int, distance: float) -> float:
    time = data.get((node_1, node_2))  # На основе исторических данных

    if time is not None:
        return time

    return distance / AVG_TRAIN_SPEED  # Если нет исторических данных о времени рассчитать его


def calculate_coords(coords_path: list[tuple[float]], cumulative_distances: list[float],
                     timestamp: float, mean_time: float):
    ...
