a= str(input("Enter a word: "))

for i in a:
    if i == "a" or i == "A":
        print("A is found")
        break 
    else:
        print("A is not found. Try again!")