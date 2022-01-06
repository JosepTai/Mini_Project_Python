from msvcrt import getch
import random
import os

map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]
score = 0

def reset_map():
    for x in range(0,4):
        for y in range(0,4):
            map[x][y] = 0

def get_value_col(idx):
    temp = [0, 0, 0, 0]
    for i in range(0, 4):
        temp[i] = map[i][idx]
    return temp


def set_value_col(idx, list_value):
    flag = False
    for i in range(0, 4):
        if map[i][idx] != list_value[i]:
            map[i][idx] = list_value[i]
            flag = True
    return flag


def change_value(temp, score, flag):
    if flag:
        temp.reverse()
    temp = [item for item in temp if item != 0]
    while len(temp) != 4:
        temp.append(0)
    idx = 0
    while idx < 3:
        if temp[idx] == temp[idx + 1]:
            temp[idx] += temp[idx + 1]
            temp[idx + 1] = 0
            score += temp[idx]
        idx += 1
    if flag:
        temp.reverse()
    temp = [item for item in temp if item != 0]
    return temp, score


def go_arrow(score, type):
    move = False
    for x in range(0, 4):
        if type == 'up' or type == 'down':
            temp = get_value_col(x)
        else:
            temp = map[x].copy()
        # ----------------------------------------------------------
        if type == 'down' or type == 'right':
            temp, score = change_value(temp, score, True)
        else:
            temp, score = change_value(temp, score, False)
        # ----------------------------------------------------------
        while len(temp) != 4:
            if type == 'down' or type == 'right':
                temp.insert(0, 0)
            else:
                temp.append(0)
        # ----------------------------------------------------------
        if type == 'up' or type == 'down':
            temp_set_value = set_value_col(x, temp)
            move = temp_set_value if temp_set_value else move
        else:
            if map[x] != temp:
                map[x] = temp
                move = True
    if move:
        set_new_value()
    return score


# def go_up(score):
#     move = False
#     for x in range(0, 4):
#         temp = get_value_col(x)
#         temp, score = change_value(temp, score, False)
#         while len(temp) != 4:
#             temp.append(0)
#         temp_set_value = set_value_col(x, temp)
#         move = temp_set_value if temp_set_value else move
#     if move:
#         set_new_value()
#     return score
#
#
# def go_left(score):
#     move = False
#     for x in range(0, 4):
#         temp = map[x].copy()
#         temp, score = change_value(temp, score, False)
#         while len(temp) != 4:
#             temp.append(0)
#         if map[x] != temp:
#             map[x] = temp
#             move = True
#     if move:
#         set_new_value()
#     return score
#
#
# def go_down(score):
#     move = False
#     for x in range(0, 4):
#         temp = get_value_col(x)
#         temp, score = change_value(temp, score, True)
#         while len(temp) != 4:
#             temp.insert(0, 0)
#         temp_set_value = set_value_col(x, temp)
#         move = temp_set_value if temp_set_value else move
#     if move:
#         set_new_value()
#     return score
#
# def go_right(score):
#     move = False
#     for x in range(0, 4):
#         temp = map[x].copy()
#         temp, score = change_value(temp, score, True)
#         while len(temp) != 4:
#             temp.insert(0,0)
#         if map[x] != temp:
#             map[x] = temp
#             move = True
#     if move:
#         set_new_value()
#     return score


def get_row():
    inkey = ord(getch())
    return inkey


def set_new_value():
    ran_x = [0, 1, 2, 3]
    ran_y = [0, 1, 2, 3]
    list_ran = []
    for x in ran_x:
        list_ran += [str(x) + "|" + str(item) for item in ran_y]
    while len(list_ran) > 0:
        result_ran = random.choice(list_ran)
        list_ran.remove(result_ran)
        result_ran = result_ran.split("|")
        location_x = int(result_ran[0])
        location_y = int(result_ran[1])
        if map[location_x][location_y] == 0:
            map[location_x][location_y] = 2
            return


def show_map(score):
    for x in range(0, 4):
        print(f"{map[x][0]}\t{map[x][1]}\t{map[x][2]}\t{map[x][3]}")
    print(f"Your score: {score}")


def check_map():
    if 2048 in map:
        return True
    return False


def run(score):
    reset_map()
    set_new_value()
    set_new_value()

    while True:
        os.system('cls')
        show_map(score)
        if check_map():
            print("******* You Won!!! *******")
        # Get key
        inkey = get_row()
        if inkey == 72:
            # score = go_up(score)
            score = go_arrow(score, 'up')
        elif inkey == 75:
            # score = go_left(score)
            score = go_arrow(score, 'left')
        elif inkey == 80:
            # score = go_down(score)
            score = go_arrow(score, 'down')
        elif inkey == 77:
            # score = go_right(score)
            score = go_arrow(score, 'right')
        elif inkey == 32:
            return


if __name__ == '__main__':
    while True:
        print(
            "User arrow: up | down | left | right \n ------ Press Space to start game ------  \n ------ Press Space one time to stop game ------")
        inkey = get_row()
        if inkey == 32:
            run(0)
