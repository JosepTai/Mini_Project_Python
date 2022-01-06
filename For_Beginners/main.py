import os
import time
import sys


def get_file_to_run(list_file):
    print("List file can run:")
    for item in list_file:
        print(f"{list_file.index(item)}. {item}")
    flag_input = False
    user_choose = input("--- Please choose file ----\n- Input number's file \n- Input -1 to exit \n Your choose:  ")
    if user_choose == '-1':
        return "stop"
    else:
        while not flag_input:
            if not user_choose.isdecimal():
                print("----- Please enter number! -----")
                user_choose = input(
                    "--- Please choose file ----\n- Input number's file \n- Input -1 to exit \n Your choose:  ")
            elif int(user_choose) not in range(0, len(list_file)):
                print(f"----- Please choose number between 0 - {len(list_file) - 1}! -----")
                user_choose = input(
                    "--- Please choose file ----\n- Input number's file \n- Input -1 to exit \n Your choose:  ")
            else:
                flag_input = True

        return list_file[int(user_choose)]


def get_list_file(dir_run):
    current_path = os.getcwd() + f"\{dir_run}"
    all_file = [os.path.join(current_path, f) for f in os.listdir(current_path) if
                os.path.isfile(os.path.join(current_path, f))]
    list_file = [item.split('\\')[-1] for item in all_file if 'main.py' not in item]
    return list_file


if __name__ == '__main__':

    dir_run = sys.argv[1]
    while True:
        list_file = get_list_file(dir_run)
        file_run = get_file_to_run(list_file)
        if file_run == 'stop':
            break
        else:
            print(f"File {file_run} is running...")
            time.sleep(1)
            print(f"\n############ {file_run} ############\n")
            os.system(f'py {dir_run}/{file_run}')
            print('\n############ Succeed ############ \n')
