st = input("Enter a string:")
print(len(st))
if (" " in st):
    print("No spaces allowed!")
elif (len(st)<3 or len(st)>4):
    print("Must be between 3 or 4 characters!")
if (len(st)==3):
    for i in st:
        for j in st:
            if j != i:
                for k in st:
                  if k != i and k!=j:
                      print(i,j,k)
if (len(st)==4):
    for i in st:
        for j in st:
            if j != i:
                for k in st:
                    if k != i and k != j:
                        for l in st:
                            if l != k and l !=j and l != i:
                                print(i,j,k,l)