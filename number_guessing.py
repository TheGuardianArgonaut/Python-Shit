#!/usr/bin/python3
import random

#Greet Player and Get guess
def start_game():
    random_num = random.randint(1, 10)
    how_many_guesses = 3
    index = 0
    print(f"Hello! Welcome to the number guessing game, you have {how_many_guesses} guesses. Your guess: ")
    while index != 3:
        user_input = input("Number: ")
        try:
            user_input = int(user_input)
        except ValueError:
            print("This is not a number try again.")
            user_input = None
        if user_input != None:
            if user_input == random_num:
                print(f"Congrats {user_input} was the correct number!")
                break
            elif user_input > random_num:
                print("Too high!")
            elif user_input < random_num:
                print("Too low!")
            index=+1

start_game()
        
