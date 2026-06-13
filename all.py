#Use len() to find length of "python programming"
s1="python programming"
print("Length of string: ",len(s1))

#Use lower() to Convert "PYTHON"→ lowercase
s1="PYTHON"
print(s1.lower())
print(s1.upper())

#Use upper() to Convert "hello"→ uppercase
s1=" hello "
print(s1.strip())

#Use strip() to Remove spaces from " hello "
s1="hello world"
print(s1.replace("world", "Python"))

#Use replace() to Replace "world" with "Python" in "hello world"
str1="I love python"
print(str1.split())

#Use count()to  Count 'a' in "banana"
str1="banana"
print(str1.count('a'))

#Use find() to Find position of "pro" in "python programming"
s1="python programming"
print(s1.find('pro'))

#INTERMEDIATE
#Convert string to lowercase and count vowels
str1="python programming"
print(str1.lower())
vowels='aeiou'
count=0
for char in str1:
    if char in vowels:
        count+=1
print("Number of vowels: ",count)

#Remove spaces and find length
str1=" Hello world "
print(len(str1))
print("After: ", len(str1.replace(" ","")))

#Replace spaces with _and convert to uppercase
str1=" Hello world"
print(str1.replace(" ","-").upper())

#Split sentence and print each word
str1="python programming".split()
print(str1)
for word in str1:
    print(word)

#Count number of words using split()
str1="hello world".split()
print("Number of words: ",len(str1))

#Find longest word using split()
str1="hello programming".split()
print("Maximum word: ", max(str1))

#Check if substring exists using find()
str1="welcome to python programming"
if str1.find('python') != -1:
    print("Substring found ")
else:
    print("Substring not found")

#ADVANCED
#Remove duplicate characters using functions
def remove_duplicates(s):
    result=""
    for char in s:
        if char  not in result:
            result+=char
    return result


str1="programming"
print("original string: ",str1)
print("string after removing duplicates: ",remove_duplicates(str1))

#Reverse string using slicing
def reverse_string(s):
    return s[::-1]

str1="welcome"
print("Original string: ", str1)
print("Reversed string: " , reverse_string(str1))

#Check palindrome using functions
def is_palindrome(s):
    if s == s[::-1]:
        print("Palindrome.")
    else:
        print("Not palindrome.")
str1="malayalam"
is_palindrome(str1)

#Convert "hello world"→ "hElLo WoRlD" (alternate case)


#Extract only alphabets from "abc123@#"
str1="abc123@#"
print("Original string: ", str1)
result=""
for char in str1:
    if char.isalpha():
        result+=char
print("After removal: ",result)

# LIST FUNCTIONS
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

#Check if element exists in list
lst=[4,6,5]