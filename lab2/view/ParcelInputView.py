import tkinter as tk
from tkinter import ttk
from lab.view.ParcelInputView0 import ParcelInputView0


class ParcelInputView(ParcelInputView0):
    def __init__(self, controller):
        super().__init__(controller)             # needs to be deleted later

    def add_find_bttn(self):
        self.button = ttk.Button(self, text="Найти посылку", style="TButton", command= lambda: self.controller.open_user_view())
        self.button.place(relx=0.60, rely=0.53)

    def login_bttn(self):
        self.button_log_in = ttk.Button(self, text="Войти как оператор", command=lambda: self.controller.authorize())
        self.button_log_in.place(relx=0.5, rely=0.72, anchor='center')


    def main(self):
        self.show_info()
        self.login_bttn()
        self.add_find_bttn()
        self.mainloop()



if __name__ == "__main__":
    app = ParcelInputView('controller')
    app.main()
