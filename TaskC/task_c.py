# Copyright (c) 2026 Ville Heikkiniemi, Luka Hietala, Luukas Kola
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by Rina Poutiainen-Uekusa according to given task

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

    converted.append(int(reservation[0]))  # reservationId (str -> int)
    converted.append(reservation[1])  # name (str)
    converted.append(reservation[2])  # email (str)
    converted.append(reservation[3])  # phone (str)
    converted.append(datetime.strptime(reservation[4], "%Y-%m-%d").date()) # reservationDate (date)
    converted.append(datetime.strptime(reservation[5], "%H:%M").time())  # reservationTime (time)
    converted.append(int(reservation[6]))  # durationHours (int)
    converted.append(float(reservation[7]))  # price (float)
    converted.append(reservation[8].strip() == "True")  # confirmed (bool)
    converted.append(reservation[9])  # reservedResource (str)
    converted.append(datetime.strptime(reservation[10].strip(), "%Y-%m-%d %H:%M:%S"))  # createdAt (datetime)
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
    for reservation in reservations:
        if reservation[8]: 
            date_str = reservation[4].strftime("%d.%m.%Y")
            time_str = reservation[5].strftime("%H.%M")
            print(f"- {reservation[1]}, {reservation[9]}, {date_str} at {time_str}")


def long_reservations(reservations: list[list]) -> None:
    """
    Print long reservations

    Parameters:
     reservations (list): Reservations
    """
    for reservation in reservations:
        if reservation[6] >= 3:  
            date_str = reservation[4].strftime("%d.%m.%Y")
            time_str = reservation[5].strftime("%H.%M")
            print(f"- {reservation[1]}, {date_str} at {time_str}, duration {reservation[6]} h, {reservation[9]}")


def confirmation_statuses(reservations: list[list]) -> None:
    """
    Print confirmation statuses

    Parameters:
     reservations (list): Reservations
    """
    for reservation in reservations:
        status = "Confirmed" if reservation[8] else "NOT Confirmed"
        print(f"{reservation[1]} → {status}")



def confirmation_summary(reservations: list[list]) -> None:
    """
    Print confirmation summary

    Parameters:
     reservations (list): Reservations
    """
    count = 0
    not_count = 0
    for reservation in reservations:
        if reservation[8]:
            count += 1
        else:
            not_count += 1
    print(f"- Confirmed reservations: {count} pcs")
    print(f"- Not confirmed reservations: {not_count} pcs")


def total_revenue(reservations: list[list]) -> None:
    """
    Print total revenue

    Parameters:
     reservations (list): Reservations
    """
    total = 0.0
    for reservation in reservations:
        if reservation[8]:  
            total += reservation[6] * reservation[7]
    
    amount_str = f"{total:.2f}".replace(".", ",")
    print(f"Total revenue from confirmed reservations: {amount_str} €")


def main():
    """
    Prints reservation information according to requirements
    Reservation-specific printing is done in functions
    """
    reservations = fetch_reservations("reservations.txt")

    print("1) Confirmed Reservations")
    confirmed_reservations(reservations)
    print()

    print("2) Long Reservations (≥ 3 h)")
    long_reservations(reservations)
    print()

    print("3) Reservation Confirmation Status")
    confirmation_statuses(reservations)
    print()

    print("4) Confirmation Summary")
    confirmation_summary(reservations)
    print()

    print("5) Total Revenue from Confirmed Reservations")
    total_revenue(reservations)
    print()

if __name__ == "__main__":
    main()
