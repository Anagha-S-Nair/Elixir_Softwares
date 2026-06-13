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