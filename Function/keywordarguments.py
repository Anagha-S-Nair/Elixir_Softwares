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
