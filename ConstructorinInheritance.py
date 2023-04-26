class A:
    def __init__(self):
        print("In a init")

    def feature1(self):
        print("Feature 1A working")

    def feature2(self):
        print("Feature 2 is working")


class B:
    def __init__(self):
        ##super().__init__() ##used if u want to acces the init of the superclass also
        print("In b init")

    def feature3(self):
        print("Feature 1B working")

    def feature4(self):
        print("Feature 2 is working")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("In c init")

    def feature3(self):
        print("Feature 1 working")

    def feature4(self):
        print("Feature 2 is working")

    def feat(self):
        super().feature2()


a1 = C()
a1.feature1()  ###MRO(Method resolution order) goes from left to right
a1.feat()
