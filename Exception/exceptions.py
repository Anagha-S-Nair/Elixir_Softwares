#1. Check whether a number is even or odd using exception handling
'''try:
    num=int(input("Enter a number:"))
    if num%2==0:
        print("Even Number")
    else:
        print("Odd Number")
except ValueError:
    print("Please enter a valid integer") 

#2. Calculate the average of 3 numbers and handle invalid input
try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    num3=int(input("Enter a number:"))
    avg=(num1+num2+num3)/3
    print("Average=",avg)
except ValueError:
    print("Invalid") 

#3. Simple calculator using try and except
try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    op=input("Enter operator(+,-,*,/):")
    if op=="+":
        print("Result=",num1+num2)
    elif op=="-":
        print("Result=",num1-num2)
    elif op=="*":
        print("Result=",num1*num2)
    elif op=="/":
        print("Result=",num1/num2)
    else:
        print("Invalid operator")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid") 

#4. Take student marks and display grade while handling errors
try:
    marks=int(input("Enter marks:"))
    if marks<0 or marks>100:
        raise ValueError
    if marks>=90:
        print("Grade A")
    elif marks>=75:
        print("Grade B")
    elif marks>=50:
        print("Grade C")
    else:
        print("Grade D")
except ValueError:
    print("Invalid") 

#5.Password validation using custom exceptions
class InvalidPasswordError(Exception):
    pass
password=input("Enter a password:")
pwd="anagha"
try:
    if password==pwd:
        print("Valid password")
    else:
        raise InvalidPasswordError("Invalid password")
except InvalidPasswordError as e:
    print(e) 

#6. Read numbers from a file and handle possible exceptions

try:
    file=open("numbers.txt","r")
    for line in file:
        num=int(line.strip())
        print(num)
    file.close()
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("File contains non-numeric data.") 

#7. Handle errors while converting string to float
try:
    num=float(input("Enter a number:"))
    print("Float value =", num)
except ValueError:
    print("Invalid error") 

#8. Remove an item from a list and handle exceptions
try:
    lst=[1,2,3,4,5]
    item=int(input("Enter an item to remove:"))
    lst.remove(item)
    print("Updated list:", lst)
except ValueError:
    print("Item not found in the list.") 

#9. Handle multiple exceptions in a banking application
try:
    balance=1000
    amount=float(input("Enter amount to withdraw:"))
    deposit=float(input("Enter amount to deposit:"))
    if amount>balance:
        raise ValueError("Insufficient balance.")
    balance=balance-amount
    balance=balance+deposit
    print("Updated balance:", balance)
except ValueError as e:
    print(e)
except Exception as e:
    print("An error occurred:", e) '''

#10. Create a login system with exception handling for invalid credentials
class InvalidCredentialsError(Exception):
    pass
try:
    valid_username="admin"
    valid_password="1234"
    username=input("Enter username:")
    password=input("Enter password:")
    if username==valid_username and password==valid_password:
        print("Login successful.")
    else:
        raise InvalidCredentialsError("Invalid credentials.")
except InvalidCredentialsError as e:
    print(e)

