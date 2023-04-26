"""For example operator + is used to add two integers as well as
join two strings and merge two lists. It is achievable because ‘+’ operator
 is overloaded by int class and str class. You might have noticed that the same
 built-in operator or function shows
different behavior for objects of different classes, this is called Operator Overloading. """


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        # m1 = self.m1 + other.m1
        # m2 = self.m2 + other.m2
        # s3 = Student(m1, m2)
        # return s3
        return self.m1 + other.m1, self.m2 + other.m2
    def __gt__(self, other):
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)


s1 = Student(50, 60)
s2 = Student(60, 65)
s3 = s1 + s2
print(s3)
if s1 > s2:
    print("S1 wins")
else:
    print("S2 wins")

print(s1)

