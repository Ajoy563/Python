num=int(input("Enter a number:"))
for i in range(1,num+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
if c==2:
    print("Prime")
else:
    print("Not Prime")