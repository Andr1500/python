#method is about few forms.

#1. Polymorphism with Class Methods
class Car:
    def start(self, a, b=None):
        if b is not None:
            print(a + b)
        else:
            print(a)

#checking
car1 = Car()
car1.start(2, 5)

#2. Polymorphism with Function and Objects
#creating the class Vehicle
class Vehicle:
    def print_details(self):
        print("parent class from class Vehicle")

#creating the class which inherit Vehicle
class Car(Vehicle):
    def print_details(self):
        print("child method from class Car")

#creating class Cycle which inherit Vehicle
class Cycle(Vehicle):
    def print_details(self):
        print("child method from class Cycle")

#check
car1 = Vehicle()
car1.print_details()
car2 = Car()
car2.print_details()
car3 = Cycle()
car3.print_details()