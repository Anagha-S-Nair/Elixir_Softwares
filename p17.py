
def is_palindrome(s):
    if s == s[::-1]:
        print("Palindrome.")
    else:
        print("Not palindrome.")
str1="malayalam"
is_palindrome(str1)