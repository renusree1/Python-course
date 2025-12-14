list1= {1,2,3}
list2= {'a','b','c'}
list3= list(zip(list1, list2))
print(list3, "\n")

l1= [10, 20, 30]
l2= [100, 200, 300]
for x,y in zip (l1, l2[::1]):
    print(x,y)

stocks= ["toystore", "google", "android"]
prices= [3422, 5223, 5423]
dict= {stocks: prices for stocks, prices in zip(stocks, prices)}
print("\n{}".format(dict))