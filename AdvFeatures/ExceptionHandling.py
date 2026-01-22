# There are many built-in exceptions which are raised in python when something goes wrong.
# Exception in python can be handled using a try statement. The code that handles the exception is written in the except clause.

try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)
    
print("Thank You")

# When the exception is handled, the code flow continues without program interruption.
# We can also specify the exception to catch like below:

# try: 
#     # Code
# except ZeroDivisionError:
#     # Code
# except TypeError:
#     # Code 
# except: # Code # All other exceptions are handled here.