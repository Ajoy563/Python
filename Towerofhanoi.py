def towerofhanoi(n,a,b,c):
    if n==1:
        print(f"\nMove ring {n} from rod {a} to rod {b}.")
    else:
        towerofhanoi(n-1,a,c,b)
        print(f"\nMove ring {n} from rod {a} to rod {b}.")
        towerofhanoi(n-1,c,b,a)

r=int(input("Enter the number of Rings: "))
towerofhanoi(r,"Source","Destination","Temporary")
