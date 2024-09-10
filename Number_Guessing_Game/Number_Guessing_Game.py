import random
import art
def number_guessing_game():
    print(art.image)
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    print("I am thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard': ").lower()
    
    if difficulty == "easy":
        life = 10
        while life > 0:
            print(f"You have {life} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == number:
                print(f"You got it! The answer was {number}. ")
                break
                
            elif guess != number:
                if guess > number:
                    print("Too high!")
                    print("Guess again.\n")
                    
                    life -= 1

                elif guess < number:
                    print("Too Low!")
                    print("Guess again. \n")
                    life -= 1

            if life == 0:
                    print("You've run out of guesses, you lose!")
                    print(f"The right number was {number}")
                    break

    elif difficulty == "hard":
        life = 5
        while life > 0:
            print(f"You have {life} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == number:
                print(f"You got it! The answer was {number}. ")
                break

            elif guess != number:
                if guess > number:
                    print("Too high!")
                    print("Guess again.\n")
                    
                    life -= 1

                elif guess < number:
                    print("Too Low!")
                    print("Guess again. \n")
                    life -= 1

            if life == 0:
                print("You've run out of guesses, you lose!")
                print(f"The right number was {number}")
                break

                
number_guessing_game()