class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, ammount):
        self.account.deposit(ammount)
        return self
    def make_withdrawl(self, ammount):
        self.account.withdraw(ammount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self
    def transfer_money(self, other_user, ammount):
        self.account.withdraw(ammount)
        other_user.account.deposit(ammount)
        return self


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




user_1 = User("random_name_1")
user_2 = User("random_name_2")
user_3 = User("random_name_3")

user_1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawl(300).transfer_money(user_3, 300).display_user_balance()

user_2.make_deposit(100).make_deposit(200).make_withdrawl(300).make_withdrawl(300).display_user_balance()

user_3.make_deposit(100).make_withdrawl(200).make_withdrawl(300).make_withdrawl(300).display_user_balance()