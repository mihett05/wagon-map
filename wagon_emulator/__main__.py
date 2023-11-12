import csv
import os
from datetime import datetime
from time import sleep

import requests

server_url = os.getenv("SERVER_URL", default="http://0.0.0.0:8000/")


class WagonData:
    def __init__(self, wagon_id: int, operdate: datetime, st_id_disl: int, st_id_dest: int, train_index: str):
        self.wagon_id = wagon_id
        self.operdate = operdate
        self.st_id_disl = st_id_disl
        self.st_id_dest = st_id_dest
        self.train_index = train_index

    def to_json(self):
        return {"wagon_id": self.wagon_id,
                "operdate": self.operdate.isoformat(),
                "st_id_disl": self.st_id_disl,
                "st_id_dest": self.st_id_dest,
                "train_index": self.train_index}


def make_request(wagon: WagonData):
    url = server_url + f"trains/wagon/{wagon.wagon_id}"

    try:
        requests.post(url, json=wagon.to_json())
    except requests.exceptions.HTTPError as e:
        print(e.response.text)


wagon_data: list[WagonData] = []
index = 0

with open('disl_one_day.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        try:
            wagon_data.append(WagonData(wagon_id=int(row[0]),
                                        operdate=datetime.fromtimestamp(float(row[1])),
                                        st_id_disl=int(row[2]),
                                        st_id_dest=int(row[3]),
                                        train_index=row[4]))
        except ValueError:
            continue

while True:
    index += 1
    if wagon_data[index].operdate.time() > datetime.now().time():
        index -= 10
        break

# sleep(120)

try:
    while True:
        index = index % len(wagon_data)
        data = wagon_data[index]
        cur_time = datetime.now()
        if data.operdate.hour <= cur_time.hour and data.operdate.minute <= cur_time.minute:
            index += 1
            make_request(data)
except KeyboardInterrupt:
    print('interrupted!')
