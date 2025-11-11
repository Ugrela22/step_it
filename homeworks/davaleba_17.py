#1 

class Vector:

    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
        


vec1 = Vector(6, 4)
vec2 = Vector(6, 7)
vec3 = vec1.__add__(vec2)     

print(vec3)

#2

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    
    def __eq__(self, value):
        return True if self.title == value.title and self.author == value.author else False
    

book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')

print(book1.__eq__(book2))
print(book1.__eq__(book3))

#3

import sys

class Car:

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, brand, model, year):
        self.set_brand(brand)
        self.set_model(model)
        self.set_year(year)

    def set_brand(self, new_brand):
        self.brand = new_brand if type(new_brand) == (str) and new_brand != "" else "Wrong type of input"
    
    def set_model(self, new_model):
        self.model = new_model if type(new_model) == (str) and new_model != "" else "Wrong type of input"
        
    def set_year(self, new_year):
        
        self.year = new_year if type(new_year) == (int) and new_year in range(1850, 2026) else "Wrong type of input"
        
        
    def get_brand(self):
        return self.brand
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    
    def __str__(self):
        return f"{self.brand}, {self.model}, {self.year}"

car1 = Car("Nissan", "Skyline", 2025)

print(car1)



    



        
        

