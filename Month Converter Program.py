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

        # process & output using pure decision structures
        if month_number == 1:
            print("January")
            print("Extra: The season for January is Winter.")
        elif month_number == 2:
            print("February")
            print("Extra: The season for February is Winter.")
        elif month_number == 3:
            print("March")
            print("Extra: The season for March is Spring.")
        elif month_number == 4:
            print("April")
            print("Extra: The season for April is Spring.")
        elif month_number == 5:
            print("May")
            print("Extra: The season for May is Spring.")
        elif month_number == 6:
            print("June")
            print("Extra: The season for June is Summer.")
        elif month_number == 7:
            print("July")
            print("Extra: The season for July is Summer.")
        elif month_number == 8:
            print("August")
            print("Extra: The season for August is Summer.")
        elif month_number == 9:
            print("September")
            print("Extra: The season for September is Fall.")
        elif month_number == 10:
            print("October")
            print("Extra: The season for October is Fall.")
        elif month_number == 11:
            print("November")
            print("Extra: The season for November is Fall.")
        elif month_number == 12:
            print("December")
            print("Extra: The season for December is Winter.")
        else:
            print("That is not a valid number")

    except ValueError:
        print("That is not a valid number")

    print("\nDone.")


if __name__ == "__main__":
    main()
