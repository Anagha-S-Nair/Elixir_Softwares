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
