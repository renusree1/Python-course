my_dict= {'condingal': 2, 'best': 2, 'for': 2, 'conding': 1}
print("The orginal dictonary is:" + str(my_dict))

Key = 2
count = 0
for key in my_dict:
    if my_dict[key]== Key:
        count = count + 1

print("The frequency of the key (2) is:", str(count))