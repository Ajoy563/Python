s=input("Enter a String:")
l=len(s)
for i in range(l):
    if s[::]==s[::-1]:
        print("Palindrome")
        break
    else:
        print("Not Palindrome")
        break