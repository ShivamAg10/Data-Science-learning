## Design and create an online store for Products (name, price)
## Track total products being created.
## Create a static method to create a discount on each product based on a % parameter.

class Online_Store:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Online_Store.count += 1 
    
    def get_info(self):
        print(f"Product {self.name} is having price of {self.price}")
    
    @classmethod
    def total_prod(cls):
        print(f"Total products till now is {cls.count}")
    
    @staticmethod
    def calc_discount(price, discount_perc):
        discounted_price = price - (price * discount_perc / 100)
        print(discounted_price)

p1 = Online_Store("Bat", 2000)
p1.get_info()
p1.total_prod()

p2 = Online_Store("Bowl", 300)
p2.total_prod()

p1.total_prod()

p1.calc_discount(p1.price, 10)
p2.calc_discount(p2.price, 10)