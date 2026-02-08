import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {"Apple": "red", "banana": "yellow", "grapes": "green", "orange": "orange", "blueberry": "blue", "strawberry": "red", "dragonfruit":"white"}
    def quiz(self):
            while True:
                fruit, color = random.choice(list(self.fruits.items()))
                print("What colour is the", fruit, "?")
                user_ans= input()
                if user_ans.lower() == color:
                    print("Correct answer!!")
                else:
                    print("Wrong answer!!")
                option = input("Enter c, to continue the quiz and enter q to quit: ")
                if option:
                    break
print("Welcome to the Fruit Quiz!!")
fq = FruitQuiz()
fq.quiz()