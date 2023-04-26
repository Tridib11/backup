"""Using Duck Typing, we do not check types at all. Instead, we check for
the presence of a given method or attribute."""

class Pycharm:
    def execute(self):
        print("compiling")
        print("Running")


class Myeditor:
    def execute(self):
        print("Compiling")
        print("Self check")
        print("Convection check")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


ide1 = Myeditor()
# ide = Pycharm()
lap1 = Laptop()
lap1.code(ide1)
# for obj in Pycharm(),Myeditor():
#     obj.execute()
