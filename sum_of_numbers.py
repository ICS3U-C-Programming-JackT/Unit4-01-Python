#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: April 8, 2025

# Sum of numbers program in python


def main():

    # Initialize variables
    counter = 0
    sum = 0
    user_number = input("Enter a positive integer here:")

    # Change user number into int with try catch
    try:
        user_number = int(user_number)

        # If bigger than 0, add sums until bigger than positive
        # Else until smaller than negative usernum
        if user_number > 0:
            while counter < user_number:
                counter += 1
                sum += counter
        else:
            while counter > user_number:
                counter -= 1
                sum += counter

        # Show result
        print("The sum of your numbers was", sum)
    except:
        # Show error msg
        print("Please enter a positive integer, you entered", user_number)


if __name__ == "__main__":
    main()
