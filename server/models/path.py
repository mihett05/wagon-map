from beanie import Document


class Path(Document):
    station_id_start: int
    station_id_end: int
    ways: list[int]
