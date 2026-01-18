class Myclass:
    __private_var = 10
    def __privmeth(self):
        print("I am inside class myclass")
    def hello(self):
        print("Private variable value is:", Myclass.__private_var)
obj = Myclass()
obj.hello()
obj.__privmeth()  