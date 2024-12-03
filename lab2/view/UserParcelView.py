import tkinter as tk
from tkinter import ttk


class UserParcelView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Отслеживание посылку")
        self.geometry("800x600")
        self.configure(bg='ghost white')

    def show_info(self):
        statuses, date = self.controller.show()
        self.dark_square = tk.Frame(self, width=650, height=450, bg='LightSteelBlue1')
        self.dark_square.place(relx=0.5, rely=0.5, anchor='center')
        self.style = ttk.Style()
        self.style.configure("TButton", foreground="RoyalBlue4", background='RoyalBlue4', font=("Helvetica", 10),
                             padding=7)
        self.label = tk.Label(self.dark_square, text=f"В пути,", bg="LightSteelBlue1" ,foreground='RoyalBlue4',
                              font=("Segoe UI Semibold", 25))
        self.label.place(relx=0.18, rely=0.15, anchor="center")
        self.label_smol = tk.Label(self.dark_square, text=f" привезем до {date}", bg="LightSteelBlue1" ,foreground='RoyalBlue4',
                              font=("Segoe UI Semibold", 12))
        self.label_smol.place(relx=0.42, rely=0.165, anchor="center")
        self.label_status = tk.Label(self.dark_square, text=f"Текущий статус: {statuses[-1]}", bg="LightSteelBlue1" ,foreground='RoyalBlue4',
                              font=("Segoe UI Semibold", 15))
        self.label_status.place(relx=0.10, rely = 0.3)
        self.all_status_bttn = ttk.Button(self.dark_square, text="Показать все статусы", style="TButton", command=lambda: self.show_statuses(statuses))
        self.all_status_bttn.place(relx=0.6, rely=0.3)

    def show_statuses(self, statuses):
        y_position = 270
        for i, status in enumerate(statuses):
            label = tk.Label(self, text=status, bg='LightSteelBlue1', font=("Segoe UI Semibold", 15),foreground='RoyalBlue4')
            label.place(x=445, y=y_position, width=200, anchor="w")
            y_position += 40

    def main(self):
        self.show_info()
        self.mainloop()


if __name__ == "__main__":
    app = UserParcelView('controller')
    app.main()