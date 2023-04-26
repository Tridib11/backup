class Computer:
    def __init__(self):
        self.name = "Kevin"
        self.age = 18

    def update(self):
        self.age = 30

    def compare(self, c2):
        if self.age==c2.age:
            return True
        else:
            return False


c1 = Computer()
c1.age=30
c2=Computer()
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

# c1.name = "Rash"
print(c1.name)