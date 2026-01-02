def findSecondLargest(l):
    max = l[0]
    secondMax = -1
    for i in range(len(l)): 
        if l[i] > max:
            secondMax = max
            max = l[i]
        elif l[i] > secondMax and l[i] != max:
            secondMax = l[i]
    return secondMax
ls=input("Enter elements with space: ").split()
l=[int(i) for i in ls]
secondLargest = findSecondLargest(l)
if secondLargest == -1:
    print("No second largest number found.\n")
else :
    print("The second largest number is: ", secondLargest)
