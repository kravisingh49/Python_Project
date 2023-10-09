## blue print for creating bank objects.

class bank:

    def __init__(self, x, y, z):
        self.account_number = x
        self.initial_deposit = y
        self.account_balance = y
        self.name = z
        print("Thankyou for creating an account with us,",self.name)

    def withdraw(self, amt):
        if self.account_balance >= amt:
            self.acount_balance = self.account_balance - amt
            print(f"Your account has been debited with {amt} dollars")
            print(f"Your new account balance is {self.account_balance} dollars")
        else:
            print("you do not have enough balance")


    def deposit(self, amt):
        self.account_balance = self.account_balance + amt
        print(f"Your account has been credited with {amt} dollars")
        print(f"Your new account balance is {self.account_balance} dollars")

    def check_balance(self):
        print("Welcome", self.name)
        print(f"your account balance is {self.account_balance} dollars")

objj= bank(245026, 500, "Ravi Kumar")
objp= bank(245028, 1000, "Mradu Rathore")
