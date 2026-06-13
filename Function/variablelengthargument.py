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