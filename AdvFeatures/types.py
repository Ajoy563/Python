# Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.

n : int = 5

name : str = "Ajoy"

def sum(a: int, b: int) -> int:
    return a+b

print(sum(4, 9))