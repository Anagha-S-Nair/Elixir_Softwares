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