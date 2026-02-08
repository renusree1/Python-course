class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def __str__(self):
        return self.question+' (ans= '+self.answer+')'

flash= []

print("Welcome to Flashcard App")

while True:
    question= input("Enter a question you want to add to the flashcards: ")
    answer= input("Enter the answer for the question:")
    flash.append(Flashcard(question, answer))
    option = input("Enter c, to continue adding the flashcards and enter q to quit: ")
    if option == "q" or option == "Q":
        break
print("\nYour Flashcards:")
for i in flash:
    print(i)