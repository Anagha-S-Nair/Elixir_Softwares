#convert the string to lowercase and count vowels
str1="python programming"
print(str1.lower())
vowels='aeiou'
count=0
for char in str1:
    if char in vowels:
        count+=1
print("Number of vowels: ",count)
