#!/usr/bin/python3
import random

#Greet Player and Get guess
def start_game(guess_count):
    random_num = random.randint(1, 10)
    #Make sure input of guess limit is a number
    try:
        how_many_guesses = int(guess_count)
    except ValueError:
        print(f"Did not recoginzed the amount of guesses as a number, defaulting to 3")
        how_many_guesses = 3
    index = 0

    print(f"Hello! Welcome to the number guessing game, you have {how_many_guesses} guesses. Your guess: ")
    while index != how_many_guesses:
        # Check if limit has been reached
        if index == how_many_guesses:
            break
        # Get user input for each guess
        user_input = input("Number: ")
        #Checks if guess is a int if not set guess to None 
        try:
            user_input = int(user_input)
        except ValueError:
            print("This is not a number try again.")
            user_input = None
        # If user input is not None it will check if guess is correct.
        if user_input != None:
            if user_input == random_num:
                print(f"Congrats {user_input} was the correct number!")
                break
            elif user_input > random_num:
                print("Too high!")
            elif user_input < random_num:
                print("Too low!")
            index+=1

#start_game()
start_game(4)
