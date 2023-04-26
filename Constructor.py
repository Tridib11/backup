class Person:
    # name ="Tridib"
    # occ="Developer"
    def __init__(self):
        print("Hey i am a person")
        # self.name = n
        # self.occ = o
    def info(self):
        print("lol")
# a = Person("Harry", "developer")
a=Person()
# b = Person("Divya", "HR")
a.info()
# print(a.name)
# a.name("Divya")
# a.occ("HR")
# a.info()

class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def info(self):
        print("Config is ",self.cpu,self.ram)
com1 = Computer("i5",16)
com2 = Computer("Ry-zen 3",8)
com1.info()
com2.info()

