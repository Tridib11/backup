class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 is working")


"""Single level inheritance"""


class B(A):  ##creating the interitance making the B as a child class
    def feature3(self):
        print("Feature 1 working")

    def feature4(self):
        print("Feature 2 is working")


"""Multileve inheritance"""


class C(B):  # for multiple inhertance use c(A,B)
    def feature5(self):
        print("Feature 5 is working")


a1 = A()
a1.feature1()
a1.feature2()
b1 = B()
b1.feature1()
c1 = C()
c1.feature5()
