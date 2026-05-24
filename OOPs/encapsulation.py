## Create a BankAccount class with attributes account_number, owner_name and balance.
## Add methods to deposit, withdraw and check balance

class BankAccount:
    account_num = 100
    def __init__(self, owner_name):
        self._account_number = BankAccount.account_num + 1 #Protected attribute 
        BankAccount.account_num += 1
        self.name = owner_name #public attribute
        self.__balance = 0 # Private attribute
    
    def get_info(self):
        print(f""" Account Number: {self._account_number} 
            Owner Name: {self.name}
        """)
    
    def check_balance(self): # getter function
        print(f"Account Number {self._account_number} with name {self.name} having amount {self.__balance}")
    
    def deposit(self, amount): # setter function
        self.__balance += amount
        print(f"Amount {amount} is deposited to the Bank Account number {self._account_number} with name {self.name}")
    
    def withdraw(self,amount): # setter function
        self.__balance -= amount
        print(f"Amount {amount} is withdrawn to the Bank Account number {self._account_number} with name {self.name}")

A1 = BankAccount(input("Enter your name: "))
print(A1._account_number, A1.name)
A2 = BankAccount(input("Enter your name: "))
print(A2._account_number, A2.name)

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

# print(A1.__balance)
## Can't be accessed

print(A1._BankAccount.__balance)
## Can be accessed