class Bird:
    def __init__(self):
      print("Bird is ready")
    def who(self):
        print("Bird")
    def swim(self):
        print("Can swim fast")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def who(self):
        print("Penguin")
    def run(self):
        print("Penguin can't run fast")
peggy = Penguin()
peggy.swim()
peggy.who()
peggy.run()