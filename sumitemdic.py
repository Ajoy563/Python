num= int(input("Enter the number of key-value pairs: "))
keys=[]
values=[]
for i in range(num):
    k= input(f"Enter key {i+1}: ")
    v= int(input(f"Enter value for key {k}: "))
    keys.append(k)
    values.append(v)
my_dict = dict(zip(keys, values))
print("Resulting dictionary:")
print(my_dict)
s= sum(my_dict.values())
print("Sum of dictionary values:",s)