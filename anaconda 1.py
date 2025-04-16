import random

def main():
    """Start a colour guessing game."""
    print("Guess The Colour!")

    rainbow = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet"
    ]

    x = random.choice(rainbow)
    guess = None

    while x != guess:
        guess = input("What colour am I thinking of? ").lower()

        if x == guess:
            print(f"You guessed {guess}. Congratulations, you got it right!")
            break
        else:
            print(f"You guessed {guess}. Unfortunately, that's wrong. Try again!")

main()
