import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class ParcelCreatorView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.configure(bg='LightSteelBlue1')
        self.title("Создание посылки")
        self.geometry("800x600")

    def create_widgets(self):
        self.entries = []
        # Первая колонка
        label0 = tk.Label(self, text="Добавление посылки", bg='LightSteelBlue1', font=("Segoe UI Semibold", 20),foreground='RoyalBlue4')
        label0.place( y=10, x=230)
        label1 = tk.Label(self, text="Трек-номер послыки", bg='LightSteelBlue1')
        label1.place(x=10, y=60)
        entry1 = tk.Entry(self, width=50)
        entry1.insert(0, "UX123888948XU")
        entry1.place(x=10, y=80)
        self.entries.append(entry1)

        label2 = tk.Label(self, text="Текущий статус", bg='LightSteelBlue1')
        label2.place(x=10, y=130)
        entry2 = tk.Entry(self, width=50)
        entry2.insert(0, "Отправлено")
        entry2.place(x=10, y=150)
        self.entries.append(entry2)

        label3 = tk.Label(self, text="Ориентировочная дата доставки", bg='LightSteelBlue1')
        label3.place(x=10, y=200)
        entry3 = DateEntry(self, width=50, date_pattern='dd.MM.yyyy')
        entry3.place(x=10, y=220)
        self.entries.append(entry3)

        # Вторая колонка
        label4 = tk.Label(self, text="Имя отправителя", bg='LightSteelBlue1')
        label4.place(x=400, y=60)
        entry4 = tk.Entry(self, width=50)
        entry4.insert(0, "Дарья Демидовец")
        entry4.place(x=400, y=80)
        self.entries.append(entry4)

        label5 = tk.Label(self, text="Имя получателя", bg='LightSteelBlue1')
        label5.place(x=400, y=130)
        entry5 = tk.Entry(self, width=50)
        entry5.insert(0, "София Борикова")
        entry5.place(x=400, y=150)
        self.entries.append(entry5)

        label6 = tk.Label(self, text="Адрес доставки", bg='LightSteelBlue1')
        label6.place(x=400, y=200)
        entry6 = tk.Entry(self, width=50)
        entry6.insert(0, "г. Минск, ул. Гикало, 9")
        entry6.place(x=400, y=220)
        self.entries.append(entry6)

        # Кнопка
        self.style = ttk.Style()
        self.style.configure("TButton", foreground="RoyalBlue4", background='RoyalBlue4', font=("Helvetica", 10),
                             padding=7)

        self.add_button = ttk.Button(self, text="Добавить посылку", style='TButton', command=lambda: self.controller.create_parcel())
        self.add_button.place(x=200, y=300, width=340, height=40)

    def main(self):
        self.create_widgets()
        self.mainloop()


if __name__ == "__main__":
    app = ParcelCreatorView()
    app.mainloop()
