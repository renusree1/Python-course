list=[1,4,7,3,9,4,2,80]
print("The original list is:",list)

count=0

for i in list:
    count+=i

avg=count/len(list)
print("The sum of the list is:",count)
print("The average of the list is:",avg)

list.sort()
print("The smallest number in the list is:",list[0])
print("The largest number in the list is:",list[-1])
