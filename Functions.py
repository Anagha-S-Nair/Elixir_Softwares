# REQUIRED ARGUMENTS
#1. Write a function multiply(a,b) to print the multiplication of two numbers.
'''def multiply(a,b):
    print("Multiplication: ",a*b)

multiply(4,5)

#2. Create a function student(name,mark) and display student details.
def student(name,mark):
    print("Name: ",name)
    print("Mark: ",mark)

student("Anagha",22) 

#3. Write a function to find the area of a rectangle using length and breadth.
def rectangle_area(length,breadth):
    area=length*breadth
    print("Area of rectangle: ",area)

rectangle_area(5,3) 

#4. Create a function evenodd(num) to check whether a number is even or odd.
def evenodd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

evenodd(4) 

#5. Write a function greet(name) that prints: "Welcome <name>"
def greet(name):
    print("Welcome:",name)

greet("Anagha") 

#KEYWORD ARGUMENTS
#1. Create a function employee(name,salary) and call it using keyword arguments.
def employee(name,salary):
    print("Name: ",name)
    print("Salary: ",salary)

employee(name="Anagha",salary=20000) 

#2. Write a function movie(title,year) and pass arguments in different order.
def movie(title,year):
    print("Title: ",title)
    print("Year: ",year)
movie(year=2020,title="Leo") 

#3.Create a function product(name,price) using keyword arguments.
def product(name,price):
    print("Name: ",name)
    print("Price: ",price)
product(name="Laptop",price=50000) 

#4. Create a function person(name,city) and display details.
def person(name,city):
    print("Name: ",name)
    print("City: ",city)
person(name="Anagha",city="Kochi")

#5.Create a function book(title,author) and call it using keyword arguments.
def book(title,author):
    print("Title: ",title)
    print("Author: ",author)
book(title="The Alchemist",author="Paulo Coelho") 

#DEFAULT ARGUMENTS
#1. Write a function country(name="India")
def country(name="India"):
    print("Country: ",name)

country()
country("USA") 

#2. Create a function power(a,b=2) to find square by default.
def power(a,b=2):
    print("Result: ",a**b)
power(4)
power(4,3)

#3. Create a function welcome(name="Guest").
def welcome(name="Guest"):
    print("Welcome: ",name)
welcome()

#4. Create a function salary(amount=10000)
def salary(amount=10000):
    print("Salary: ",amount)
salary() 

#5. Write a function student(course="MCA")
def student(course="MCA"):
    print("Course: ",course)
student() 

#VARIABLE LENGTH ARGUMENTS(*args)
#1.create a function to find sum of any number of values.
def total(*args):
    print("Sum: ",sum(args))
total(1,2,3,4,5) 

#2. Create a function to print all given names.
def print_names(*args):
    print("Names: ",args)
print_names("Anagha","Akhil","Anu") 

#3.Write a function to find largest number using args
def largest(*args):
    print("Largest: ",max(args))
largest(3,5,2,8,1) 

#4. Create a function to calculate average of numbers.
def average(*args):
    avg=sum(args)/len(args)
    print("Average: ",avg)
average(1,2,3,4,5) 

#5. Write a function to count total arguments passed.
def count_args(*args):
    print("Total arguments: ",len(args))
count_args(1,2,3,4,5)

#VARIABLE LENGTH KEYWORD ARGUMENTS(**kwargs)
#1. Write a function to display student details using 
def student_details(**kwargs):
    print("Student Details: ",kwargs)
student_details(name="Anagha",age=22,course="MCA")

#2.Create a function to print employee information.
def employee_info(**kwargs):
    print("Employee Information: ",kwargs)
employee_info(name="Anagha",salary=20000)

#3. Write a function to display product information.
def product_info(**kwargs):
    print("Product Information: ",kwargs)
product_info(name="Laptop",price=50000)

#4.Create a function to store customer information dynamically.
def customer_info(**kwargs):
    print("Customer Information: ",kwargs)
customer_info(name="Anagha",city="Kochi",age=22)

#5. Write a function that accepts any number of keyword arguments and prints them
def print_kwargs(**kwargs):
    print("Keyword Arguments: ",kwargs)
print_kwargs(name="Anagha",age=22,course="MCA")

#MINI PRACTICAL PROGRAMS
#1. Create a calculator using functions.
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b  
print("Addition: ",add(4,5))
print("Subtraction: ",subtract(4,5))
print("Multiplication: ",multiply(4,5))
print("Division: ",divide(4,5))

#2.Write a menu-driven program using functions.
def menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice=int(input("Enter your choice: "))
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    if choice==1:
        print("Result: ",add(a,b))
    elif choice==2:
        print("Result: ",subtract(a,b))
    elif choice==3:
        print("Result: ",multiply(a,b))
    elif choice==4:
        print("Result: ",divide(a,b))
    else:
        print("Invalid choice")
menu()

#3. Create a student marklist using functions and arguments.
def marklist(name,marks):
    print("Name: ",name)
    print("Marks: ",marks)
marklist("Anagha",85) 

#4. Build a simple billing system using function arguments.
def billing_system(**kwargs):
    print("Billing Information: ",kwargs)
billing_system(customer="Anagha",items=["Laptop","Mouse"],total=55000)

#5.Create a login function using username and password arguments.
def login(username,password):
    if username=="admin" and password=="password":
        print("Login successful")
    else:
        print("Invalid credentials")
login("admin","password") '''
