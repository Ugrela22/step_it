#1



class Car:

    def __init__(self, brand, model, creation_year):
        self.brand = brand
        self.model = model
        self.creation_year = creation_year

    
    def car_info(self):
        print(f"{"="*25}\nCar Brand: {self.brand}\n{"="*25}\nModel: {self.model}\n{"="*25}\nCreation Year: {self.creation_year}\n{"="*25}")



car1 = Car(brand= "Audi", model = "R8", creation_year=2025)

car1.car_info()

#2

class Car:

    def __init__(self, brand, model, creation_year):
        self.brand = brand
        self.model = model
        self.creation_year = creation_year

    
    def car_info(self):
        print(f"{"="*25}\nCar Brand: {self.brand}\n{"="*25}\nModel: {self.model}\n{"="*25}\nCreation Year: {self.creation_year}\n{"="*25}")

        Car.car_age(car1)

    def car_age(self):
        today = 2025

        try:
            print(f"Car is {today - self.creation_year} years old\n{"="*25}")
        except TypeError:
            print("Creation year shoud be always a number!!")



car1 = Car(brand= "Audi", model = "R8", creation_year = 2015)

car1.car_info()

#3

class ElectricCar(Car):

    def __init__(self, brand, model, creation_year, battery_life):
        super().__init__(brand, model, creation_year)
        self.battery_life = battery_life

    
    def battery_info(self):
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი")

    

ect_car1 = ElectricCar("Tesla", "ModelX", 2021, 100)

ect_car1.battery_info()

#4


class Car:

    number_of_cars = 0

    def __init__(self, brand, model, creation_year):
        self.brand = brand
        self.model = model
        self.creation_year = creation_year
        Car.number_of_cars += 1

    
    def car_info(self):
        print(f"{"="*25}\nCar Brand: {self.brand}\n{"="*25}\nModel: {self.model}\n{"="*25}\nCreation Year: {self.creation_year}\n{"="*25}")

        




car1 = Car(brand= "Audi", model = "R8", creation_year = 2015)
car2 = Car(brand= "Porsche", model = "911", creation_year = 2015)
car1.car_info()

#5 

class Car:

    number_of_cars = 0

    def __init__(self, brand, model, creation_year):
        self.brand = brand
        self.model = model
        self.creation_year = creation_year
        Car.number_of_cars += 1

    
    def car_info(self):
        print(f"{"="*25}\nCar Brand: {self.brand}\n{"="*25}\nModel: {self.model}\n{"="*25}\nCreation Year: {self.creation_year}\n{"="*25}")

    def total_cars(self):
        print(f"Total Number Of Cars: {self.number_of_cars}")



car1 = Car(brand= "Audi", model = "R8", creation_year = 2015)
car2 = Car(brand= "Porsche", model = "911", creation_year = 2015)

car1.total_cars()



        
