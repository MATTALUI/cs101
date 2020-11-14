from random import randint

min = 1
max = 75
target_number = randint(min, max)
guess = None
guess_count = 0

while guess != target_number:
    guess = int(input(f"Guess number between {min} and {max}: "))
    guess_count += 1
    if guess > target_number:
        print("Too High.\n")
    if guess < target_number:
        print("Too Low.\n")

print(f"You did it! You guessed the right number in {guess_count} tries.")
