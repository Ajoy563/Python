x=int(input("Enter number: "))
def fact(x):
    pro=1
    for i in range(1, x+1):
        pro*=i
    return pro
def factrec(x):
    product=1
    if x==1:
        return 1
    else:
        product= x*factrec(x-1)
        return product
product=factrec(x)
print(f"Factorial of {x}! is ",fact(x))
print(f"Factorial of {x}! by Recursuion is ",product) 
