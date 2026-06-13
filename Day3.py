#BASIC LEVEL
#1.Create a tuple and access elements using indexing
# t=(1, 2, 3, 4, 5)
# print(t[0])

#2. Convert a list into a tuple
# lst1=[1,4,6,2]
# t1=tuple(lst1)
# print(t1)

#INTERMEDIATE LEVEL
#1. Reverse a list without using built-in functions
'''lst=[2,4,6,8,10]
print(lst[::-1])

#2.Merge two lists into one without using +
lst1=[1,3,5]
lst2=[2,4,6]
lst1.extend(lst2)
print(lst1)

#3. Create a dictionary from two lists
lst1=['Fruit','Dress']
lst2=['Apple','Kurta']
d1=dict()
for i in range(len(lst1)):
    d1[lst1[i]]=lst2[i]
print(d1)

#4. Flatten a nested list
nested=[[1,2],[3,4],[5,6]]
flat=[]
for i in nested:
    for j in i:
        flat .append(j)
print(flat)

#5. Find missing numbers in a squence
lst=[1,2,4,5,7]
for i in range(lst[0],lst[-1]+1):
    if i not in lst:
        print(i)'''

#ADVANCED LEVEL
#1. Rotate a list by k positions
'''num=[9,5,2,1]
length=len(num)
k=2
while(k!=0):
    temp=num[0]
    for i in range(length-1):
        if i!=(length-1):
            num[i]=num[i+1]
    num[length-1]=temp
    k-=1
print(num)

#2.Find all pairs in a list whose sum is equal to a target
lst=[1,2,3,4,5]
target=5
sum=0
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==target:
            print(lst[i],lst[j])

#3. Implement a stack using a list
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
x=stack.pop()
print("Popped element:",x)
print("Stack afer popping:",stack)

#4. Implement a queue using a list
queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
y=queue.pop(0)
print("Dequeued element:",y)
print("Queue after dequeuing:",queue)

#5. Find the first non-repeating element in a list
lst1=[1,2,3,2,1,4]
for i in lst1:
    if lst1.count(i)==1:
        print(i)
        break

#6.Group elements by frequency
lst2=[1,2,3,2,1,4]
freq={}
for i in lst2:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

#7. Find intersection of two lists
lst3=[1,2,3,4]
lst4=[3,4,5,6]
for i in lst3:
    if i in lst4:
        print(i)
    
#8.Implement a simple hashmap using dictionary
hashmap={1:'one',2:'two',3:'three'}
print(hashmap[1])

#9.Detect duplicates efficiently
lst5=[1,2,3,4,2,5]
print(set(lst5))

#10.Find longest consecutive sequence in a list
lst6=[10,20,30,40,50]
lst6.sort()


#FOR LOOP
#BASIC
#1. Print numbers from 1 to 10
for i in range(1,11):
    print(i,end=' ')

#2. Print even numbers from 1 to 50
for i in range(1,51):
    if i%2==0:
        print(i,end=' ')

#3.Find sum of numbers from 1 to n
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#4. Print multiplication table of a number
num=5
for i in range(1,11):
    print(num,'*',i,'=',num*i)

#5.Iterate through a list and print each element
lst=[1,2,3,4,5]
for i in lst:
    print(i,end=' ')

#INTERMEDIATE
#1. count vowels in a string
s=input("Enter a string:")
count=0
vowels='aeiouAEIOU'
for i in s:
    if i in vowels:
        count+=1
print("Number of vowels:",count)

#2.Find factorial of a number
n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial:",fact)

#3. Reverse a string using loop
s=input("Enter a string:")
rev=''
for i in s[::-1]:
    rev+=i
print("Reversed:",rev)

#4.Find sum of digits of a number
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    rem=n%10
    sum=sum+rem
    n=n//10
print("Sum of digits:",sum)

#ADVANCED 
#1.Print pyramid pattern
n=int(input("Enter number of rows:"))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for k in range(i+1):
        print('* ',end=' ')
    print()

#2. Find prime number in a range
n=int(input("Enter a number:"))
flag=0
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    else:
        print(i,end=' ')

#3. Generate Fibonacci series
a,b=0,1
for i in range(10):
    print(a,end=' ')
    c=a+b
    a=b
    b=c

#4.Find common elements in two lists using loop
lst7=[1,2,3,4]
lst8=[3,4,5,6]
for i in lst7:
    for j in lst8:
        if i==j:
            print(i,end=' ') 

#ADVANCED
#1.Guess the number game
secret=7
guess=int(input("Guess the number :"))
if guess==secret:
    print("Success")
else:
    print("Try again") '''

