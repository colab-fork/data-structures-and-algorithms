#instance methods - perform behavior on instance variables

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, amount):
        if self.balance >= amount:
           self.balance -= amount
        else:
            raise ValueError("Insufficient Funds")
            
    def deposit(self, amount):
        self.balance += amount

account = BankAccount(2000)
account.deposit(3000)
account.withdraw(6000)


print(account.balance)
