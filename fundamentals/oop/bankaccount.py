class BankAccount:

    def __init__(self, int_rate: float, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            temp = self.balance * self.int_rate
            self.balance += temp
        return self

user1 = BankAccount(0.01)
user2 = BankAccount(0.01)

user1.deposit(300).deposit(300).deposit(300).withdraw(300).yield_interest().display_account_info()
user2.deposit(300).deposit(300).withdraw(300).withdraw(300).withdraw(300).withdraw(300).yield_interest().display_account_info()