from lab.view.ViewsFactory import ViewsFactory
from lab.model.AccountStorage import AccountStorage
from lab.model.CurrentSession import CurrentSession
from lab.model.AccountFactory import AccountFactory
from lab.model.DataSaver import DataSaver


class AccountLoginController:
    def __init__(self):
        self.account_storage = AccountStorage
        self.account_factory = AccountFactory
        self.data_saver = DataSaver
        self.current_session = CurrentSession
        self.login_view = ViewsFactory.create_login_view(self)
        
    def login_view_start(self):
        self.login_view.main()
        return 0