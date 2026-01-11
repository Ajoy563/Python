# Repeat program 4 for a list of such words to be censored.

word = ["donkey", "another", "still", "water"]

with open("don2.txt") as f:
    content = f.read()
for i in word:
    if(i in content):
        content = content.replace(i, "#" * len(word))

with open("don2.txt", "w") as f:
    f.write(content)