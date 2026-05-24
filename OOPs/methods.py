class Laptop:
    storage_type = "ssd"
    
    def __init__(self,RAM, storage):
        self.RAM = RAM
        self.storage = storage
    
    @classmethod # decorator
    def get_storage_type(cls): # class method
        return f"Storage type of laptop is {cls.storage_type}"
    
    def get_info(self): #instance method
        return (f"Laptop has {self.RAM} RAM and {self.storage} {self.storage_type}")
    
    @staticmethod # decorator
    def calc_discount(price, discount): # static method
        final_price = price - (discount * price / 100)
        print(f"discounted price = {final_price}")

lappy1 = Laptop("16gb", "512gb")
lappy2 = Laptop("8gb", "256gb")
# print(lappy1.get_info())
# print(lappy1.get_storage_type())
lappy1.calc_discount(40_000, 10)