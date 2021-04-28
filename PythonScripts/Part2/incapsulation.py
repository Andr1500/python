#task: model of car between 2000 and 2018. if user put less than 2000,
#parameter will be 2000, if more than 2018, will be 2018, if
# if between - inputed parameter.

#create the class Car
class Car:

    def __init__(self, model):
    #initialise of properties
        self.model = model

    #create the properties of the model
    @property
    def model(self):
        return self.__model

    #the setter for creating properties
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def getCarModel(self):
        return "year of production is : " + str(self.model)

#checking
car1 = Car(1345)
print(car1.getCarModel())