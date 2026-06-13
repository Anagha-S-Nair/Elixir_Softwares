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