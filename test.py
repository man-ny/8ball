import sys
import random
# this is an 8ball python script
#Hello Manny- Try to swap out the While/if for an array. In other words enter the possible answers into an array.

from setuptools.command.easy_install import sys_executable

ans = True

while ans:

    question = input("ask xtoes guru a question ")

    answers = random.randint(1, 4)
    if question == "":
        print("you have to ask wuestion")
        sys.exit()


    elif answers == 1:
        print("Yes, its correct")

    elif answers == 2:
        print("negative")

    elif answers == 3:
        print("possibly")

    elif answers == 4:
        print("Super wrong")

    break

