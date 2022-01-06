"""Require
    - Input 2 number: low and up
    - Program random a number between low and up
    - User have log(up-low, 2) times to try input answer
"""

import random
import math


def user_input():
    low = up = 0
    flag = False
    while not flag:
        low = input("Enter Low Number: ")
        up = input("Enter UP Number: ")
        if not low.isdecimal() or not up.isdecimal():
            print("----- Please enter number! -----")
        elif int(low) > int(up):
            print(f'{low} is bigger than {up}. Please try again')
        else:
            flag = True
    return int(low), int(up)


if __name__ == '__main__':
    # Get user input 2 number
    low, up = user_input()

    # Set up result of process
    result = random.randint(low, up)

    # Get count try to enter user result
    count_try = int(math.log(up - low + 1, 2))
    print(f"You have {count_try} try")
    user_try = 0

    # Get user answer
    while user_try < count_try:
        user_try += 1
        user_answer = input("Please input your answer: ")
        # Check answer is int
        if not user_answer.isdecimal():
            print("----- Please enter number! -----")
        elif int(user_answer) == result:
            break
        else:
            print(f"Your answer {user_answer} is not correct. Please try again.")
            print(f"---- You have {count_try - user_try} try ----")

    if user_try > count_try:
        print("You don't have any try!")
        print(f"Result: {result}")
    else:
        print(f"Congratulations! You win with {user_try} try.")
