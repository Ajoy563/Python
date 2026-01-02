while(1):
    print("\n1.Linear Search\n2.Binary Search\n3.Exit")
    c=int(input("Enter your choice: "))
    if c==1:
        n=input("\nEnter the elements with space: ")
        n=n.split(" ")
        l=[int(i) for i in n]
        x=int(input("\nEnter the elements to find the position: "))
        if x in l:
            p=l.index(x)
            print(f"\n{x} is found at:{p}")
        else:
            print("\nElement not found")  
    elif c==2:
        n=input("\nFor Binary search, Enter the sorted elements with space: ")
        n=n.split(" ")
        lst=[int(i) for i in n]
        x=int(input("\nEnter the element to find the position: "))
        l=0
        h=len(lst)-1
        f=0
        while(l<=h):
            mid=(l+h)//2
            if(lst[mid]==x):
                print(f"\n{x} is found at:{mid}")
                f=1
                break
            elif(lst[mid] > x):
                h=mid-1
            else:
                l=mid+1
        if f==0:
            print("\nElement not found")
    elif c==3:
        exit()
    else:
        print("\nInvalid Choice!")
            