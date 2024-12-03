from lab.view.ViewsFactory import ViewsFactory
from lab.model.ParselStorage import ParcelStorage
from lab.model.DataSaver import DataSaver
from lab.model.ParcelFactory import ParcelFactory
from tkinter import messagebox


class ParcelCreatorController:
    def __init__(self):
        self.parcle_storage = ParcelStorage
        self.data_saver = DataSaver
        self.parcel_creator_view = ViewsFactory.create_parcel_creator_view(self)
        self.parcel_creator_view.main()

    def create_parcel(self):
        messagebox.showinfo("Уведомление", "Посылка успешно добавлена!")
        self.parcel_creator_view.destroy()

if __name__ == "__main__":
    app = ParcelCreatorController()