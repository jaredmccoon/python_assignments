class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, ammount):
        self.account_balance += ammount
        return self
    def make_withdrawl(self, ammount):
        self.account_balance -= ammount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    def transfer_money(self, other_user, ammount):
        self.make_withdrawl(ammount)
        other_user.make_deposit(ammount)
        return self
user_1 = User("random_name_1")
user_2 = User("random_name_2")
user_3 = User("random_name_3")

user_1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawl(300).transfer_money(user_3, 300).display_user_balance()

user_2.make_deposit(100).make_deposit(200).make_withdrawl(300).make_withdrawl(300).display_user_balance()

user_3.make_deposit(100).make_withdrawl(200).make_withdrawl(300).make_withdrawl(300).display_user_balance()