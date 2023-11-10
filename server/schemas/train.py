from beanie import Document

from models.train import Train


class TrainDocument(Document):
    train_info: Train
