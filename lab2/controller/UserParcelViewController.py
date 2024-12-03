from lab.view.ViewsFactory import ViewsFactory
from lab.model.Parcel import Parcel


class UserParcelViewController:
    def __init__(self):
        self.user_parcel_view = ViewsFactory.create_user_parcel_view(controller=self)
        self.user_parcel_view.main()
    def show(self):
        self.statuses = ["Оформлено", "Готово к отправке", "Отправлено"]
        self.date = "14 декабря"
        return self.statuses, self.date


if __name__ == "__main__":
    upvc = UserParcelViewController()
    