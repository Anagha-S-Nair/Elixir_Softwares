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