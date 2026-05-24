''' 
    Create a class Book with the following attributes:
        title 
        author 
        list of reviews
    
    And add methods:
        add a new review
        count reviews
        display all reviews
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []
    
    def get_info(self):
        print(f"Author: {self.author}, Title: {self.title}")
    
    def add_review(self, review):
        self.reviews.append(review)
    
    def count_review(self):
        print("Total Number of reviews are: ", len(self.reviews))
    
    def display_all_reviews(self):
        for i in self.reviews:
            print(i)

b1 = Book(input("Enter Title of Book: "), input("Enter Author of Book: "))
b2 = Book(input("Enter Title of Book: "), input("Enter Author of Book: "))
b1.get_info()
b2.get_info()

num = int(input("Enter How many reviews you want to enter: "))
for i in range(num):
    b1.add_review(input("Enter a reveiw: "))

num = int(input("Enter How many reviews you want to enter: "))
for i in range(num):
    b2.add_review(input("Enter a reveiw: "))

b1.count_review()
b2. count_review()

b1.display_all_reviews()
b2. display_all_reviews()