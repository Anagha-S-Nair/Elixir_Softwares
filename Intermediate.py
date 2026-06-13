#Convert string to lowercase and count vowels
str1="python programming"
print(str1.lower())
vowels='aeiou'
count=0
for char in str1:
    if char in vowels:
        count+=1
print("Number of vowels: ",count)

#Remove spaces and find length
str1=" Hello world "
print(len(str1))
print("After: ", len(str1.replace(" ","")))

#Replace spaces with _and convert to uppercase
str1=" Hello world"
print(str1.replace(" ","-").upper())

#Split sentence and print each word
str1="python programming".split()
print(str1)
for word in str1:
    print(word)

#Count number of words using split()
str1="hello world".split()
print("Number of words: ",len(str1))

#Find longest word using split()
str1="hello programming".split()
print("Maximum word: ", max(str1))

#Check if substring exists using find()
str1="welcome to python programming"
if str1.find('python') != -1:
    print("Substring found ")
else:
    print("Substring not found")