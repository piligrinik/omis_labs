from .Account import Account
from .DataSaver import DataSaver
from .Saveable import Saveable

class AccountStorage(Saveable):
    def __init__(self):
        self.accounts = dict()

    def add(self, account: Account):
        pass

    def find_account(self, login: str):
        pass

    def load(self, data_svr: DataSaver):
        pass

    def save(self, data_svr: DataSaver):
        pass

