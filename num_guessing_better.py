#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 11, 2021
# This program makes a random number and then has the user guess it
# The user will get score based on their guess

# this is a module that I found to generate random numbers
# found on
# https://www.programiz.com/python-programming/examples/random-number
import random


# this is the fucntion that does everything
def random_number_fun():
    # make the random number
    random_num = random.randint(0, 9)
    random_num = 7
    # just as a test to make sure it was working
    print(random_num)

    # get the users guess
    user_num = input("What do you think the number is: ")

    # make sure the user inputed an integer
    try:
        int(user_num)
    except ValueError:
        print("'{}' is not a number".format(user_num))
        random_number_fun()
    else:
        # FIRST CHECKING #############
        user_num = int(user_num)
        # check if the user got it right
        if (user_num == random_num):
            print("\nCongratulations you got it right!")
            random_number_fun()

        # check if the user got it wrong
        if (user_num != random_num):
            print("\nSorry you got it wrong")

            # ask user if they think their number is bigger or
            # smaller than their guess
            user_bigger_smaller = input(
                "Do you think the random number was bigger or smaller?(b/s): ")

            # check if the user_num was bigger or smaller than the random_num
            if (user_num < random_num):
                bigger_smaller = "b"
            else:
                bigger_smaller = "s"

            # if they guessed right congratulate them
            if (bigger_smaller == user_bigger_smaller):
                print("\nCongratulations you got it right!")
                random_number_fun()

            else:
                print("\nSorry you got it wrong")
                print("The number was {}".format(random_num))
                random_number_fun()


# initial bootup of the program
if __name__ == "__main__":
    random_number_fun()
