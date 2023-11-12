# EX 1
# import math

# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def get_area(self):
#         pass
#     def get_perimeter(self):
#         pass
#     def get_sides(self):
#         pass
#     def print_info(self):
#         print( f"Shape at position ({self.x},{self.y}) with area {self.get_area()} and perimeter {self.get_perimeter()}")

# class Circle(Shape):
#     def __init__(self, x, y, r):
#         super().__init__(x, y)
#         self.r = r
#     def get_area(self):
#         return math.pi * self.r**2
#     def get_perimeter(self):
#         return 2 * math.pi * self.r
#     def get_sides(self):
#         return float('inf')
#     def print_info(self):
#         return super().print_info()
    
# class Rectangle(Shape):
#     def __init__(self, x, y, w, h):
#         super().__init__(x, y)
#         self.w = w
#         self.h = h
#     def get_area(self):
#         return self.w * self.h
#     def get_perimeter(self):
#         return self.w * 2 + self.h * 2
#     def get_sides(self):
#         return 4
#     def print_info(self):
#         return super().print_info()
    
# class Triangle(Shape):
#     def __init__(self, x, y, side1, side2, side3):
#         super().__init__(x, y)
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#     def get_area(self):
#         s = (self.side1 + self.side2 + self.side3) / 2
#         return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
#     def get_perimeter(self):
#         return self.side1 + self.side2 + self.side3
#     def get_sides(self):
#         return 3
#     def print_info(self):
#         return super().print_info()
    
# shapes = [Circle(0, 0, 6), Rectangle(1, 2, 5, 4), Triangle(1, 1, 4, 4, 4)]
# for shape in shapes:
#     shape.print_info()
#     print(shape.get_area())
#     print(shape.get_perimeter())
#     print(shape.get_sides())


# EX 2

# class Account:
#     def __init__(self, account_number, account_holder, balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposit: ${amount} successful. New balance: ${self.balance}")
#         else:
#             print("Invalid")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawal: ${amount} successful. New balance: ${self.balance}")
#         else:
#             print("Invalid withdrawal amount or insufficient funds.")

#     def calculate_interest(self):
#         pass


# class SavingsAccount(Account):
#     def __init__(self, account_number, account_holder, balance, interest_rate):
#         super().__init__(account_number, account_holder, balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate
#         self.deposit(interest)
#         print(f"Interest of ${interest} calculated and deposited. New balance: ${self.balance}")


# class CheckingAccount(Account):
#     def __init__(self, account_number, account_holder, balance, overdraft_limit):
#         super().__init__(account_number, account_holder, balance)
#         self.overdraft_limit = overdraft_limit

#     def withdraw(self, amount):
#         if 0 < amount <= (self.balance + self.overdraft_limit):
#             self.balance -= amount
#             print(f"Withdrawal: ${amount} successful. New balance: ${self.balance}")
#         else:
#             print("Invalid withdrawal amount or overdraft limit reached.")

# savings_account = SavingsAccount("RO3628", "Stefan Casuneanu", 1000, 0.02)

# savings_account.deposit(500)
# savings_account.withdraw(200)

# savings_account.calculate_interest()

# checking_account = CheckingAccount("RO3629", "Stefan Casuneanu", 500, 200)

# checking_account.deposit(300)
# checking_account.withdraw(1000)
# checking_account.deposit(100)
# checking_account.withdraw(400)


# EX 3

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.make} {self.model}")

# class Car(Vehicle):
#     def __init__(self, make, model, year, fuel_efficiency):
#         super().__init__(make, model, year)
#         self.fuel_efficiency = fuel_efficiency

#     def calculate_mileage(self, distance):
#         return distance / self.fuel_efficiency

# class Motorcycle(Vehicle):
#     def __init__(self, make, model, year, fuel_efficiency):
#         super().__init__(make, model, year)
#         self.fuel_efficiency = fuel_efficiency

#     def calculate_mileage(self, distance):
#         return distance / self.fuel_efficiency

