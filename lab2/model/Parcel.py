class Parcel:
    def __init__(self, track: str, status: str, sender: str, getter: str, date: str):
        self.track = track
        self.statuses = []
        self.statuses.append(status)
        self.sender = sender
        self.getter = getter
        self.date = date

    def get_last_status(self):
        return self.statuses[-1]

    def change_status(self, new_stat: str):
        self.statuses.append(new_stat)

    def change_date(self, new_date: str):
        self.date = new_date