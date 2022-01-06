"""Resuire
    - User input a paragraph word to program
    - Program random a word longer 5 character
    - User have len(word)/2 times to try input it
    - First try: program show random a location character in word
    - If user input wrong answer, program show more 1 character
    - Mission:  find this word with times try minimum
"""

import random


def get_list_word():
    print("-------------------------------------------")
    paragraph = str(input("Please input your paragraph: "))
    special_char = "!#$%^&*().,+-/\\:\(){}\'\"@"
    list_word = []
    while len(list_word) == 0:
        if paragraph == "":
            print("----- Warning -----\nParagraph is empty. Please try again!")
            paragraph = str(input("Please input your paragraph: "))
        else:
            len_word = input("Input len word to find: ")
            if not len_word.isdecimal():
                print("Please input number!")
            else:
                for item in special_char:
                    paragraph = paragraph.replace(item, " ")
                list_word = list(set([item.lower() for item in paragraph.split() if len(item) >= int(len_word)]))
                if len(list_word) == 0:
                    print(f"----- Waring -----\nDon't have word's length larger than {len_word}\nPlease try again.")
                    paragraph = str(input("Please input your paragraph: "))

    return list_word


def show_word(word, list_show):
    list_idx = [item for item in range(0, len(word))]
    while len(list_idx) > 0:
        temp = int(random.choice(list_idx))
        if list_show[temp] == '*':
            list_show[temp] = word[temp]
            print("Suggest:\t\t" + "".join(list_show))
            break
        else:
            list_idx.remove(temp)
    return list_show


def run(word_result):
    time_try = int(len(word_result) / 2)
    user_try = 0
    list_show = ['*' for i in range(0, len(word_result))]

    while user_try <= time_try:
        print(f"\nYou have {time_try - user_try} times try. Good luck!\n")
        user_try += 1
        list_show = show_word(word_result, list_show)
        user_answer = input("### Your answer: ")
        if user_answer == word_result:
            break
        else:
            print("Oh. Your answer is not match. Please try again.")

    if user_try > time_try:
        print("You don't have any times try(T.T)")
    else:
        print(f"Congratulations! You win with {user_try} try.")
    print(f"##### Result:  {word_result} #####")


if __name__ == '__main__':
    list_word = get_list_word()
    word_result = random.choice(list_word)
    run(word_result)
