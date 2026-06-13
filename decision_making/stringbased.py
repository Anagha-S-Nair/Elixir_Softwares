#1.Check if a string is empty
str=input("Enter a string:")
if str=='':
    print("String is empty")
else:
    print("String is not empty")

#2.check if a string starts with vowel
str=input("Enter a string: ")
if str[0].lower() in 'aeiou':
    print("starts with a vowel")
else:
    print("Does not start with a vowel")

#3. Check if two strings are equal
str1=input("Enter first string:")
str2=input("Enter second string:")
if str1==str2:
    print("Strings are equal")
else:
    print("Strings are not equal")

#4. Check if a word is in uppercase
str=input("Enter a word:")
if str.isupper():
    print("Uppercase")
else:
    print("Not uppercase")

#5. Check if a character is alphabet or not
char=input("Enter a character:")
if char.isalpha():
    print("Alphabet")
else:
    print("Not an alphabet")