"""
This is a number guessing game
----------------------------------
"""
import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is no high score, it's yours for the taking!") 
    else:
        print("the current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))               