# class Truck(Vehicle):
#     def __init__(self, make, model, year, towing_capacity):
#         super().__init__(make, model, year)
#         self.towing_capacity = towing_capacity

#     def calculate_towing_capacity(self):
#         return f"Towing capacity: {self.towing_capacity}."

# car = Car(make="Toyota", model="Bambino", year=2022, fuel_efficiency=130)
# car.display_info()
# print(f"Mileage: {car.calculate_mileage(distance=300)}")

# motorcycle = Motorcycle(make="Harley", model="Quinn", year=2018, fuel_efficiency=45)
# motorcycle.display_info()
# print(f"Mileage: {motorcycle.calculate_mileage(distance=150)}")

# truck = Truck(make="Ford", model="Tom", year=2021, towing_capacity=8000)
# truck.display_info()
# print(f"Towing capacity: {truck.calculate_towing_capacity()}")


# EX 4

# from datetime import datetime

# class Employee:
#     def __init__(self, name, employee_id, hire_date, salary):
#         self.name = name
#         self.employee_id = employee_id
#         self.hire_date = hire_date
#         self.salary = salary

#     def display_info(self):
#         print(f"Employee ID: {self.employee_id}\nName: {self.name}\nHire Date: {self.hire_date}\nSalary: ${self.salary}")

#     def calculate_years_in_company(self):
#         hire_date = datetime.strptime(self.hire_date, "%Y-%m-%d")
#         current_date = datetime.now()
#         years_in_company = int((current_date - hire_date).days / 365)
#         return years_in_company

#     def request_raise(self):
#         pass


# class Manager(Employee):
#     def __init__(self, name, employee_id, hire_date, level, salary):
#         super().__init__(name, employee_id, hire_date, salary)
#         self.level = level

#     def display_info(self):
#         super().display_info()
#         print(f"Level: {self.level}")

#     def request_raise(self):
#         years_in_company = super().calculate_years_in_company()
#         raise_amount = self.level * 50 + years_in_company * 100
#         print(f"{self.name} requested a monthly raise: ${raise_amount} -> yearly raise: ${raise_amount*12}")


# class Engineer(Employee):
#     def __init__(self, name, employee_id, hire_date, skill_level, salary):
#         super().__init__(name, employee_id, hire_date, salary)
#         self.skill_level = skill_level

#     def display_info(self):
#         super().display_info()
#         print(f"Skill Level: {self.skill_level}")

#     def request_raise(self):
#         years_in_company = super().calculate_years_in_company()
#         raise_amount = self.skill_level * 75 + years_in_company * 75
#         print(f"{self.name} requested a monthly raise: ${raise_amount} -> yearly raise: ${raise_amount*12}")


# class Salesperson(Employee):
#     def __init__(self, name, employee_id, hire_date, sales_volume, salary):
#         super().__init__(name, employee_id, hire_date, salary)
#         self.sales_volume = sales_volume

#     def display_info(self):
#         super().display_info()
#         print(f"Sales Volume: ${self.sales_volume}")

#     def request_raise(self):
#         years_in_company = super().calculate_years_in_company()
#         raise_amount = self.sales_volume * 0.005 + years_in_company * 50
#         print(f"{self.name} requested a monthly raise: ${raise_amount} -> yearly raise: ${raise_amount*12}")


# manager = Manager(name="Radu Tudoran", employee_id=101, hire_date="2020-01-15", level=3, salary=120000)
# engineer = Engineer(name="Cella Serghi", employee_id=102, hire_date="2018-05-20", skill_level=5, salary = 80000)
# salesperson = Salesperson(name="Mihail Drumes", employee_id=103, hire_date="2019-09-10", sales_volume=150000, salary=55000)

# manager.display_info()
# manager.request_raise()

# engineer.display_info()
# engineer.request_raise()

# salesperson.display_info()
# salesperson.request_raise()


# EX 5

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         pass

#     def move(self):
#         pass


# class Mammal(Animal):
#     def __init__(self, name, species, fur_color, sound):
#         super().__init__(name, species)
#         self.fur_color = fur_color
#         self.sound = sound

