num= int(input("Enter the number of key-value pairs: "))
keys = []
values = []
for i in range(num):
    k= input(f"Enter key {i+1}: ")
    v= int(input(f"Enter value for key {k}: "))
    keys.append(k)
    values.append(v)
original= dict(zip(keys, values))
inverted=dict(zip(original.values(), original.keys()))
print("Original dictionary:", original)
print("Inverted dictionary:", inverted)