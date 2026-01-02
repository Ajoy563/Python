s=input("Enter a string:")
while s:
    c=s[0]
    cnt=s.count(c)
    print(c,":",cnt)
    s=s.replace(c,"")
