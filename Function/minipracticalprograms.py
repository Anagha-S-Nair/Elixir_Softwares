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
login("admin","password") 
