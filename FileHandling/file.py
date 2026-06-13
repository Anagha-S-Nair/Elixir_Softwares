#1. Write a Python program to create a file and write data into it

'''file=open("s.txt","w")
file.write("Hello world")
file.close()
print("Data written to file successfully.")

#2. Write a Python program to read a file
file=open("s.txt","r")
data=file.read()
print(data)
file.close() 

#3. Write a Python program to append data to a file.
file=open("s.txt","a")
file.write("\nWelcome to Python programming.")
file.close()
print("Data appended to file successfully") 

#4. Write a Python program to read a file line by line.
file=open("s.txt","r")
for line in file:
    print(line.strip())
file.close() 

#5. Write a Python program using readlines() .
file=open("s.txt","r")
lines=file.readlines()
for line in lines:
    print(line.strip())
file.close() 

#6. Write a Python program using writelines() .
file=open("s.txt","w")
lines=["Hello ","Anagha "]
file.writelines(lines)
file.close() 

#7. Write a Python program demonstrating tell() .
file=open("s.txt","r")
print("Current file position:", file.tell())
file.read(5)
print("Current file position after reading 5 characters:", file.tell())
file.close() 

#8.Write a Python program demonstrating seek() 
file=open("s.txt","r")
print(file.read(5))
file.seek(0)
print(file.read(5))
file.close() '''

#9. Write a Python program to create a file using exclusive mode.
file=open("newfile.txt","x")
file.write("Welcome to programming.")
file.close()
print("File created and data written successfully.")

