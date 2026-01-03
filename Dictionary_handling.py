marks = {
  "Ajoy": 100,
  "spandan": 83,
  "Santanu": 53
}

''' --Properties--
1.It is unordered.
2.It is mutable.
3.It is indexed.
4.Cannot contain duplicate keys.'''

# print(marks, type(marks))
# print(marks["spandan"])
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Ajoy":99, "Renuka": 90})

# print(marks.get("Ajoy"))
# print(marks.get("sourav"))

print(marks.get("Nandini")) #This will give None if data not found
print(marks["Nandini"]) #This will give Error if data not found

'''keys()        # returns all keys of the dictionary
values()      # returns all values of the dictionary
items()       # returns key-value pairs as tuples
get()         # returns value of a key (no error if key not found)
update()      # updates dictionary with another dictionary or key-value pairs
pop()         # removes and returns value of specified key
popitem()     # removes and returns the last inserted key-value pair
clear()       # removes all items from the dictionary
copy()        # returns a shallow copy of the dictionary
setdefault()  # returns value of key; inserts key with default if not present'''
