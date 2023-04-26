class Car:


    """Any variable outuside the init thing is a class/static variable """
    wheels = 5

    def __init__(self):

        """Anything inside the init thing is an instance variable"""

        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()
c1.mil = 8

"""TO change the class variable we use"""

Car.wheels=8

print(c1.com, c1.mil, c1.wheels)

print(c2.com, c2.mil, c2.wheels)
