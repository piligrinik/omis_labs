import tkinter as tk
from tkinter import ttk


class LoginView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.style = ttk.Style()
        self.style.configure("TButton", foreground="RoyalBlue4", background='RoyalBlue4', font=("Helvetica", 10),
                             padding=6)
        
    def show(self):

        self.title("Авторизация")
        self.geometry("800x600")
        self.configure(bg='ghost white')

        self.frame = tk.Frame(self, bg="LightSteelBlue1", bd=5)
        self.frame.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.1)

        self.login_label = tk.Label(self.frame, text="email", bg="LightSteelBlue1", font=("Segoe UI", 12))
        self.login_label.place(relx=0.4, rely=0.2)
        self.login_entry = ttk.Entry(self.frame)
        self.login_entry.place(relx=0.4, rely=0.3)
        self.login_entry.insert(0, "nosova@email.com")

        self.password_label = tk.Label(self.frame, text="Пароль:", bg="LightSteelBlue1", font=("Segoe UI", 12))
        self.password_label.place(relx=0.4, rely=0.4)
        self.password_entry = ttk.Entry(self.frame, show='*')
        self.password_entry.place(relx=0.4, rely=0.5)
        self.password_entry.insert(0, "Введите пароль")

        self.login_button = ttk.Button(self.frame, style="TButton",  text="Войти как оператор", command=lambda: self.destroy())
        self.login_button.place(relx=0.4, rely=0.7)

        # Register button below the frame
        self.register_button = ttk.Button(self, style="TButton", text="Зарегистрироваться", command=lambda: self.destroy())
        self.register_button.place(relx=0.1, rely=0.7, relwidth=0.8)

    def main(self):
        self.show()
        self.mainloop()

if __name__ == "__main__":
    app = LoginView()
    app.mainloop()
