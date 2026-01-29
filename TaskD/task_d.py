# Copyright (c) 2026 Rina Poutiainen-Uekusa
# License: MIT

import csv
from datetime import datetime

finDays = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]


def read_data(filename: str) -> list[list[str]]:
    """Reads the CSV file and returns all rows."""
    rows = []
    with open(filename, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            rows.append(row)
    return rows


def wh_to_kwh(wh: float) -> float:
    """Converts Wh to kWh."""
    return wh / 1000.0


def format_comma(value: float) -> str:
    """Formats number with 2 decimals and comma as decimal separator."""
    return f"{value:.2f}".replace(".", ",")


def main() -> None:
    """Main function: reads data, computes daily totals, and prints the report."""
    data = read_data("week42.csv")
    daily = {}

    print("Week 42 electricity consumption and production (kWh, by phase)\n")
    print("Day          Date        Consumption [kWh]               Production [kWh]")
    print("            (dd.mm.yyyy)  v1      v2      v3             v1     v2     v3")
    print("-" * 75)

    for row in data[1:]:
        dt = datetime.fromisoformat(row[0])
        d = dt.date()

        if d not in daily:
            daily[d] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # For both cons v1-3, prod v1-3

        # consumption (Wh)
        daily[d][0] += float(row[1])
        daily[d][1] += float(row[2])
        daily[d][2] += float(row[3])

        # production (Wh)
        daily[d][3] += float(row[4])
        daily[d][4] += float(row[5])
        daily[d][5] += float(row[6])

    for d in sorted(daily.keys()):
        cons1 = format_comma(wh_to_kwh(daily[d][0]))
        cons2 = format_comma(wh_to_kwh(daily[d][1]))
        cons3 = format_comma(wh_to_kwh(daily[d][2]))
        prod1 = format_comma(wh_to_kwh(daily[d][3]))
        prod2 = format_comma(wh_to_kwh(daily[d][4]))
        prod3 = format_comma(wh_to_kwh(daily[d][5]))

        weekday = finDays[d.weekday()]
        date_str = d.strftime("%d.%m.%Y")

        print(
            f"{weekday:<12} {date_str:<12} "
            f"{cons1:>7} {cons2:>7} {cons3:>7}   "
            f"{prod1:>7} {prod2:>7} {prod3:>7}"
        )


if __name__ == "__main__":
    main()
