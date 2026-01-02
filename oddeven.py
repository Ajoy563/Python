l=input("Enter the elements with space: ")
l=l.split(" ")
odd=[]
even=[]
for i in l:
    if int(i)%2==0:
        even.append(int(i))
    else:
        odd.append(int(i))
print("Odd numbers: ",odd)
print("Even numbers: ",even)