class Customer():
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    def balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

customer1 = Customer('Vishal',500)     # creating Instance of class

print(f"Available Balance is : {customer1.balance}")
customer1.deposit(500)
print(f"Available Balance is : {customer1.balance}")
customer1.withdraw(2000)
print(f"Available Balance is : {customer1.balance}")