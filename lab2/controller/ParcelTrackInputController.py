from lab.view.ViewsFactory import ViewsFactory
from lab.model.ParselStorage import ParcelStorage
from lab.model.DataSaver import DataSaver
from lab.model.CurrentSession import CurrentSession
from lab.controller.AccountLoginController import AccountLoginController
from lab.controller.UserParcelViewController import UserParcelViewController
from lab.controller.OperatorParcelViewController import OperatorParcelViewController
from lab.controller.ParcelCreatorController import ParcelCreatorController


class ParcelTrackInputController:
    def __init__(self):
        self.parcle_storage = ParcelStorage
        self.current_session = CurrentSession
        self.data_saver = DataSaver
        self.parcel_input_view = ViewsFactory.create_parcel_input_view(self)
        self.parcel_input_view.main()


        
    def parcel_input_view_customer(self):
        self.parcel_input_view.main()


    def authorize(self):
        self.parcel_input_view.destroy()
        account_login_controller = AccountLoginController()
        account_login_controller.login_view_start()
        self.parcel_input_view0 = ViewsFactory.create_parcel_input_view0(self)
        self.parcel_input_view0.main()
        
    def open_operator_view(self):
        self.operator_view = OperatorParcelViewController()
        
    def open_user_view(self):
        self.user_view = UserParcelViewController()

    def create(self):
        self.parcel_create_controller = ParcelCreatorController()

if __name__ == "__main__":
    parcel_track_input_controller = ParcelTrackInputController()

        