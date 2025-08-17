# The Perfect Guess Game
# This is a simple number guessing game where the user has to guess a randomly generated number between 1 and 100.

import random


def random_number():
    return random.randint(1, 100)


def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Invalid input. Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def play_game():
    number = random_number()
    attempts = 0
    print("\n//************** Welcome to The Perfect Guess Game! **************//")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        guess = get_user_guess()
        attempts += 1
        if guess == number:
            print(
                f"🎉 Congratulations! You've guessed the number {number} in {attempts} attempts."
            )
            break
        elif guess < number:
            print("📉 Your guess is too low. Try again.")
        else:
            print("📈 Your guess is too high. Try again.")


def main():
    while True:
        play_game()
        choice = input("\nDo you want to play again? (y/n): ").strip().lower()
        if choice not in ("y", "yes"):
            print("Thanks for playing The Perfect Guess Game! Goodbye 👋")
            break


if __name__ == "__main__":
    main()
