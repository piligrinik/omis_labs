from lab.model.Parcel import Parcel
from lab.view.ViewsFactory import ViewsFactory


class ParcelEditViewController:
    def __init__(self):
        self.parcel_edit_view = ViewsFactory.create_parcel_edit_view(controller=self)
        self.parcel_edit_view.main()