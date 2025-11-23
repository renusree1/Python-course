tuple = ("tuple", False, 3.2, 1)
print("The 1st tuple is:", tuple)
tuple1 = (10, 20, 30, 40, 50)
print("The 2nd tuple is:", tuple1)
tuple2 = tuple1 + (9,)
print("The 3rd after adding 9 tuple is:", tuple2)
tuple3 = ( 50, 40, 30, 20, 10, 40)
print(tuple3.count(40))
tuple4 = ("P","Y","T","H","O","N")
slice = tuple4[3:5]
print("The sliced tuple is:", slice)
slice1 = tuple4[:6]
print("The sliced tuple is:", slice1)