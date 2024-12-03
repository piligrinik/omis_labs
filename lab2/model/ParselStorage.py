from .DataSaver import DataSaver
from .Saveable import Saveable
from .Parcel import Parcel


class ParcelStorage(Saveable):
    def __init__(self):
        self.parcels = []

    def add(self, new_parcel: Parcel):
        self.parcels.append(new_parcel)

    def remove(self, parcel_to_r: Parcel):
        self.parcels.remove(parcel_to_r)

    def find_parcel(self, track: str):
        for parcel in self.parcels:
            if parcel.track == track:
                return parcel
        return None

    def load(self, data_saver: DataSaver):
        pass

    def save(self, data_saver: DataSaver):
        pass
