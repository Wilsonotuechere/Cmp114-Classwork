from Atm import *


class CurrentAcc(Account):

    def __init__(self):
        # Account.__init__(self)
        super().__init__()
        self.account_number = 9011223423


current_acc = CurrentAcc()
current_acc.deposit(amt=1000)

print(current_acc.account_balance)

