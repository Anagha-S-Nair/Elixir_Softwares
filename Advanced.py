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

#Extract only alphabets from "abc123@#"
str1="abc123@#"
print("Original string: ", str1)
result=""
for char in str1:
    if char.isalpha():
        result+=char
print("After removal: ",result)