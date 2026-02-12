# Copyright (c) 2026 Ville Heikkiniemi, Luka Hietala, Luukas Kola
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by Rina Poutiainen-Uekusa according to given task

"""
A program that prints reservation information according to requirements

The data structure and example data record:

reservationId | name | email | phone | reservationDate | reservationTime | durationHours | price | confirmed | reservedResource | createdAt
------------------------------------------------------------------------
201 | Moomin Valley | moomin@whitevalley.org | 0509876543 | 2025-11-12 | 09:00:00 | 2 | 18.50 | True | Forest Area 1 | 2025-08-12 14:33:20
int | str | str | str | date | time | int | float | bool | str | datetime

"""

from datetime import datetime


def convert_reservation_data(reservation: list[str]) -> dict:
    """
    Convert data types to meet program requirements
    """
    return {
        "reservationId": int(reservation[0]),  # reservationId (str -> int)
        "name": str(reservation[1]),  # name (str)
        "email": str(reservation[2]),  # email (str)
        "phone": str(reservation[3]),  # phone (str)
        "reservationDate": datetime.strptime(reservation[4], "%Y-%m-%d").date(),  # reservationDate (date)
        "reservationTime": datetime.strptime(reservation[5], "%H:%M").time(),  # reservationTime (time)
        "durationHours": int(reservation[6]),  # durationHours (int)
        "price": float(reservation[7]),  # price (float)
        "confirmed": True if reservation[8].strip() == 'True' else False,  # confirmed (bool)
        "reservedResource": str(reservation[9]),  # reservedResource (str)
        "createdAt": datetime.strptime(str(reservation[10]).strip(), "%Y-%m-%d %H:%M:%S"),  # createdAt (datetime)
    }


def fetch_reservations(reservation_file: str) -> list[dict]:
    """
    Reads reservations from a file and returns the reservations converted
    """
    reservations = []
    
    with open(reservation_file, "r", encoding="utf-8") as f:
        for line in f:
            if len(line) > 1:
                fields = line.split("|")
                reservations.append(convert_reservation_data(fields))
    return reservations


def confirmed_reservations(reservations: list[dict]) -> None:
    """
    Print confirmed reservations
    """
    for reservation in reservations:
        if reservation["confirmed"]:
            print(
                f'- {reservation["name"]}, {reservation["reservedResource"]}, '
                f'{reservation["reservationDate"].strftime("%d.%m.%Y")} at '
                f'{reservation["reservationTime"].strftime("%H.%M")}'
            )


def long_reservations(reservations : list[dict]) -> None:
    """
    Print long reservations

    Parameters:
     reservations (list[dict]): Reservations
    """
    for reservation in reservations:
        if reservation["durationHours"] >= 3:
            print(
                f'- {reservation["name"]}, '
                f'{reservation["reservationDate"].strftime("%d.%m.%Y")} at '
                f'{reservation["reservationTime"].strftime("%H.%M")}, '
                f'duration {reservation["durationHours"]} h, '
                f'{reservation["reservedResource"]}')


def confirmation_statuses(reservations: list[dict]) -> None:
    """
    Print confirmation statuses
    """
    for reservation in reservations:
        name: str = reservation["name"]
        confirmed: bool = reservation["confirmed"]
        print(f'{name} → {"Confirmed" if confirmed else "NOT Confirmed"}')


def confirmation_summary(reservations: list[dict]) -> None:
    """
    Print confirmation summary
    """
    confirmed: int = len([r for r in reservations if r["confirmed"]])
    print(f'- Confirmed reservations: {confirmed} pcs\n- Not confirmed reservations: {len(reservations) - confirmed} pcs')


def total_revenue(reservations: list[dict]) -> None:
    """
    Print total revenue
    """
    revenue: float = sum(r["durationHours"] * r["price"] for r in reservations if r["confirmed"])
    print(f'Total revenue from confirmed reservations: {revenue:.2f} €'.replace('.', ','))


def main():
    """
    Prints reservation information according to requirements
    """
    reservations = fetch_reservations("reservations.txt")
    print("1) Confirmed Reservations")
    confirmed_reservations(reservations)
    print("2) Long Reservations (≥ 3 h)")
    long_reservations(reservations)
    print("3) Reservation Confirmation Status")
    confirmation_statuses(reservations)
    print("4) Confirmation Summary")
    confirmation_summary(reservations)
    print("5) Total Revenue from Confirmed Reservations")
    total_revenue(reservations)


if __name__ == "__main__":
    main()
