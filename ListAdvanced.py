#sort list without using sort()
lst=[5,2,9,1]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
print("Sorted list: ", lst)

#Find frequency of each element(use list + dictionary)
lst=[5,2,9,1,5]
freq={}
for i in lst:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("Frequency: ", freq)

#Remove all ocurrences of an element from list
lst=[5,2,9,1,5]
element=5
while element in lst:
    lst.remove(element)
print("List after removing element: ", lst)

#Rotate list 
lst=[1,2,3,4]
n=2
rotated=lst[n:]+lst[:n]
print("Rotated list: ", rotated)

#split list into even and odd numbers