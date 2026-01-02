s=input("Enter a string: ")
s=s.replace(" ","")
s=s.lower()
l=[]
for i in s:
    c=ord(i)
    if c not in l:
        l.append(c)
l.sort()
print(l)
for i in l:
    c=chr(i)
    cnt=s.count(c)
    print(c,":",cnt)
    
