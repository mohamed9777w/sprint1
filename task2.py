#!/usr/bin/env python3

# function to check if a year is a leap year
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# loop to continuously ask the user to enter a year and check if it's a leap year
while True:
    try:
        year = int(input("Enter a year to check (or enter 0 to exit): ").strip())
        if year == 0:
            break
        elif year < 0:
            print("Invalid year entered. Year must be a positive integer.")
        elif is_leap(year):
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid year as a positive integer.")

