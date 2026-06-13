# Write a Python program to create a class student and display student details using an object.(Class and Object)
'''class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll no:",self.rollno)
        print("Marks:",self.marks)

s1=Student("Anagha",14,85)
s1.display() 

#2. Write a Python program using a constructor (__init__)to initialize and display employee details.Constructor)
class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("ID:",self.id)
        print("Department:",self.department)

e1=Employee("Varun",101,"IT")
e1.display() 

#3. Write a Python program to demonstrate Single Inheritance using classes Animal and Dog (Single Inheritance)
class Animal:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Animal Name:",self.name)
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def display(self):
        super().display()
        print("Breed:",self.breed)
d1=Dog("Bruno","German Shepherd")
d1.display() 

#4. Write a Python program to demonstrate Multiple Inheritance using classes Father , Mother , and Child (Multiple Inheritance)
class Father:
    def drive(self):
        print("Father can drive")

class Mother:
    def cook(self):
        print("Mother can cook")

class Child(Father, Mother):
    def play(self):
        print("Child can play")

c = Child()

c.drive()
c.cook()
c.play() 

#5.Write a Python program to demonstrate Multilevel Inheritance using classes A , B , and C .(Multilevel Inheritance)
class A:
    def displayA(self):
        print("Class A")
class B(A):
    def displayB(self):
        print("Class B")
class C(B):
    def displayC(self):
        print("Class C")
obj = C()
obj.displayA()
obj.displayB()
obj.displayC() 

#6. Write a Python program to demonstrate Polymorphism using classes Dog and Cat with the same method sound() .(Polymorphism)
class Dog:
    def sound(self):
        print("Dog barks")
class cat:
    def sound(self):
        print("Cat meows")

d=Dog()
d.sound()
c=cat()
c.sound() 

#7. Write a Python program to demonstrate Method Overriding using parent and child classes.(Runtime Polymorphism)
class Parent:
    def display(self):
        print("Parent")
class Child(Parent):
    def display(self):
        print("Child")
c=Child()
c.display() 

#8. Write a Python program to demonstrate Encapsulation using public and private variables.Encapsulation)
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.__marks)
s1=Student("Anagha",85)
print("Public variable:",s1.name)
s1.display() 

#9. Write a Python program to create a BankAccount class with deposit and withdrawal methods.Class, Object, Methods)
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited:",amount)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdrawn:",amount)
        else:
            print("Insufficient balance")
    def display(self):
        print("Current Balance:",self.balance)
account=BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.display() '''

#10 Write a Python program to demonstrate Abstraction using an abstract class Shape and a subclass Square .(Abstraction)
