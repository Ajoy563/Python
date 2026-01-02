s=input("Enter a string:")
r=s.split(" ")
e=r[::-1]
for i in range(len(e)):
    print(e[i], end=" ")