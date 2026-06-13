#Use append() to Add "orange" to list
lst=['apple','grape']
print("Original list: ", lst)
lst.append('orange')
print("After appending: ", lst)

#Use insert() to Insert "grapes" at index 1
str1=['apple','orange']
print("Original list: ", str1)
str1.insert(1,'grape')
print("After inserting: ", str1)

#Use remove() to Remove "banana"
str1=['apple','orange','banana']
print("Original list: ", str1)
str1.remove('banana')
print("After removing: ", str1)

#Use pop() to Remove last element
str1=['apple','orange','banana']
print("Original list: ", str1)
str1.pop()
print("After popping: ", str1)

#Use len() to Find length of list
str1=['apple','orange','banana']
print("Length:",len(str1))

#Use count() to Count occurrences of 2 in [1,2,2,3]
lst=[1,2,2,3]
print("Count",lst.count(2))

#Use sort() Sort [5,2,9,1]
lst=[5,2,9,1]
print("Original list: ", lst)
print("Sorted list:",sorted(lst))

#Use reverse() Reverse list
lst=[5,2,9,1]
print("Original list: ", lst)
print("Reverse list:",lst[::-1])

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
    
