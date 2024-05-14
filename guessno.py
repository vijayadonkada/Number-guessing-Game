import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Number of attempts allowed
    max_attempts = 5
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. You have 5 attempts to guess it.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
        
        attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
