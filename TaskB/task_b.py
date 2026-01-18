# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by Rina Poutiainen-Uekusa according to given task

"""
A program that reads reservation data from a file
and prints them to the console using functions:

Reservation number: 123
Booker: Anna Virtanen
Date: 31.10.2025
Start time: 10.00
Number of hours: 2
Hourly rate: 19,95 €
Total price: 39,90 €
Paid: Yes
Venue: Meeting Room A
Phone: 0401234567
Email: anna.virtanen@example.com

"""
from datetime import datetime

def print_reservation_number(reservation: list) -> None:
    """
    Prints the reservation number

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    reservation_number = int(reservation[0])
    print(f"Reservation number: {reservation_number}")

def print_booker(reservation: list) -> None:
    """
    Prints the booker
    """
    booker = reservation[1]
    print(f"Booker: {booker}")
    
def print_date(reservation: list) -> None:
    """
    Prints the date
    """
    day = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    finnish_day = day.strftime("%d.%m.%Y")
    print(f"Date: {finnish_day}")

def print_start_time(reservation: list) -> None:
    """
    Prints the start time
    """
    time = datetime.strptime(reservation[3], "%H:%M").time()
    finnish_time = time.strftime("%H.%M")
    print(f"Start time: {finnish_time}")

def print_hours(reservation: list) -> None: 
    """
    Prints the number of hours
    """
    hours = int(reservation[4])
    print(f"Number of hours: {hours}")
    
def print_hourly_rate(reservation: list) -> None:
    """
    Prints the hourly rate
    """
    hourly_rate = float(reservation[5])
    hourly_rate_str = f"{hourly_rate:.2f}".replace('.', ',')
    print(f"Hourly rate: {hourly_rate_str} €")

def print_total_price(reservation: list) -> None:
    """
    Prints the total price
    """
    hours = int(reservation[4])
    hourly_rate = float(reservation[5])
    total_price = hours * hourly_rate
    total_price_str = f"{total_price:.2f}".replace('.', ',')
    print(f"Total price: {total_price_str} €")

def print_paid(reservation: list) -> None:
    """
    Prints whether the reservation is paid
    """
    paid = bool(reservation[6])
    print(f"Paid: {'Yes' if paid else 'No'}")

def print_venue(reservation: list) -> None:
    """
    Prints the venue
    """
    venue = reservation[7]
    print(f"Venue: {venue}")

def print_phone(reservation: list) -> None:
    """
    Prints the phone number
    """
    phone = reservation[8]
    print(f"Phone: {phone}")

def print_email(reservation: list) -> None:
    """
    Prints the email
    """
    email = reservation[9]
    print(f"Email: {email}")


def main():
    """
    Reads reservation data from a file and
    prints them to the console using functions
    """
    # Define the file name directly in the code
    reservations = "reservations.txt"

    # Open the file, read it, and split the contents
    with open(reservations, "r", encoding="utf-8") as f:
        reservation = f.read().strip()
        reservation = reservation.split('|')


    print_reservation_number(reservation)
    print_booker(reservation)
    print_date(reservation)
    print_start_time(reservation)
    print_hours(reservation)
    print_hourly_rate(reservation)
    print_total_price(reservation)
    print_paid(reservation)
    print_venue(reservation)
    print_phone(reservation)
    print_email(reservation)

if __name__ == "__main__":
    main()
