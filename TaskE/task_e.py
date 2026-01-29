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


def daily_totals(rows: list[list[str]]) -> dict:
    """Returns daily totals."""
    daily = {}

    for row in rows[1:]:
        dt = datetime.fromisoformat(row[0])
        d = dt.date()

        if d not in daily:
            daily[d] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # cons1-3, prod1-3 (Wh)

        daily[d][0] += float(row[1])
        daily[d][1] += float(row[2])
        daily[d][2] += float(row[3])
        daily[d][3] += float(row[4])
        daily[d][4] += float(row[5])
        daily[d][5] += float(row[6])

    return daily

def week_section(week_no: int, daily: dict) -> str:
    """Builds the weekly electricity consumption and production report section as text."""

    lines: list[str] = []

    lines.append(f"Week {week_no} electricity consumption and production (kWh, by phase)")
    lines.append("Day          Date        Consumption [kWh]               Production [kWh]")
    lines.append("            (dd.mm.yyyy)  v1      v2      v3             v1     v2     v3")
    lines.append("-" * 75)

    for d in sorted(daily.keys()):
        cons1 = format_comma(wh_to_kwh(daily[d][0]))
        cons2 = format_comma(wh_to_kwh(daily[d][1]))
        cons3 = format_comma(wh_to_kwh(daily[d][2]))
        prod1 = format_comma(wh_to_kwh(daily[d][3]))
        prod2 = format_comma(wh_to_kwh(daily[d][4]))
        prod3 = format_comma(wh_to_kwh(daily[d][5]))

        weekday = finDays[d.weekday()]
        date_str = d.strftime("%d.%m.%Y")

        lines.append(
            f"{weekday:<12} {date_str:<12} "
            f"{cons1:>7} {cons2:>7} {cons3:>7}   "
            f"{prod1:>7} {prod2:>7} {prod3:>7}"
        )
    lines.append("")
    return "\n".join(lines)

def write_report(filename: str, text: str) -> None:
    """Writes the report text to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def main() -> None:
    """Main function: reads data of 3 weeks and writes the summary report."""

    weeks = [
        (41, "week41.csv"),
        (42, "week42.csv"),
        (43, "week43.csv"),
    ]

    parts: list[str] = []
    for week_no, filename in weeks:
        rows = read_data(filename)
        daily = daily_totals(rows)
        parts.append(week_section(week_no, daily))

    report = "\n".join(parts)
    write_report("summary.txt", report)


if __name__ == "__main__":
    main()

