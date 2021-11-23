#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Nov 2021
# this program does the number guessing game

import random

some_variable = random.randint(1, 100)  # a number between 1 and 100


def main():
    # this program is the number guessing game

    guess = int(input("Enter a number between 0-9: "))

    if guess == 4:
        print("You guessed correct!")
        print("")
    else:
        print("Incorrect , The number was 4")
        print("")

    print("Done.")


if __name__ == "__main__":
    main()
