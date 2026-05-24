## Create a BankAccount class with attributes account_number, owner_name and balance.
## Add methods to deposit, withdraw and check balance

class BankAccount:
    account_num = 100
    def __init__(self, owner_name):
        self.account_number = BankAccount.account_num + 1
        BankAccount.account_num += 1
        self.name = owner_name
        self.balance = 0
    
    def get_info(self):
        print(f""" Account Number: {self.account_number} 
            Owner Name: {self.name}
        """)
    
    def check_balance(self):
        print(f"Account Number {self.account_number} with name {self.name} having amount {self.balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} is deposited to the Bank Account number {self.account_number} with name {self.name}")
    
    def withdraw(self,amount):
        self.balance -= amount
        print(f"Amount {amount} is withdrawn to the Bank Account number {self.account_number} with name {self.name}")

A1 = BankAccount(input("Enter your name: "))
print(A1.account_number, A1.name)
A2 = BankAccount(input("Enter your name: "))
print(A2.account_number, A2.name)

A1.get_info()
A2.get_info()

A1.check_balance()
A2. check_balance()

A1.deposit(int(input("Enter amount deposited: ")))
A2.deposit(int(input("Enter amount deposited: ")))
A1.check_balance()
A2. check_balance()

A1.withdraw(int(input("Enter amount withdrawn: ")))
A2.withdraw(int(input("Enter amount withdrawn: ")))
A1.check_balance()
A2. check_balance()

print(A1.balance)