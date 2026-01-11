# st = "Hey Ajoy, You are amazing"

# f = open("myfile.txt", "w") # Writing a file
# f.write(st)
# f.close

# f = open("myfile.txt", "r") # Reading a file
# data = f.read()
# print(data)
# f.close()

# f = open("file.txt")
# lines = f.readlines()  #Return a list of lines
# print(lines, type(lines))

# line1 = f.readline() #Return 1st line
# print(line1, type(line1))

# line2 = f.readline() #Return next line
# print(line2, type(line2))

# line3 = f.readline() #Return next line
# print(line3, type(line3))

# line4 = f.readline() #Return next line
# print(line4, type(line4))

# line5 = f.readline() #Return next line, if not nothing
# print(line5 == "")

# line = f.readline() #Take the 1st line
# while(line != ""):
#   print(line) #Print until end of file
#   line = f.readline()

# f.close()

# ----MODES OF OPENING A FILE----
# r – open for reading
# w - open for writing
# a - open for appending
# + - open for updating.
# ‘rb’ will open for read in binary mode.
# ‘rt’ will open for read in text mode.


# ----WITH STATEMENT----
with open("myfile.txt") as f:  #Don't need too close the file
  print(f.read())