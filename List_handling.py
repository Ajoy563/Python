friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

# friends.append("Ajoy") #Insert at the end of the list
# print(friends)

l1 = [1,8,7,2,21,15]

# l1.reverse()
# print(l1) #Reverse the whole list

# l1.sort() #Sort in ascending order
# print(l1)

# l1.sort(reverse=True) #Sort in decending order
# print(l1)

# l1.insert(3, 12) #Insert the value at the given index (pos, val)
# print(l1)

# print(l1.pop(2)) #Delete element at index and return value
# print(l1)

# l1.remove(21) #Delete element by its value
# print(l1)

a = [1,2,2,3,4,2,6,2] #Remove 2 from the list
n=True
while(n) :
  if 2 in a:
    a.remove(2)
  else :
    n=False
print(a)

# append()      # adds an element at the end of the list
# extend()      # adds multiple elements from another list
# insert()      # inserts an element at a given index
# remove()      # removes the first matching element
# pop()         # removes and returns element at given index (last by default)
# clear()       # removes all elements from the list
# index()       # returns index of first matching element
# count()       # returns number of occurrences of an element
# sort()        # sorts the list in ascending order by default
# reverse()     # reverses the order of the list
# copy()        # returns a shallow copy of the list