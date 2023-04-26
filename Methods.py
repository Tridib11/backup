"""Methods are used when u want to perform a certain task"""


class Student:
    school = "Tridib"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        """Average of all the numbers"""
        return (self.m1 + self.m2 + self.m3) / 3

    # There are two types of methods 1 accessors and 2 mutators

    """Getters setters"""

    """Accessors when u want to access something(fetching the values)"""

    def get_m1(self):
        return self.m1

    """Mutators when u want to change something(modify)"""

    def set_m1(self, value):
        self.m1 = value



    @classmethod  #to use class method we have to use decorator called class method
    def getSchool(cls):
        return cls.school

    """"Static method if u dont have to do anything with the class or the instance variable then """
    @staticmethod #to use static method we have to use decorator called class staticmethod
    def info():
        print("This is a student class ")



s1 = Student(34, 67, 32)
s2 = Student(22, 44, 55)
print(s1.avg())
print(s1.getSchool())
Student.info()
