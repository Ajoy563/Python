def square(list):
    for i in range(len(list)):
        list[i]=list[i]**2
    return list

e=input("Enter list of elements seperated by space: ")
e=e.split(" ")
original=[]
for i in e:
    original.append(int(i))
print("\nOriginal list: ",original)
new=square(original)
print("\nList after squaring element: ",new)
print("\nOriginal list after squaring element: ",original)