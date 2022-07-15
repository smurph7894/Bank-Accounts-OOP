#Bank Account

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

#User
class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.account = None ## only works for single account instance
        self.user_accounts = {}

#has to be run first to connect accounts to user
    def set_account (self, account, account_name):
        self.user_accounts[account_name] = account
        print(self.user_accounts)
        return self

#once set account connected these will work 
    
    def display_info(self,account_name):
        print(self.name)
        print(self.email)
        print(f"{self.name}'s {account_name} balance is: ${self.user_accounts[account_name].balance}")
        return self

    def make_deposit (self, amount, account_name):
        deposit_value = self.__deposit(amount, account_name)
        print(deposit_value)
        return self

    def __deposit (self, amount, account_name):
        self.user_accounts[account_name].deposit(amount)
        return amount

    def make_withdrawal (self, amount, account_name):
        withdrawal_value = self.__withdrawal(amount, account_name)
        print(withdrawal_value)
        return self 

    def __withdrawal (self, amount, account_name):
        self.user_accounts[account_name].withdraw(amount)
        return amount   

    def display_user_balance(self):
        print(f"{self.name}'s account balances:")
        for account_key in self.user_accounts:
            print(f"{account_key}: $ {self.user_accounts[account_key].balance}")
        return self

    def transfer_money (self, amount, other_user, user_account_name, other_users_account_name):
        if self.user_accounts[user_account_name].balance >= amount:
            transfer_amount = self.__withdrawal(amount, user_account_name)
            #have to use make_deposit instead of __deposit because you can only use private functions on self.
            other_user.make_deposit(transfer_amount, other_users_account_name)
            print(f"{other_user.name}'s new {other_users_account_name} balance is {other_user.user_accounts[other_users_account_name].balance}")
            print(f"{self.name}'s new {user_account_name} balance is {self.user_accounts[user_account_name].balance}")
        else:
            print(f"{self.name} does not have succient funds for transfer.")
        

sarah = user("Sarah", "murphs@dojo.com")
beth = user("Beth", "Hums@email.com")
roger = user("Roger","grig@email.com")

print("*****")
#should not use variable in first arguement or it will use the same account for all users
sarah.set_account(BankAccount(), "savings_account1")
sarah.set_account(BankAccount(), "checking_account1")


print("*****")
sarah.make_deposit(140, "savings_account1").make_withdrawal(20, "savings_account1")


print("*****")
sarah.make_deposit(20, "checking_account1")


print("*****")
sarah.display_user_balance()


print("*****")
beth.set_account(BankAccount(), "savings_account1")
beth.set_account(BankAccount(), "checking_account1")


print("*****")
beth.display_user_balance()


print("*****")
beth.make_deposit(40, "savings_account1")
beth.make_deposit(60, "savings_account1")


print("*****")
beth.make_deposit(100, "checking_account1")


print("*****")
beth.display_info("savings_account1")


print("*****")
beth.display_user_balance()


print("*****")
sarah.display_user_balance()


print("*****")
beth.transfer_money(20,sarah,"savings_account1","savings_account1")