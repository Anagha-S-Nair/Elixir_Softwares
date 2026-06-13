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