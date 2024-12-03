from lab.controller.UserParcelViewController import UserParcelViewController
from lab.controller.ParcelEditViewController import ParcelEditViewController
from lab.view.ViewsFactory import ViewsFactory
from lab.model.Parcel import Parcel


class OperatorParcelViewController(UserParcelViewController):
    def __init__(self):
        self.operator_percel_view = ViewsFactory.create_operator_parcel_view(controller=self)
        self.operator_percel_view.main()

    def edit_parcel(self):
        parcel_edit_view_c = ParcelEditViewController()


if __name__ == "__main__":
    upvc = OperatorParcelViewController()

