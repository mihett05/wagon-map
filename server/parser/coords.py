import csv
import json
import asyncio
from pathlib import Path
from schemas.geojson import GeoJSON
from models.station import Station


async def save_station(st_id: int, lat: float, lon: float):
    st = Station(id=int(st_id), cooridnates=GeoJSON.point(lat, lon))
    await st.create()


async def parse_coords():
    with open(
        Path(__file__).parent.parent / "data" / "STATION_COORDS_HACKATON.csv"
    ) as f:
        rows = list(csv.reader(f, delimiter=";"))[1:]
    await asyncio.gather(
        *[
            save_station(
                int("".join(row[0].split())),
                float(row[1].replace(",", ".")),
                float(row[2].replace(",", ".")),
            )
            for row in rows
            if row[1] and row[2]
        ]
    )


def parse_coords_json():
    with open(
        Path(__file__).parent.parent / "data" / "STATION_COORDS_HACKATON.csv"
    ) as f:
        rows = list(csv.reader(f, delimiter=";"))[1:]
    output = [
        {
            "id": int("".join(row[0].split())),
            "lat": float(row[1].replace(",", ".")),
            "lon": float(row[2].replace(",", ".")),
        }
        for row in rows
        if row[1] and row[2]
    ]
    with open(Path(__file__).parent.parent / "stations.json", "w") as f:
        json.dump(output, f)
