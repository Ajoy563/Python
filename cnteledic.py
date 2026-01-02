#input: 1 2 3 4 (5 6 7) 8 9
l = input("Enter a list of elements separated by space: ")
l=l.split(" ")
c=0
for i in l:
    if '(' in i:
        break
    c+= 1
print("Count of elements until a tuple is encountered:", c)