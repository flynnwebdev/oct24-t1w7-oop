# Class - blueprint for creating objects - custom data type

# Camel case - eg. helloThere

class Car: # Pascal case - eg. HelloThere
    # Constructor - optional special method that sets up attributes of a new instance
    # will be called automatically when a new instance is created
    def __init__(self, make, model, engine): # self is passed implicitly by the interpreter
        # create an attribute 'make' and copy the value of the 'make' param into it
        # dunder makes the attr private
        self.__make = make # dot notation - <object>.<attr/method>
        self.model = model
        self.engine = engine
        # implicitly returns self

    def start(self):
        print(f'{self.__make} {self.model} started!')

    # Function overloading - not supported in Python
    # def start(self, foo):
    #     pass

    def __str__(self): # Returns a string representation of the object
        return f'This is a {self.__make} {self.model}'
    
    # Getter
    def get_make(self):
        # Authorize
        # if condition
        return self.__make
        # side-effects
    
    # Setter
    def set_make(self, new_make):
        # Validate new_make
        # Authorize
        self.__make = new_make


# Inheritance - "is a" relationship
class PetrolCar(Car):
    def __init__(self, make, model, engine, tank_capacity_l):
        super().__init__(make, model, engine)
        self.tank_capacity_l = tank_capacity_l

    def __str__(self):
        return f'{super().__str__()}. It has a {self.tank_capacity_l}l tank.'


# Composition - "has a" relationship
class Engine:
    def __init__(self, type, max_power_kw):
        self.type = type
        self.max_power_kw = max_power_kw
    
    def __str__(self):
        return f'This is a {self.type} engine with a maximum power of {self.max_power_kw}kW'


# Main
engine1 = Engine(type='petrol', max_power_kw=235)
my_car = PetrolCar(make='Honda', model='Civic', tank_capacity_l=47, engine=engine1) # create a new instance of Car
# my_car is now an object of class 'Car'
# your_car = Car('Toyota', 'Landcruiser')
# print(my_car.__dict__)
# your_car.model = 'Prius'
print(my_car.engine)
# print(your_car)
# my_car.start()
# your_car.start()
# print(my_car.get_make())
