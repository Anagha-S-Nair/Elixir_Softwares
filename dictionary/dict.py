#1. Create a dictionary with 3 items and print it
dict1={'Name':'Anagha' , 'Age': 21, 'College':'MA college'}
print(dict1)

#2. Access a value using key
print(dict1.get("Name"))

#3. Add a new key-value pair
dict1['course']= 'MCA'
print(dict1)

#4. update a value in dictionary
dict1["Age"]= 22
print(dict1)

#5.Remove a key using pop()
dict1.pop("College")
print(dict1)

#6. Print all keys using .keys()
print(dict1.keys())

#7.Print all keys using .values()
print(dict1.values())

#8.Get value using .get()
print(dict1.get("Name"))

#9.copy a dictionary
dict2=dict1.copy()
print(dict2)

#10. Clear all items
dict1.clear()
print(dict1)