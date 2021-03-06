# Exercise 7.1
# Create a class Account and an __init__ constructor method
# that takes (after self) two additional parameters:
# - balance (representing the account balance, e.g. 1000)
# - type (representing the type of account, e.g. "savings")

# Exercise 7.2
# Create three class methods:
# - withdraw (taking, next to self, one argument amount)
#   that withdraws the given amount from the balance
# - deposit (taking, next to self, one argument amount)
#   that deposits the given amount to the balance
# - add_interest (taking, next to self, one argument interest_rate)
#   that adds the given interest rate to the amount (where e.g. 0.05 represent 5%)
#   but ONLY if the account type equals "savings"

# Exercise 7.3
# Create a new instance of the Account class with an initial balance of 1000
# and account type equal to "savings"
# Then:
# 1. Withdraw 500
# 2. Deposit 750
# 3. Add 5% interest
# 4. Print the resulting balance

# Exercise 7.4
# Create another instance of the Account class with an initial balance of 1000
# but now with account type "checking"
# Then:
# 1. Withdraw 500
# 2. Deposit 750
# 3. Add 5% interest
# 4. Print the resulting balance
# Is the outcome different? (Hint: it should be...)

class Account:
    def __init__(self, balance, type):
        self.balance = balance
        self.type = type

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def add_interest(self, interest_rate):
        if self.type == "savings":
            self.balance *= (1 + interest_rate)

my_account = Account(1000, "savings")
my_account.withdraw(500)
my_account.deposit(750)
my_account.add_interest(0.05)
print(my_account.balance)

my_other_account = Account(1000, "checking")
my_other_account.withdraw(500)
my_other_account.deposit(750)
my_other_account.add_interest(0.05)
print(my_other_account.balance)