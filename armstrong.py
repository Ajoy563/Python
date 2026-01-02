print("Armstrong numbers between 1 to 1000 are:")
for i in range(1,1000):
    hundred= i//100
    tens=(i//10)%10
    ones=i%10
    sum=(hundred**3)+(tens**3)+(ones**3) 
    if i==sum:
        print(i, end=" ")
