import os
import time


def get_dir_to_run(list_dir):
    print("List dir can run:")
    for item in list_dir:
        print(f"{list_dir.index(item)}. {item}")
    flag_input = False
    user_choose = input("--- Please choose dir ----\n- Input number's dir \n- Input -1 to exit \n Your choose:  ")
    if user_choose == '-1':
        return "stop"
    else:
        while not flag_input:
            if not user_choose.isdecimal():
                print("----- Please enter number! -----")
                user_choose = input("--- Please choose dir ----\n- Input number's dir \n- Input -1 to exit \n Your choose:  ")
            elif int(user_choose) not in range(0, len(list_dir)):
                print(f"----- Please choose number between 0 - {len(list_dir) - 1}! -----")
                user_choose = input("--- Please choose dir ----\n- Input number's dir \n- Input -1 to exit \n Your choose:  ")
            else:
                flag_input = True

        return list_dir[int(user_choose)]


def get_list_dir():
    current_path = os.getcwd()
    all_dir = [os.path.join(current_path, f) for f in os.listdir(current_path) if
                os.path.isdir(os.path.join(current_path, f))]
    list_dir = [item.split('\\')[-1] for item in all_dir if '.idea' not in item]
    return list_dir


if __name__ == '__main__':
    while True:
        list_dir = get_list_dir()
        dir_run = get_dir_to_run(list_dir)
        if dir_run == 'stop':
            break
        else:
            print(f"dir {dir_run} is running...")
            time.sleep(1)
            print(f"\n############ {dir_run} ############\n")
            os.system(f'py {dir_run}/main.py {dir_run}')
            print('\n############ Succeed ############ \n')
