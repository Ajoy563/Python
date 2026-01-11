# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("poem.txt") as f:
  content = f.read()
if("twinkle" in content):
  print("Yes, it contain twinkle word")
else:
  print("No, it contain twinkle word")
  