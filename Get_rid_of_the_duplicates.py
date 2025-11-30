studentdata = {'id1': {'name': 'Renu', 'age': 12, 'class': 8},
               'id2': {'name': 'Surya', 'age': 17, 'class': 12},
               'id3': {'name': 'Renu', 'age': 12, 'class': 8},
               'id4': {'name': 'Sara', 'age': 7, 'class': 1},}
result= {}
for key, value in studentdata.items():
    if value not in result.values():
        result[key] = value
print(result)