#     def make_sound(self):
#         print(f"Mammal {self.name} says: {self.sound}")

#     def give_birth(self):
#         print(f"Mammal {self.name} gives birth to a small {self.name}")


# class Bird(Animal):
#     def __init__(self, name, species, wingspan, sound, speed):
#         super().__init__(name, species)
#         self.wingspan = wingspan
#         self.sound = sound
#         self.speed = speed

#     def make_sound(self):
#         print(f"Bird {self.name} says: {self.sound}")

#     def fly(self):
#         print(f"Bird {self.name} flies with it's {self.wingspan} wingspan with a speed of {self.speed} km/h")


# class Fish(Animal):
#     def __init__(self, name, species, scale_color, sound):
#         super().__init__(name, species)
#         self.scale_color = scale_color
#         self.sound = sound

#     def make_sound(self):
#         print(f"Fish {self.name} says: {self.sound}")

#     def swim(self):
#         print(f"Fish {self.name} swims and the light reflects on it's {self.scale_color} colored scales")


# mammal = Mammal(name="Lioness", species="Feline", fur_color="Golden", sound="Roawr")
# mammal.make_sound()
# mammal.move()
# mammal.give_birth()

# bird = Bird(name="Eagle", species="Acvilian", wingspan=140, sound="Cah-Cah", speed=150)
# bird.make_sound()
# bird.move()
# bird.fly()

# fish = Fish(name="Goldfish", species="Amphibian", scale_color="Orange", sound="Blub-blub")
# fish.make_sound()
# fish.move()
# fish.swim()


# EX 6

# class LibraryItem:
#     def __init__(self, title, item_id, checked_out=False):
#         self.title = title
#         self.item_id = item_id
#         self.checked_out = checked_out
#         self.who_checked_out = None

#     def display_info(self):
#         print(f"Item ID: {self.item_id}\nTitle: {self.title}\nChecked Out: {'Yes' + ' by ' + self.who_checked_out if self.checked_out else 'No'}")

#     def check_out(self, who_checked_out):
#         if not self.checked_out:
#             self.checked_out = True
#             self.who_checked_out = who_checked_out
#             print(f"{self.title} has been checked out by {self.who_checked_out}")
#         else:
#             print(f"{self.title} is already checked out by {self.who_checked_out}")

#     def return_item(self):
#         if self.checked_out:
#             self.checked_out = False
#             print(f"{self.title} has been returned by {self.who_checked_out}")
#         else:
#             print(f"{self.title} is not currently checked out.")


# class Book(LibraryItem):
#     def __init__(self, title, item_id, author, checked_out=False):
#         super().__init__(title, item_id, checked_out)
#         self.author = author

#     def display_info(self):
#         super().display_info()
#         print(f"Author: {self.author}")


# class DVD(LibraryItem):
#     def __init__(self, title, item_id, director, checked_out=False):
#         super().__init__(title, item_id, checked_out)
#         self.director = director

#     def display_info(self):
#         super().display_info()
#         print(f"Director: {self.director}")


# class Magazine(LibraryItem):
#     def __init__(self, title, item_id, issue_number, checked_out=False):
#         super().__init__(title, item_id, checked_out)
#         self.issue_number = issue_number

#     def display_info(self):
#         super().display_info()
#         print(f"Issue Number: {self.issue_number}")


# # Example usage:
# book = Book(title="Cronicile ucigasului de regi", item_id="B001", author="Patrick Rothfuss")
# book.display_info()
# book.check_out("Stefan Casuneanu")
# book.return_item()
# book.return_item()

# dvd = DVD(title="The Prestige", item_id="D001", director="Christopher Nolan")
# dvd.display_info()
# dvd.check_out("Mihai George")
# dvd.check_out("George Eliot")

# magazine = Magazine(title="National Geographic", item_id="M001", issue_number="October 2023")
# magazine.display_info()
# magazine.check_out("Mihai George")
