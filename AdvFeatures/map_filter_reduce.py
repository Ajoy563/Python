# Map Example
l = [1, 2, 3, 4, 5, 6]

square = lambda x: x*x
sqList = map(square, l)

print(list(sqList))

# Filer Example
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Function

from functools import reduce
sum  = lambda a,b : a+b
print(reduce(sum, l))