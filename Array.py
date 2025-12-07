import array as arr

a= arr.array("i",[1,2,3,4,5])
print("Original array:")
print(a)

print(a.count(3))

a.reverse()
print(a)