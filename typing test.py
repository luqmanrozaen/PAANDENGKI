import random
import time

def typing_speed_test():
    words = ["elephant", "giraffe", "chocolate", "butterfly", "adventure"]
    word = random.choice(words)

    print("Welcome to the typing speed test!")
    print(f"Type the following word as fast as you can: {word}")
    input("Press Enter to start...")

    start_time = time.time()
    user_input = input("Type here: ")
    end_time = time.time()

    if user_input == word:
        time_taken = round(end_time - start_time, 2)
        print(f"Great job! You took {time_taken} seconds.")
    else:
        print(f"Oops! You typed it incorrectly. The correct word was '{word}'. Try again!")

if __name__ == "__main__":
    typing_speed_test()

