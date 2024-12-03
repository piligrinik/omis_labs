from .UserParcelView import UserParcelView
from .LoginView import LoginView
from .ParcelEditView import ParcelEditView
from .ParcelInputView import ParcelInputView
from .ParcelCreatorView import ParcelCreatorView
from .OperatorParcelView import OperatorParcelView
from .ParcelInputView0 import ParcelInputView0


class ViewsFactory:

    @staticmethod
    def create_user_parcel_view(controller):
        user_parcel_view = UserParcelView(controller)
        return user_parcel_view
    
    @staticmethod
    def create_operator_parcel_view(controller):
        operator_parcel_view = OperatorParcelView(controller)
        return operator_parcel_view
    
    @staticmethod
    def create_parcel_edit_view(controller):
        parcel_edit_view = ParcelEditView(controller)
        return parcel_edit_view
    
    @staticmethod
    def create_parcel_input_view0(controller):
        parcel_input_view0 = ParcelInputView0(controller)
        return parcel_input_view0
    
    @staticmethod
    def create_parcel_input_view(controller):
        parcel_input_view = ParcelInputView(controller)
        return parcel_input_view
    
    @staticmethod
    def create_login_view(controller):
        login_view = LoginView(controller)
        return login_view

    @staticmethod
    def create_parcel_creator_view(controller):
        creator_view = ParcelCreatorView(controller)
        return creator_view