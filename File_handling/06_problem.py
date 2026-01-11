# Write a program to mine a log file and find out whether it contains ‘python’. Aslo find the line number.

with open("word.txt") as f:
    content = f.readlines()
    
for i in range(len(content)):
    if("python" in content[i]):
        print(f"The word 'python' found in line no: {i}")
        break
else:
    print("The word 'python is not present'")