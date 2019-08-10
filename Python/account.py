class Account:

    def __init__(self, name="", balance=0):
        self.owner = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
        else:
            print("Insufficient Funds!")

    def __str__(self):
        return(f"str: {self.owner} has ${self.balance} to his/her name.")

a = Account("Hugh", 0)
print(a)
#print(f"Name: {a.owner}, Balance: {a.balance}")
a.deposit(100)
print(a)
#print(f"Name: {a.owner}, Balance: {a.balance}")
a.withdrawal(50)
#print(f"Name: {a.owner}, Balance: {a.balance}")
print(a)
a.withdrawal(50)
print(a)
#print(f"Name: {a.owner}, Balance: {a.balance}")
a.deposit(25)
print(a)
#print(f"Name: {a.owner}, Balance: {a.balance}")
a.withdrawal(26)
print(a)
#print(f"Name: {a.owner}, Balance: {a.balance}")
