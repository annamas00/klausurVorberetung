"""Exercise 1: (5 points)

a) Using the slides & the script, put together a file containing the
   complete Account class.  Each method must have a documentation
   string at the beginning which describes what the method is doing.
   (1 point)

b) Create a main application where you create a number of accounts.
   Play around with depositing / withdrawing money.  Change the
   account holder of an account using a setter method.  (1 point)

c) Change the withdraw function such that the minimum balance allowed
   is -1000.  (1 point)

d) Write a function apply_interest(self) which applies an interest
   rate of 1.5% to the current balance and call it on your objects.
   (1 point)

e) Implement the __str__ magic method and use it to print accounts.
   (1 point)
"""


class Account:
    """ Here has to be a documentation string that describes
    which data objects this class is designed for.
    You have to remove the pass statement and then write some
    code for the class. """
    pass

    def __init__(self, accountNumber, holder, balance = 0):
        self.accountNumber = accountNumber
        self.holder = holder
        self.balance = balance

    def depositing (self, amount):
        self.balance = self.balance + amount
        return amount
    def withdrawing(self, amount):
        self.balance = self.balance - amount
        if amount > self.balance:
            amount = self.balance
            return amount
        self.balance = self.balance - amount
        return amount
    def set_holder(self, holder):
        self.holder=holder
    def apply_interest(self, rate = 0.015):
        self.balance = self.balance+rate
    def __str__(self):
        res = "Account Info about current owner: \n"
        res += "Account ID: " + str(self.number) + "\n"
        res += "Holder:" + self.holder + "\n"
        res += "Balance: " + str(self.balance) + "\n"
        return res

if __name__ == "__main__":
    print("Welcome to the Python Bank!")
    annesAccount = Account(1, "Anne")
    annesAccount.balance = 1000
    print("1) Balance Anne:", annesAccount.balance)
    cash1 = annesAccount.withdraw(1500)  # ???
    print("2) For withdrawing: ", cash1)
    print("3) Balance Anne after withdraw:", annesAccount.balance)
    # annesAcc.print_info()
    annesAccount.set_holder("Stefan")
    print("4) Now ist the holder of the accoun is ", annesAccount.holder)
    print("5) ", annesAccount)


