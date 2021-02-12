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

    def __init__(self, num, person):
        self.balance = 0
        self.number = num
        self.holder = person

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (self.balance - amount) < -1000:
            print("Operation is not possible: insufficient funds")
        else:
            self.balance -= amount

    def print_info(self):
        print(self.holder + "'s balance is " + str(self.balance) + " dollars.")

    def set_num(self, num):
        self.number = num

    def set_holder(self, person):
        self.holder = person

    def apply_interest(self):
        self.balance = self.balance + (self.balance*0.15)

    def __str__(self):
        res = "***AccountInfo***\n"
        res += "AccountID:" + str(self.number) + "\n"
        res += "Holder:" + self.holder + "\n"
        res += "Balance:" + str(self.balance) + "\n"
        return res


if __name__ == "__main__":
    print("Welcome to the Python Bank!")
    franksAcc = Account(1, "Frank")
    franksAcc.balance = 100
    franksAcc.print_info()
    franksAcc.set_holder("Francis")
    franksAcc.print_info()
    franksAcc.apply_interest()
    franksAcc.print_info()
    print(franksAcc)
