def https_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not found!"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
        
print(https_status(5000))

# Python 3.10 introduced the match statement, which is similar to the switch statement found in other programming languages.
# The basic syntax of the match statement involves matching a variable against several cases using the case keyword.