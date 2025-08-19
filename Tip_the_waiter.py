def total (bill,tip):
    calcu= bill+(bill*0.01*tip)
    print("Total: $", calcu)

realbill= int(input("Enter the amount of your bill: "))
realtip= int(input("Enter the tip percentage: "))

total(realbill,realtip)