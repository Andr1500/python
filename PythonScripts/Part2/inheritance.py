#example of inheritance

#creating the class Vehicle
class Vehicle:
    def vehicle_method(self):
        print("this is parent method from the class Vehicle")

#creating the child class Car
class Car(Vehicle):
    def car_method(self):
        print("this is from the child method")

#checking
car1 = Car()
car1.vehicle_method()


#1 parent class and many child classes
print("1 parent class and many child classes:")

#creatng class Vehicle
class Vehicle:
    def vehicle_method(self):
        print("this is the parent method form the class Vehicle")

#creating the class Car, child of the Vehicle
class Car(Vehicle):
    def car_method(self):
        print("child method from the class car")

#creating class Cycle, child of Vehicle class
class Cycle(Vehicle):
    def cycle_method(self):
        print("this is child from the class Vehicle")

#checking
car1 = Car()
car1.vehicle_method()  #calling the method from the parent class
car2 = Cycle()
car2.vehicle_method()  #calling the method from the parent class


#1 child class and 2 parent classes
print("1 child class and 2 parent classes")
class Camera:
    def camera_method(self):
        print("parent method from class Camera")

class Radio:
    def radio_method(self):
        print("parent method from class Radio")

class Cellphone(Camera, Radio):
    def cellphone_method(self):
        print("child method from the class Cellphone")

#checking
cellphone1 = Cellphone()
cellphone1.camera_method()
cellphone1.radio_method()



