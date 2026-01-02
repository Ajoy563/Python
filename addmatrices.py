def display(a,r,c):
    for i in range(r):
        for j in range(c):
            print(a[i][j], end=' ')
        print("\n")

r=int(input("Enter no of Rows: "))
c=int(input("Enter no of Columns: "))
mat1=[]
for i in range(1,r+1):
    row=[]
    for j in range(1,c+1):
        v=int(input(f"\nEnter elements [{i},{j}]: "))
        row.append(v)
    mat1.append(row)
print("\nMatrix 1:\n")
display(mat1,r,c)
mat2=[]
for i in range(1,r+1):
    row=[]
    for j in range(1,c+1):
        v=int(input(f"\nEnter elements [{i},{j}]: "))
        row.append(v)
    mat2.append(row)
print("\nMatrix 2:\n")
display(mat2,r,c)
result=[]
for i in range(1,r+1):
    row=[]
    a=0
    for j in range(1,c+1):
        row.append(0)
    result.append(row)
for i in range(r):
    for j in range(c):
        result[i][j]=mat1[i][j] + mat2[i][j]
print("\nResultant Matrix:\n")
display(result,r,c)
