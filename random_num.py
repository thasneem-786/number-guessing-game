import random

# Generate a random number
number = random.randint(1, 100)

# Get the user's guess
guess = int(input("Guess a number between 1 and 100: "))

# Check if the guess is correct
while guess != number:
  if guess < number:
    print("Too low!")
  else:
    print("Too high!")

  # Get the next guess
  guess = int(input("Guess again: "))

# Print the winning message
print("You win!")
