"""
Python offers multiple libraries to ease our work.
Here we will learn how to take a screenshot using Python.
Python provides a module called pyscreenshot for this task.
It is only a pure Python wrapper, a thin layer over existing backends.
Performance and interactivity are not important for this library.

pip install pyscreenshot
"""

import pyscreenshot
import os


def get_index():
    current_path = os.getcwd() + "/img"
    all_file = [os.path.join(current_path, f) for f in os.listdir(current_path) if
                os.path.isfile(os.path.join(current_path, f))]
    list_file = [item.split('\\')[-1] for item in all_file if '.png' in item]
    return len(list_file) + 1


if __name__ == '__main__':
    image = pyscreenshot.grab()
    index = get_index()
    image.save(f"./img/img_{index}.png")
    choice = input("Are you want show this image?(Y/N)\nChoice: ")
    if choice == 'Y' or choice == 'y':
        image.show()

