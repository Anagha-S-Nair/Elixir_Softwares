#1. Check if a number(number/string)
value=input("Enter a value: ")
if value==value[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#2.Check Armstrong number
num = int(input("Enter a number: "))
temp = num
sum = 0
digits = len(str(num))
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10
if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

#3. Check if Character is Vowel or Consonant
ch = input("Enter a character: ")
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")

#4. Menu-Based Program Using if-elif
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    print("Result =", a / b)
else:
    print("Invalid Choice")

#5. Check if a Number Lies Between Two Numbers
num = int(input("Enter number: "))
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
if start < num < end:
    print("Number lies between")
else:
    print("Number does not lie between")
