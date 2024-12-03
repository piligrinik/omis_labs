import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from lab.view.UserParcelView import UserParcelView



class OperatorParcelView(UserParcelView):
    def __init__(self, controller):
        super().__init__(controller)

    def add_edit_delete_bttns(self):
        self.style = ttk.Style()
        self.style.configure("TButton", foreground="RoyalBlue4", background='RoyalBlue4', font=("Helvetica", 10),
                             padding=7)
        self.edit_bttn = ttk.Button(self, text="Редактировать посылку", style="TButton", command=lambda: self.controller.edit_parcel())
        self.edit_bttn.place(relx=0.3, rely=0.7)
        self.delete_bttn = ttk.Button(self, text="Удалить посылку", style="TButton",  command=lambda: self.delete_btn())
        self.delete_bttn.place(relx=0.6, rely=0.7)

    def delete_btn(self):
        messagebox.showinfo("Уведомление", "Посылка успешно удалена!")
        self.destroy()


    def main(self):
        self.show_info()
        self.add_edit_delete_bttns()
        self.mainloop()


if __name__ == "__main__":
    app = OperatorParcelView()
    app.main()