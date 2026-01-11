class Parent:
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num
    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.id_num)
class Employee(Parent):
    def __init__(self, name, id_num, salary, post):
        self.salary = salary
        self.post = post
        Parent.__init__(self, name, id_num)
Renu= Employee("Renu", 14829424, 5000000, "Manager")
Renu.display()