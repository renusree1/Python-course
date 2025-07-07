english= int(input("Enter your marks for english: "))
math= int(input("Enter your marks for maths: "))
science= int(input("Enter your marks for science: "))
french= int(input("Enter your marks for french: "))
arabic= int(input("Enter your marks for arabic: "))
average= (english+math+science+french+arabic)/5
print("Your average is:", average)
if average >=91 and average <=100:
    print("A1")
elif average >=81 and average <=90:
    print("A2")
elif average >=71 and average <=80:
    print("B1")
elif average >=61 and average <=70:
    print("B2")
elif average >=51 and average <=60:
    print("C1")
elif average >=41 and average <=50:
    print("C2")
elif average >=31 and average <=40:
    print("D")
elif average >=21 and average <=30:
    print("E")
elif average >=11 and average <=20:
    print("F")
else:
    print("Invalid level")