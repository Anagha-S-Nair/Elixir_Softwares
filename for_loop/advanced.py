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