#!/usr/bin/env python3
import colorama
from colorama import Fore, Style

# initialize colorama
colorama.init()

# define the mutate_string function
def mutate_string(string, position, character):
    # convert the string to a list
    string_list = list(string)
    # change the value at the given position
    string_list[position-1] = character
    # convert the list back to a string and return it
    return ''.join(string_list)

# initialize the result variable
result = ""

# loop to handle multiple input strings
while True:
    # prompt the user for the input string
    string = input(Fore.BLUE + "Enter the string (or type 'exit' to quit): " + Style.RESET_ALL)

    # check if the user wants to exit
    if string.lower() == 'exit':
        break

    # set the result variable to the current string
    result = string

    # loop to handle multiple position and character inputs
    while True:
        # prompt the user for the position and character
        position_input = input(Fore.BLUE + "Enter the position (or type 'exit' to quit): " + Style.RESET_ALL)

        # check if the user wants to exit
        if position_input.lower() == 'exit':
            break

        try:
            # convert position_input to an integer
            position = int(position_input)

            # check if position is within the string length
            if position > len(result):
                print(Fore.RED + f"Position {position} is out of range. Please enter a position less or equal than {len(result)}." + Style.RESET_ALL)
            else:
                # loop to handle multiple character inputs
                while True:
                    character = input(Fore.BLUE + "Enter the character: " + Style.RESET_ALL)
                    # check if the input is a single character
                    if len(character) == 1:
                        # call the function with the input values
                        result = mutate_string(result, position, character)
                        # print the result
                        print(Fore.GREEN + "Result:" + Style.RESET_ALL, result)
                        break
                    elif character.lower() == 'exit':
                        break
                    else:
                        print(Fore.RED + "Please enter only one character or type 'exit' to quit." + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + "Please enter a valid integer for the position." + Style.RESET_ALL)

    # ask the user if they want to enter another string
    response = input(Fore.BLUE + "Do you want to enter another string? (y/n): " + Style.RESET_ALL)
    if response.lower() != 'y':
        break   
