class Account:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount
            print(f"Deposit of {amount} accepted.New balance is {self.balance}")
        else:
            print("Oops invalid deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted.New balance: {self.balance}")
        else:
            print("Oops invalid withdraw or not enought fund")

check = Account("Kairat Nurtas")

check.deposit(200)
check.withdraw(50)
check.withdraw(180)
check.deposit(200)
check.withdraw(80)