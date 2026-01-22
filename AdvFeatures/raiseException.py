a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if(b == 0):
    raise ZeroDivisionError("Hey, our prgram is not meant to divide numbers by zero")
else:
    print(f"The division {a}/{b} is: {a/b}")