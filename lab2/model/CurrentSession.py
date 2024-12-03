from .Account import Account


class CurrentSession:
    def __init__(self):
        self.is_authorizd = False

    def is_authorized(self):
        self.is_authorizd = True
        return self.is_authorizd

    def log_in(self, account: Account):
        self.account = account

    def log_out(self):
        self.is_authorizd = False