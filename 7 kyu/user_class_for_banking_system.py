"""A company is opening a bank, but the coder who is designing the user class made some errors.
They need you to help them.

You must include the following:

    A withdraw method
        Subtracts money from balance
        One parameter, money to withdraw
        Raise ValueError if there isn't enough money to withdraw
        Return a string with name and balence(see examples)

    A check method
        Adds money to baleance
        Two parameters, other user and money
        Other user will always be valid
        Raise a ValueError if other user doesn't have enough money
        Raise a ValueError if checking_account isn't true for other user
        Return a string with name and balance plus other name and other balance(see examples)

    An add_cash method
        Adds money to balance
        One parameter, money to add
        Return a string with name and balance(see examples)

Additional Notes:

    Checking_account should be stored as a boolean

    No input numbers will be negitive

    Output must end with period

    Float numbers will not be used so, balance should be integer

    No currency will be used

Examples:

Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, False)"""


class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def __str__(self):
        return "{} has {:d}.".format(self.name, self.balance)

    def withdraw(self, withdraw):
        if self.balance >= withdraw:
            self.balance -= withdraw
            return str(self)
        else:
            raise ValueError

    def check(self, other, pay):
        if pay > other.balance or not other.checking_account:
            raise ValueError
        self.add_cash(pay)
        other.withdraw(pay)
        return '{} has {:d} and {} has {:d}.'.format(self.name, self.balance, other.name, other.balance)

    def add_cash(self, cash):
        self.balance += cash
        return str(self)


if __name__ == "__main__":
    Jeff = User('Jeff', 80, True)
    Joe = User('Joe', 70, True)

    print(Joe.check(Jeff, 50))
    print(Jeff.withdraw(20))
    print(Jeff.add_cash(65))
