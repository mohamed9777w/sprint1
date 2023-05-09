#!/usr/bin/env python3

# import colorama library to use colored output
import colorama
from colorama import Fore, Style

# initialize colorama
colorama.init()

def isBalanced(balancedBrackets):
    # create stack to keep track of open brackets
    stack = []
    # loop through the brackets in the input string
    i = 0
    while i < len(balancedBrackets):
        bracket = balancedBrackets[i]
        # if the bracket is an opening bracket, push it onto the stack
        if bracket in ['(', '[', '{']:
            stack.append(bracket)
        else:
            # if the stack is empty or the last open bracket doesn't match the current closing bracket, return NO
            if not stack:
                return Fore.RED + "NO" + Style.RESET_ALL
            if bracket == ')' and stack[-1] == '(':
                stack.pop()
            elif bracket == ']' and stack[-1] == '[':
                stack.pop()
            elif bracket == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return Fore.RED + "NO" + Style.RESET_ALL
        i += 1
    # if the stack is not empty, return NO
    if stack:
        return Fore.RED + "NO" + Style.RESET_ALL
    # otherwise, the brackets are balanced
    return Fore.GREEN + "YES" + Style.RESET_ALL

while True:
    text = input("Please enter a string of brackets to check for balance: ")
    result = isBalanced(text)
    print(result)

    choice = input("Would you like to enter another string? (y/n): ")
    if choice.lower() != "y":
        break

print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)

