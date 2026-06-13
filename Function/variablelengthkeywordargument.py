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