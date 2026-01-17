# We are going to write a program that generates a random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
# Hint: Use the random module.

from random import randint

n = randint(1, 100)
guesses = 0

while(True):
    guesses += 1
    a = int(input("Guess the number:"))
    
    if(a > n):
        print("Lower number please!")
    elif(a == n):
        break
    else:
        print("Higher number please!")
        
print(f"You have guessed the number {n} in {guesses} attempts.")