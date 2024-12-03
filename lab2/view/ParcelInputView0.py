import tkinter as tk
from tkinter import ttk


class ParcelInputView0(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Поиск посылки")
        self.geometry("800x600")
        self.configure(bg='ghost white')

    def show_info(self):
        self.style = ttk.Style()
        self.style.configure("TButton", foreground="RoyalBlue4", background='RoyalBlue4', font=("Helvetica", 12),
                             padding=10)

        self.dark_square = tk.Frame(self, width=500, height=200, bg='SlateGray2')
        self.dark_square.place(relx=0.5, rely=0.5, anchor='center')

        self.label = tk.Label(self.dark_square, text="Где моя посылка?", bg='SlateGray2',
                              font=("Segoe UI Semibold", 16))
        self.label.place(relx=0.5, rely=0.15, anchor="center")

        self.label_smol = tk.Label(self.dark_square,
                                   text="Чтобы найти посылку, введите трек-номер,\n полученный при оформлении",
                                   bg='SlateGray2', font=('Segoe UI Semibold', 8))
        self.label_smol.place(relx=0.5, rely=0.4, anchor='center')

        self.entry = tk.Entry(self, width=40)
        self.entry.place(relx=0.25, rely=0.55)

    def add_find_bttn(self):
        self.button = ttk.Button(self, text="Найти посылку", style="TButton", command= lambda: self.controller.open_operator_view())
        self.button.place(relx=0.60, rely=0.53)

    def add_parcel_bttn(self):
        self.button_log_in = ttk.Button(self, text="Добавить посылку", command=lambda: self.controller.create())
        self.button_log_in.place(relx=0.5, rely=0.72, anchor='center')

    def main(self):
        self.show_info()
        self.add_parcel_bttn()
        self.add_find_bttn()
        self.mainloop()
        
    

if __name__ == "__main__":
    app = ParcelInputView0('controller')
    app.main()