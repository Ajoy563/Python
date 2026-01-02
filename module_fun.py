def f1(x,y):
    if y<=x:
        return f1(x-y,y)+1
    else:
        return 0
def f2(n,r):
    if n!=0 and r!=0:
        return f2(n-1,r)+f2(n-1,r-1)
    else:
        return 1
def f3(n):
    if n>1:
        return f3(n/2)+1
    else:
        return 0
def f4(m,n):
    if m==0:
        return 1
    elif n>=1 and n<=m:
        return f4(m-1,n)+f4(m-1,n-1)
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
def f5(m,x):
    if m>x:
        return fact(m)/(fact(x)*fact(m-x))
    else:
        return 1