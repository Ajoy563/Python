# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

word = "donkey"

with open("don.txt") as f:
    content = f.read()

if(word in content):
    content = content.replace(word, "#" * len(word))

with open("don.txt", "w") as f:
    f.write(content)