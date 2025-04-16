import random

def main():
    """Start a number guessing game between 1 - 100."""
    print("Guess the number!")

    x = random.randint(1, 100)
    guess = None

    while guess != x:
        try:
            guess = int(input("Pick a number between 1 to 100: "))
            if guess < 1 or guess > 100:
                print("Please pick a number *within* the range 1 to 100.")
                continue
            if guess == x:
                print("You genius!")
            elif guess < x:
                print("Try a bigger number.")
            else:
                print("Try a smaller number.")
        except ValueError:
            print("Please enter a valid number.")

main()
