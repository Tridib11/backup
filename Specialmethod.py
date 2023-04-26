"""Constructors are callled as special method"""


class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def info(self):
        print("Config is ", self.cpu, self.ram)


com1 = Computer("i5", 16)
com2 = Computer("Ry-zen 3", 8)
com1.info()
com2.info()




