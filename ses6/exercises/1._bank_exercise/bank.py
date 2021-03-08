class Bank:
    # This class should contain knowledge about accounts

    def __init__(self):
        self.accounts = []


    def add_account(self, account):
        self.accounts.append(account)


    def __str__(self):
        tmp = ""
        for element in self.accounts:
            tmp += element.get_customer() + '\n' + element.get_balance() + '\n' + element.get_acc_number() + '\n'
        return tmp
        