import random
import string


class ParcelIdentifier:
    def __init__(self):
        self.tracks = []

    def create_track(self):
        track = self.__generate_hash()

    def clean_track(self, track_to_r: str):
        track_indx = -1
        for i in range(len(self.tracks)):
            if self.tracks[i] == track_to_r:
                track_indx = i
        if track_indx != -1:
            self.tracks.remove(self.tracks[track_indx])

    def __generate_hash(self):
        characters = string.digits + string.ascii_uppercase
        hash_value = ''.join(random.choices(characters, k=12))
        return hash_value
