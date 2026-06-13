#remove duplicate characters using function

def remove_duplicates(s):
    result=""
    for char in s:
        if char  not in result:
            result+=char
    return result


str1="programming"
print("original string: ",str1)
print("string after removing duplicates: ",remove_duplicates(str1))