class Person:
    name="Rahul"
    occupation="Software Developer"
    networth=10
    """Self parameter is a reference to the current 
    instance of a class and it is used to accesss  
    variables that belongs to a class """
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=Person()
# a.name="Tridib" 
# print(a.name,a.networth)
a.info()