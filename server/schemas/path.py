from beanie import Document


class PathDocument(Document):
    station_id_start: int
    station_id_end: int
    ways: list[int]
