"""
Winning Rules as follows :

Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.

"""
import os
import random
import time


def get_choice(input):
    if input == 1:
        return "Rock"
    elif input == 2:
        return "Paper"
    elif input == 3:
        return "Scissor"


def check_result(user_choice, computer_choice):
    if user_choice == "Paper" and computer_choice == "Rock":
        return 'win'
    elif user_choice == "Rock" and computer_choice == "Scissor":
        return 'win'
    elif user_choice == "Scissor" and computer_choice == "Paper":
        return 'win'
    elif user_choice == computer_choice:
        return 'equal'
    return False


def run():

    while True:
        os.system('cls')
        print("Winning Rules of the Rock paper scissor game as follows: \n"
              + "Paper vs Rock -> Paper wins \n"
              + "Rock vs Scissor -> Rock wins \n"
              + "Scissor vs Paper -> Scissor wins \n")
        print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
        user_input = input("Your choice: ")
        user_choice = get_choice(int(user_input))
        print(f"You choise: {user_choice}")
        print("Computer is choice now...")
        time.sleep(1)
        computer_input = random.randint(1, 3)
        computer_choice = get_choice(computer_input)
        print(f"Computer choise: {computer_choice}")
        result = check_result(user_choice, computer_choice)
        if result == 'win':
            print("---- You wins ----")
        elif result == 'equal':
            print("------- Same choice. No one win -------")
        else:
            print("----- Oh. You are loser. (T.T) -----")

        resume = input("Press Enter to continue!\n")
        if resume != "":
            break


if __name__ == '__main__':
    run()
