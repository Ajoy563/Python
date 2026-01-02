import module_fun
while(True):
    print("1. F(x, y)=F(x-y,y)+1")
    print("2. F(n, r)=F(n-1,r)+F(n-1, r-1)")
    print("3. F(n)=F(n/2)+1")
    print("4. F(M, N)=F(M-1,N)+F(M-1,N-1)")
    print("5. B(m, x)= m!/(x!(m-x)!)")
    print("6. Exit")
    c=int(input("Enter your choice: "))
    if c==1:
        x=int(input("Enter a number: "))
        y=int(input("Enter a number: "))
        print("Result is: ", module_fun.f1(x,y))
    elif c==2:
        n=int(input("Enter a number: "))
        r=int(input("Enter a number: "))
        print("Result is: ", module_fun.f2(n,r))
    elif c==3:
        n=int(input("Enter a number: "))
        print("Result is: ", module_fun.f3(n))
    elif c==4:
        m=int(input("Enter a number: "))
        n=int(input("Enter a number: "))
        print("Result is: ", module_fun.f4(m,n))
    elif c==5:
        m=int(input("Enter a number: "))
        x=int(input("Enter a number: "))
        print("Result is: ", module_fun.f5(m,x))
    elif c==6:
        print("Exit!")
        exit(0)
    else:
        print("Invalid Choice!")