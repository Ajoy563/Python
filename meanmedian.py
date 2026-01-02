def avg(x):
    s=0
    for i in x:
        s+=int(i)
    average=s/len(x)
    return average
def median(x):
    n1=-1
    if(len(x)%2)==0:
        n1=(len(x)//2) + 1
    else:
        n1=len(x)//2    
    return x[n1]
n=input("Enter numbers with space: ").split(" ")
print("Average is: ", avg(n))
print("Median is: ", median(n))