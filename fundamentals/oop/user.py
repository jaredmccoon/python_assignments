class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, ammount):
        self.account_balance += ammount
    def make_withdrawl(self, ammount):
        self.account_balance -= ammount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    def transfer_money(self, other_user, ammount):
        self.make_withdrawl(ammount)
        other_user.make_deposit(ammount)
user_1 = User("random_name_1")
user_2 = User("random_name_2")
user_3 = User("random_name_3")


user_1.make_deposit(100)
user_1.make_deposit(200)
user_1.make_deposit(300)
user_1.make_withdrawl(300)
user_1.transfer_money(user_3, 300)
user_1.display_user_balance()

user_2.make_deposit(100)
user_2.make_deposit(200)
user_2.make_withdrawl(300)
user_2.make_withdrawl(300)
user_2.display_user_balance()

user_3.make_deposit(100)
user_3.make_withdrawl(200)
user_3.make_withdrawl(300)
user_3.make_withdrawl(300)
user_3.display_user_balance()

