# d = {} #Empty dictionary
# print(type(d))
 
# e = set() #Empty set not s = {}
# print(type(e))

'''--Properties--
1.Sets are unordered => Element's order doesn't matter
2.Sets are unindexed => Cannot access elements by index
3.There is no way to change items in sets.
4.Sets cannot contain duplicate values.'''

s1 = {1, 2, 5, 32, 5, 5} #{32, 1, 2, 5} unique, unordered, multi data type
# s.add(566)
# print(s1)

'''add()            # adds an element to the set
update()         # adds multiple elements from another set or iterable
remove()         # removes an element (raises error if not found)
discard()        # removes an element (no error if not found)
pop()            # removes and returns a random element
clear()          # removes all elements from the set
copy()           # returns a shallow copy of the set
union()          # returns union of two or more sets
intersection()   # returns common elements of sets
difference()     # returns elements present only in first set
.issubset()      # checking subset or not
.issuperset()    # checking superset or not
symmetric_difference()  # returns elements not common to both sets'''


s2 = {7,8, 1, 78, 5, 2}
print(s1.union(s2))
print(s1.intersection(s2))