import json
import math
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


def calculate_coords(coords_path: list[tuple[float, float]], cumulative_distances: list[float], timestamp: float) -> \
list[float]:
    max_velocity = 25
    max_acceleration = 0.5
    earth_radius = 6371000.0

    acceleration_distance = cumulative_distances[-1] / 4

    acceleration_time = math.sqrt(2 * acceleration_distance / max_acceleration)
    no_acceleration_time = 2 * acceleration_distance / max_velocity

    if timestamp < acceleration_time:
        velocity = max_acceleration * timestamp
        distance = max_acceleration * timestamp ** 2 / 2
    elif timestamp < acceleration_time + no_acceleration_time:
        velocity = max_velocity
        distance = max_velocity * (timestamp - acceleration_time) + acceleration_distance
    else:
        relative_time = timestamp - acceleration_time - no_acceleration_time
        velocity = max_velocity - max_acceleration * relative_time
        distance = max_velocity * relative_time - max_acceleration * relative_time ** 2 / 2 + acceleration_distance * 3

    pair_number = 0
    while pair_number + 2 < len(cumulative_distances) and not (
        cumulative_distances[pair_number] < distance / 1000 < cumulative_distances[pair_number + 1]):
        pair_number += 1

    relative_distance = distance - cumulative_distances[pair_number] * 1000
    segment_distance = (cumulative_distances[pair_number + 1] - cumulative_distances[pair_number]) * 1000
    relative_distance_coefficient = relative_distance / segment_distance

    first_latitude, first_longitude = coords_path[pair_number]
    second_latitude, second_longitude = coords_path[pair_number + 1]

    current_latitude = (second_latitude - first_latitude) * relative_distance_coefficient + first_latitude
    current_longitude = (second_longitude - first_longitude) * relative_distance_coefficient + first_latitude

    velocity_x = (second_longitude - first_longitude) / (second_longitude ** 2 + first_longitude ** 2) * velocity
    velocity_y = (second_latitude - first_latitude) / (second_latitude ** 2 + first_latitude ** 2) * velocity

    velocity_x = velocity_x / (earth_radius * math.cos(math.radians(current_latitude)))
    velocity_y = velocity_y / earth_radius

    return [current_latitude, current_longitude, velocity_x, velocity_y]
