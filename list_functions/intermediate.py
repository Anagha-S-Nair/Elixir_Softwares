#Append multiple elements using loop
lst=[5,2,9,1]
for i in range(5):
    n=int(input("Enter a number: "))
    lst.append(n)
print("List after appending: ", lst)

#Sort list in descending order
lst=[5,4,9,1]
print(lst)
lst.sort()
print(lst[::-1])

#Remove duplicates from list
lst=[5,4,9,1,5]
s=set(lst)
print(list(s))

#Find second largest number
lst=[5,4,9,1,10]
lst.sort()
print(lst[-2])

#Copy a list using copy()
lst1=[5,9,6]
lst2=lst1.copy()
print(lst2)

#Merge two lists using +
lst1=[5,9,3]
lst2=[7,2,4]
print(lst1 + lst2)

#check if element exits in list
lst=[5,9,3]
if 9 in lst:
    print("Element exists")
else:
    print("Element does not exist")
    
