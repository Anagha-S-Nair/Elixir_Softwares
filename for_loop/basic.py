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