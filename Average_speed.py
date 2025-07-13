speed1=int(input("Enter the speed: "))
speed2=int(input("Enter the speed: "))
speed3=int(input("Enter the speed: "))
sum= speed1+speed2+speed3
average= sum/3
print("The average is:", average)
if average > speed1 and average > speed2 and average > speed3:
    print("%d is higher than %d,%d,%d"%(average,speed1,speed2,speed3))
elif average > speed1 and average > speed2:
    print("%d is higher than %d,%d"%(average,speed1,speed2))
elif average > speed2 and average > speed3:
    print("%d is higher than %d,%d"%(average,speed2,speed3))
elif average > speed1 and average > speed3:
    print("%d is higher than %d,%d"%(average,speed1,speed3))
elif average > speed1:
    print("%d is higher than %d"%(average,speed1))
elif average > speed2:
    print("%d is higher than %d"%(average,speed2))
elif average > speed3:
    print("%d is higher than %d"%(average,speed3))
else:
    print("None")