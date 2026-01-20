# Copyright (c) 2026 Ville Heikkiniemi, Luka Hietala, Luukas Kola
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by nnn according to given task

"""
A program that prints reservation information according to task requirements

The data structure and example data record:

reservationId | name | email | phone | reservationDate | reservationTime | durationHours | price | confirmed | reservedResource | createdAt
------------------------------------------------------------------------
201 | Moomin Valley | moomin@whitevalley.org | 0509876543 | 2025-11-12 | 09:00:00 | 2 | 18.50 | True | Forest Area 1 | 2025-08-12 14:33:20
int | str | str | str | date | time | int | float | bool | str | datetime

"""

from datetime import datetime

HEADERS = [
    "reservationId",
    "name",
    "email",
    "phone",
    "reservationDate",
    "reservationTime",
    "durationHours",
    "price",
    "confirmed",
    "reservedResource",
    "createdAt",
]


def convert_reservation_data(reservation: list) -> list:
    """
    Convert data types to meet program requirements

    Parameters:
     reservation (list): Unconverted reservation -> 11 columns

    Returns:
     converted (list): Converted data types
    """
    converted = []
    # Convert the first element = reservation[0]
    converted.append(int(reservation[0]))  # reservationId (str -> int)
    # And continue from here
    converted.append("")  # name (str)
    converted.append("")  # email (str)
    converted.append("")  # phone (str)
    converted.append("")  # reservationDate (date)
    converted.append("")  # reservationTime (time)
    converted.append("")  # durationHours (int)
    converted.append("")  # price (float)
    converted.append("")  # confirmed (bool)
    converted.append("")  # reservedResource (str)
    converted.append("")  # createdAt (datetime)
    return converted


def fetch_reservations(reservation_file: str) -> list:
    """
    Reads reservations from a file and returns the reservations converted
    You don't need to modify this function!

    Parameters:
     reservation_file (str): Name of the file containing the reservations

    Returns:
     reservations (list): Read and converted reservations
    """
    reservations = []
    with open(reservation_file, "r", encoding="utf-8") as f:
        for line in f:
            fields = line.split("|")
            reservations.append(convert_reservation_data(fields))
    return reservations


def confirmed_reservations(reservations: list[list]) -> None:
    """
    Print confirmed reservations

    Parameters:
     reservations (list): Reservations
    """
    print("")


def long_reservations(reservations: list[list]) -> None:
    """
    Print long reservations

    Parameters:
     reservations (list): Reservations
    """
    print("")


def confirmation_statuses(reservations: list[list]) -> None:
    """
    Print confirmation statuses

    Parameters:
     reservations (list): Reservations
    """
    print("")


def confirmation_summary(reservations: list[list]) -> None:
    """
    Print confirmation summary

    Parameters:
     reservations (list): Reservations
    """
    print("")


def total_revenue(reservations: list[list]) -> None:
    """
    Print total revenue

    Parameters:
     reservations (list): Reservations
    """
    print("")


def main():
    """
    Prints reservation information according to requirements
    Reservation-specific printing is done in functions
    """
    reservations = fetch_reservations("reservations.txt")
    # PART A -> Before continuing to part B, make sure that the following lines
    # print all the reservation data and the correct data types to the console. 
    # After that, you can remove this section or comment it out up to part B.
    print(" | ".join(HEADERS))
    print("------------------------------------------------------------------------")
    for reservation in reservations:
        print(" | ".join(str(x) for x in reservation))
        data_types = [type(x).__name__ for x in reservation]
        print(" | ".join(data_types))
        print(
            "------------------------------------------------------------------------"
        )

    # PART B -> Build the output required in part B from this using
    # the predefined functions and the necessary print statements.

    # print("1) Confirmed Reservations")
    # confirmed_reservations(reservations)
    # Continue from here


if __name__ == "__main__":
    main()
