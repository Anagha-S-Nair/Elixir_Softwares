#Mixed Practice
#1. convert string to list using spilt() then count words
str1="Python programming language".split()
print("Length of words:", len(str1))

#2. Convert list to string using join() 
str1=['I', 'love', 'Python']
print("Joined string:", ' '.join(str1))

#3. Count vowels in list of strings
lst1=['banana','apple']
count=0
vowels='aeiou'
for word in lst1:
    for char in word:
        if char in vowels:
            count+=1
print("Total vowels:", count)

#4. Find common element in two lists
lst1=['python','programming']
lst2=['java','programming']
for i in lst1:
    if i in lst2:
        print(i)

#5. Remove empty string from list
lst1=['a','','b','','c']
for i in lst1:
    if i=='':
        lst1.remove(i)
print(lst1)
    
# Dictionary simple questions
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

#SET
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

#BOOLEAN
#Print result of 10 > 5
print(10>5)

#Print result of 10 == 5
print(10==5)

#Print result of True and false
print(True and False)

#Print result of True or False
print(True or False)

#Print result of not True 
print(not True)

#Compare two numbers using >=
print(10>=5)

#Check equality of two strings
print("abc" == "bcd")

#Print type of a boolean value
print(type(True))

#Assign boolean value to a variable and print it
var = True
print(var)

#Compare two value using !=
print(10!=5)

#BONUS MIXED
#Create a dictionary and check its length
d1={"Name" : "Varun","Age": 20, "College":"MA College"}
print(len(d1))

#Create two sets and perform union
s1={10,5,4,1}
s2={7,9,6,2}
print(s1.union(s2))

#Store boolean vales inside a dictionary
d={0:False,1:True}
print(d)

#Create a set and print it
s={"Python","Programming"}
print(s)

#Compare two dictionary values
d2={"Name":"Amina","Age":22}
print(d1==d2)

#Basic Decision Making Questions
#1. Check if a number is positive or negative
num=int(input("Enter a number: "))
if num>0:
    print("Positive")
else:
    print("Negative")

#2. Check if a number is even or odd
num=int(input("Enter a number: "))
if num%2==0:
    print("Even")
else:
    print("odd")

#3.Check if a person is eligible to vote (age >=18)
age=int(input("Enter your age: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#4.Check if a number is greater than 100
num=int(input("Enter a number: "))
if num>100:
    print("Greater than 100")
else:
    print("Not greater than 100")

#5. Check if two numbers are equal
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if num1==num2:
    print("Numbers are equal")
else:
    print("Numbers are not equal")

#INTERMEDIATE QUESTIONS
#1.Find the greatest of two numbers
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1>num2:
    print("Greatest number is: ",num1)
else:
    print("Greatest number is: ",num2)

#2. Find the largest of three numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b and a>c:
    print("Largest:",a)
elif(b>a and b>c):
    print("Largest:",b)
else:
    print("Largest:",c)

#3. Check if a number is divisible by 5
num=int(input("Enter a number: "))
if num%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

#4. Check if a number is divisible by both 3 and 5
num=int(input("Enter a number: "))
if num%3==0 and num%5==0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")

#5. Check if a year is a leap year
year=int(input("Enter a year: "))
if (year%4==0 or year%400==0) and year%100!=0:
    print("Leap year")
else:
    print("Not a leap year")

#String-Based conditions
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


#REAL-LIFE BASED QUESTIONS
#1. Check login(username and password)
username=input("Enter username: ")
password=input("Enter password: ")
user="anagha"
pwd="pwd123"
if username==user and password==pwd:
    print("Login successful")
else:
    print("Login failed")

#2. Check pass/fail(marks >= 50)
marks=int(input("Enter marks:"))
if marks>=50:
    print("Pass")
else:
    print("Fail")

#3.Grade System(A,B,C,Fail)
marks=int(input("Enter marks:"))
if marks>=90:
    print("Grade: A")
elif marks>=80:
    print("Grade:B")
elif marks>=70:
    print("Grade: C")
else:
    print("Grade: Fail")

#Check if a number is within a range(1-100)
num=int(input("Enter a number: "))
if num>=1 and num<=100:
    print("Within range")
else:
    print("Not within range")

#Simple calculator (based on operation +,-,*,/)
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operation=input("Enter operation(+,-,*,/): ")
if operation=='+':
    print("Result: ", num1+num2)
elif operation=='-':
    print("Result: ",num1-num2)
elif operation=='*':
    print("Result: ",num1*num2)
elif operation=='/':
    if num2!=0:
        print("Result: ",num1/num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")

#NESTED IF QUESTIONS
#1.Find largest of three numbers using nested if
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b:
    if a>c:
        print("Largest:",a)
    else:
        print("Largest:",c)
else:
    if b>c:
        print("Largest:",b)
    else:
        print("Largest:",c)

# Check if a triangle is Equilateral, Isosceles or Scalene using nested if
side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))
if side1 == side2:
    if side2 == side3:
        print("Equilateral triangle")
    else:
        print("Isosceles triangle")
else:
    if side1 == side3 or side2 == side3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

# Check if a number is positive, negative or zero using nested if
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

#4. ATM withdrawal condition(Balance check)
balance=1000
withdraw=int(input("Enter amount to withdraw: "))
if withdraw>0:
    if withdraw<=balance:
        balance-=withdraw 
        print("Withdrawal successful. Remaining balance: ", balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid withdrawal amount")

#Check discount eligibility based on amount
amount=int(input("Enter amount:"))
if amount>500:
    if amount>=2000:
        print("25% discount")
    else:
        print("10% discount")
else:
    print("No discount")

#CHALLENGING QUESTIONS
#1. Check if a number(number/string)
value=input("Enter a value: ")
if value==value[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#2.Check Armstrong number
num = int(input("Enter a number: "))
temp = num
sum = 0
digits = len(str(num))
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10
if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

#3. Check if Character is Vowel or Consonant
ch = input("Enter a character: ")
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")

#4. Menu-Based Program Using if-elif
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    print("Result =", a / b)
else:
    print("Invalid Choice")

#5. Check if a Number Lies Between Two Numbers
num = int(input("Enter number: "))
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
if start < num < end:
    print("Number lies between")
else:
    print("Number does not lie between")
