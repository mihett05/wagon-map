import datetime

from pydantic import BaseModel


class Wagon(BaseModel):
    wagon_id: int
    operdate: datetime.datetime
    st_id_disl: int
    st_id_dest: int
    train_index: str

    def to_json(self):
        return {"wagon_id": self.wagon_id,
                "operdate": self.operdate.timestamp(),
                "st_id_disl": self.st_id_disl,
                "st_id_dest": self.st_id_dest,
                "train_index": self.train_index}


class WagonPosition(Wagon):
    lat: float
    lon: float
