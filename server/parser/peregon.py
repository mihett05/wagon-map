import csv
import json
from pathlib import Path


def parse_peregon_to_json():
    with open(Path(__file__).parent.parent / "data" / "PEREGON_HACKATON.csv") as f:
        rows = list(csv.reader(f, delimiter=";"))[1:]
    output = []
    for row in rows:
        id1, id2, dist = list(map(lambda x: int("".join(x.split())), row))
        output.append({"id1": id1, "id2": id2, "dist": dist})
    with open(Path(__file__).parent.parent / "railways.json", "w") as f:
        json.dump(output, f)
