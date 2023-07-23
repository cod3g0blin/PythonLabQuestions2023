"""Create a bank account class that represents a simple bank account. The class should have the following attributes and methods.
Attributes: (acc_no,acc_holder, balance)
methods: deposit, withdraw, get_balance, display_acc_info"""

class BankAccount:
    def __init__(self, acc_no, acc_holder, balance):
        self.acc_no = acc_no
        self.acc_holder = acc_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance<amount:
            print("Insufficient Balance.")
            return
        self.balance -= amount
    
    def getBalance(self):
        return self.balance

    def displayAccountInfo(self):
        print(f"Account Number:\t{self.acc_no}")
        print(f"Account holder:\t{self.acc_holder}")
        print(f"Balance:\t{self.balance}")

acc = BankAccount("3389582", "Shubham", 5000)
acc.displayAccountInfo()
acc.deposit(5000)
acc.displayAccountInfo()

