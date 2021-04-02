#define class

class Hero(): #parent class, like superclass
    """class for heroes"""
    def __init__(self, name, level, race):  #method of the class , init is necessary
        """initiate the hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """all parameters of the hero"""
        description = (self.name + ' level: ' + str(self.level) +
                       ' race: ' + self.race + ' Health: ' + str(self.health)).title()
        print(description)

    def level_up(self):
        """upgrade hero's level"""
        self.level += 1  #like self.level = self.level + 1

    def move(self):
        """start moving"""
        print("hero " + self.name + " is moving now")

    def set_health(self, new_health):
        """set new parameter of health"""
        self.health = new_health

#-----------------child class-------------
#define incapsulated class
class SuperHero(Hero):
    """class for creating superhero""" #chaild class of Hero class

    def __init__(self, name, level, race, magiclevel):
        """initiate the super hero"""
        super().__init__(name, level, race)  #super is the function for initialise parent class
        self.magiclevel = magiclevel
        self.__magic = 100  #__magic forbidden change this value outside of the class

    def domagic(self):
        """use magic"""
        self.__magic -= 10

    def show_hero(self):
        """all parameters of the hero"""
        description = (self.name + ' level: ' + str(self.level) +
                           ' race: ' + self.race + ' Health: ' + str(self.health) + "Magic is " + str(self.__magic)).title()
        print(description)


