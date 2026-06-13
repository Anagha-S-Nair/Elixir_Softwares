str1="abc123@#"
print("Original string: ", str1)
result=""
for char in str1:
    if char.isalpha():
        result+=char
print("After removal: ",result)
