from lab.controller.ParcelTrackInputController import ParcelTrackInputController


class Application:
    def run(self):
        parcel_track_input_controller = ParcelTrackInputController()


if __name__ == "__main__":
    app = Application()
    app.run()