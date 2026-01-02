s=0
c=0
while True:
    try:
        x=input("Enter numbers or write 'done' to stop:")
        if x=="done":
            print("Count:",c,"Sum:",s,"Average:",round(s/c,2))
            break
        s+=int(x)
        c+=1
    except:
        print("Wrong input!")