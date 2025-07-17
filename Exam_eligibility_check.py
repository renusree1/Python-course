medical= input("Enter if you have a medical cause. (Y for yes and N for no):")
attendence=int(input("Enter the percentage of your attendence:"))
if attendence>= 75:
    print("You are allowed for the examination")
else:
    if medical== "Y":
        print("You are allowed for the examination")
    else:
        print("You are not allowed for the examination")
        