'''s=input("Enter string: ")
st=""
for i in range(len(s)):
    if s[i].isalpha() or s[i].isspace():
        st+=s[i]
st=st.split(' ')
r=[]
for i in st:
    r.append(i[0])
print("\nInitial character of each word: ",r)'''

s=input("Enter string: ")
s=s.split(" ")
print("\nInitial character of each word: ")
for i in s:
    c=i[0]
    print(c, end=' ')