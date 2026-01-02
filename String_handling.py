# name = "  harry  "

# # print(name[:4]) #same as 0:4
# # print(name[1:]) #same as 1:n-1

# # print(name[-4:-1])

# a = "0123456789"
# print(a[1:7:2])
# print(len(a))
# print(a.endswith("89")) #checking condition
# print(a.startswith("89")) #checking condition

# print(name.capitalize()) #Make 1st letter capital
# print(name.lower()) #convert str into lower character 
# print(name.upper()) #convert str into upper character 
# print(name.title()) #capitalize the 1st letter of each word
# print(name.strip()) #Remove leading and trailing whitespaces

# print("42".zfill(5)) #Pads the strings with zeros on the left, to fill the specified width

# # Other inbuilt function
# # count, find, replace, split, join, isalnum, isalpha, isdigit, isspace

letter = '''Dear <|Name|>,
You are Selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Ajoy").replace("<|Date|>", "1st January, 2026"))