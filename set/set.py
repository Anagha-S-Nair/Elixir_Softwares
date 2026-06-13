#Create a set with 5 numbers
s={2,8,6,3}
print(s)

#Add an item to a set
s.add(10)
print(s)

#Remove an element using remove()
s.remove(6)
print(s)

#Remove an element using discard()
s.discard(2)
print(s)

#Find union of two sets
s1={5,7,1}
print(s.union(s1))

#Find Intersection of two sets
s2={3,8,7}
print(s.intersection(s2))

#Find difference of two sets
s3={10,8,1}
print(s.difference(s3))

#Check length of a set
print(len(s))
print(s)

#Convert list to set
lst = [7,20,96]
print(set(lst))

#Clear a set
s.clear()
print(s)