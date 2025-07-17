type= input("Do you prefer a bike or a car:")
if type== "bike":
    choice= input("Enter your type \n 1. Scooter \n 2. Electric scooter \n")
    if choice== "scooter":
        print("You choose a scooter")
    elif choice== "electric scooter":
        print("You choose a electric scooter")
    else:
        print("Your choice is invaild")
elif type== "car":
    choice1= input("Enter your type \n 1. XUV \n 2. Tesla \n")
    if choice1== "XUV" or choice1== "xuv":
        print("You choose a XUV")
    elif choice1== "tesla" or choice1== "Tesla":
        print("You choose a Tesle")
    else:
        print("Your choice is invaild")
else:
    print("Invalid input")
