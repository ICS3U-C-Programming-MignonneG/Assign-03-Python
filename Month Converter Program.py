#!/usr/bin/env python3

# Created by: Mignonne Gihozo
# Created on: Oct 2026
# This program converts a number to match the month
# and includes the corresponding season as extra functionality.


def main():
    # Initial greeting
    print("Welcome to Mignonne’s Month Converter program!")

    try:
        # input
        month_number = int(input("Enter a number between 1 and 12: "))
        print("")

        # process & output
        months = {
            1: ("January", "Winter"),
            2: ("February", "Winter"),
            3: ("March", "Spring"),
            4: ("April", "Spring"),
            5: ("May", "Spring"),
            6: ("June", "Summer"),
            7: ("July", "Summer"),
            8: ("August", "Summer"),
            9: ("September", "Fall"),
            10: ("October", "Fall"),
            11: ("November", "Fall"),
            12: ("December", "Winter"),
        }

        if 1 <= month_number <= 12:
            month_name, season = months[month_number]
            print(month_name)
            print(f"Extra: The season for {month_name} is {season}.")
        else:
            print("That is not a valid number")

    except ValueError:
        print("That is not a valid number")

    print("\nDone.")


if __name__ == "__main__":
    main()
