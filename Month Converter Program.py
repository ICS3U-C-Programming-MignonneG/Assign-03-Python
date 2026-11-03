#!/usr/bin/env python3
# Created by: Mignonne Gihozo
# Created on: Oct 2026
# This program converts a number to match the month.


def main():
    try:
        # input
        month_number = int(input("Enter a number between 1 and 12: "))
        print("")

        # process & output
        months = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        }

        if 1 <= month_number <= 12:
            print(months[month_number])
        else:
            print("That is not a valid number")

    except ValueError:
        print("That is not a valid number")


if __name__ == "__main__":
    main()
