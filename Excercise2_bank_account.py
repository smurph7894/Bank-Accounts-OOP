
import re


class BankAccount:
    bank_name = "Dojo Bank"

    all_accounts = []

    def __init__(self, balance = 0, int_rate = .01):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)

    def deposit (self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw (self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("insufficient funds:Charging a $5 fee")
            self.balance = self.balance - (amount+5) 
        return self

    def display_account_info(self):
        print (f"Balance is ${self.balance}")
        print (f"Interest Rate is: {self.int_rate}%")
        return self

    def yield_interest (self):
        if self.balance >= 0:
            self.balance = self.balance * (1 + self.int_rate)
            return self
        else:
            print("insuffient funds")
            return self
    
    @classmethod
    def print_all_accounts_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()



savings_account = BankAccount()
checking_account = BankAccount()

print("savings")
savings_account.deposit(50).deposit(20).deposit(30).withdraw( 40).yield_interest().display_account_info()
print("checking")
checking_account.deposit(160).deposit(10).withdraw(10).withdraw(40).withdraw(20).yield_interest().display_account_info()


BankAccount.print_all_accounts_info()