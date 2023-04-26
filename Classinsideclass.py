class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.Lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.Lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8gb'

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Navin', 2)
s2 = Student('Jenny', 3)
# print(s1.name,s1.rollno)
s1.show()
# lap1 = Student.Laptop()

# """Explanation"""
"""The Student class has a constructor method (__init__) that takes two parameters, name and rollno, and initializes two 
instance variables, name and rollno, with these parameters.It also initializes a third instance variable, Lap, with a 
new instance of the Laptop class.The Laptop class has its own constructor method that initializes three instance 
variables, brand, cpu, and ram, with the values 'HP', 'i5', and '8gb', respectively. It also has a show method that 
prints the values of these instance variables.The Student class also has a show method that prints the values of the
name and rollno instance variables of the student object, and calls the show method of the associated 
laptop object (self.Lap). When s1.show() is called, it will print Navin 2 followed by HP i5 8gb, 
because s1 has a laptop with the default values of brand, cpu, and ram.The last
 commented line (# lap1 = Student.Laptop()) creates a new instance of the Laptop class using the 
 Student class itself, which is not correct because the Laptop class is defined inside the Student 
 class and can only be accessed using an instance of the Student class."""
