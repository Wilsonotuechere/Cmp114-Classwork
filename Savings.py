from Atm import *


class SavingsAcc(Account):
    def withdraw(self, amt):
        if amt <= 5000:
            acc = Account()
            amount = acc.withdraw(amt)
            return amount
        else:
            return "limit exceeded"


action = True
savings = SavingsAcc()
from ATM import *


class SavingsAcc(Account):
    def withdraw(self, amt):
        if amt <= 5000:
            acc = Account()
            amount = acc.withdraw(amt)
            return amount
        else:
            return "limit exceeded"


action = True
savings = SavingsAcc()

print("welcome to access easymoni")
print('''
    options:
    withdraw
    deposit
    check balance
    check account number
    ''')

while action:
    choice = input("please select an option: ")
    if choice == "withdraw" or choice == "1":
        money = int(input("enter amount to withdraw: "))
        balance = savings.withdraw(amt=money)
        if balance != "limit exceeded":
            print(f"transaction successful, New bal: {balance}")
        else:
            print(balance)
    elif choice == "deposit" or choice == "2":
        money = int(input("enter amount to deposit: "))
        savings.deposit(money)
        print(f"deposit successful, New bal: {savings.account_balance}")
    elif choice == "check balance" or choice == "3":
        savings.get_bal()
    elif choice == "check account" or choice == "4":
        savings.get_acc()
    elif choice == "end transaction" or choice == "5":
        print(f"thank you {savings.name}")
        action = False
    else:
        print("invalid command, try again")

print("welcome to access easymoni")
print('''
    options:
    withdraw
    deposit

    ''')

while action:
    choice = input("please select an option: ")
    if choice == "withdraw" or choice == "1":
        money = int(input("enter amount to withdraw: "))
        balance = savings.withdraw(amt=money)
        if balance != "limit exceeded":
            print(f"transaction successful, New bal: {balance}")
        else:
            print(balance)
    elif choice == "deposit" or choice == "2":
        money = int(input("enter amount to deposit: "))
        savings.deposit(money)

    else:
        print("invalid command, try again")





