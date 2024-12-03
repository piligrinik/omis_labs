class Account:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def try_autificate(self):
        return True
        