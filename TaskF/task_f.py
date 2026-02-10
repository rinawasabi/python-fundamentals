# Copyright (c) 2026 Rina Poutiainen-Uekusa
# License: MIT

import csv
from datetime import datetime, date

def read_data(filename: str) -> list[list[str]]:
    """Reads a CSV file and returns the rows in a suitable structure."""
    rows = []
    with open(filename, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            rows.append(row)
    return rows

def show_main_menu() -> str:
    """Prints the main menu and returns the user selection as a string."""
    print("Choose a report type:")
    print("1) Daily summary for a date range")
    print("2) Monthly summary for one month")
    print("3) Full year 2025 summary")
    print("4) Exit the program")
    return input("Your choice: ").strip()

def show_after_main_menu() -> str:
    """Prints the after-report menu and returns the user selection as a string."""
    print("What would you like to do next?")
    print("1) Write the report to the file report.txt")
    print("2) Create a new report")
    print("3) Exit")
    return input("Your choice: ").strip()

def parse_fi_date(s: str) -> date:
    """Parses a date string in dd.mm.yyyy format into a date object."""
    return datetime.strptime(s.strip(), "%d.%m.%Y").date()

def format_fi_date(d: date) -> str:
    """Formats a date object as dd.mm.yyyy."""
    return d.strftime("%d.%m.%Y")

def format_comma(value: float) -> str:
    """Formats number with 2 decimals and comma as decimal separator."""
    return f"{value:.2f}".replace(".", ",")

def calculate_daily_totals(rows: list[list[str]]) -> dict[date, list[float]]:
    """Calculates daily totals for consumption, production, and temperature."""
    daily: dict[date, list[float]] = {}
    for row in rows[1:]:
        dt = datetime.fromisoformat(row[0].strip())
        d = dt.date()

        cons = float(row[1].strip().replace(",", "."))
        prod = float(row[2].strip().replace(",", "."))
        temp = float(row[3].strip().replace(",", "."))

        if d not in daily:
            daily[d] = [0.0, 0.0, 0.0, 0.0]  # cons, prod, temp_sum, temp_count
        
        daily[d][0] += cons
        daily[d][1] += prod
        daily[d][2] += temp
        daily[d][3] += 1.0

    return daily

def create_daily_report(daily: dict[date, list[float]]) -> list[str]:
    """Creates a daily report for a selected date range."""
    start_s = input("Enter start date (dd.mm.yyyy): ").strip()
    end_s = input("Enter end date (dd.mm.yyyy): ").strip()

    start_d = parse_fi_date(start_s)
    end_d = parse_fi_date(end_s)

    if end_d < start_d:
        start_d, end_d = end_d, start_d

    cons_sum = 0.0
    prod_sum = 0.0
    temp_sum = 0.0
    temp_count = 0.0

    for d in daily:
        if start_d <= d <= end_d:
            cons_sum += daily[d][0]
            prod_sum += daily[d][1]
            temp_sum += daily[d][2]
            temp_count += daily[d][3]

    avg_temp = (temp_sum / temp_count) if temp_count > 0 else 0.0

    lines: list[str] = []
    lines.append("-" * 53)
    lines.append(f"Report for the period {format_fi_date(start_d)}-{format_fi_date(end_d)}")
    lines.append(f"- Total consumption: {format_comma(cons_sum)} kWh")
    lines.append(f"- Total production: {format_comma(prod_sum)} kWh")
    lines.append(f"- Average temperature: {format_comma(avg_temp)} °C")
    return lines

def create_monthly_report(daily: dict[date, list[float]]) -> list[str]:
    """Creates a monthly summary report for a selected month."""
    month = int(input("Enter month number (1-12): ").strip())

    cons_sum = 0.0
    prod_sum = 0.0
    daily_avg_temp_sum = 0.0
    days_count = 0

    for d in daily:
        if d.year == 2025 and d.month == month:
            cons_sum += daily[d][0]
            prod_sum += daily[d][1]

            # daily average temperature based on hourly values
            t_count = daily[d][3]
            day_avg = (daily[d][2] / t_count) if t_count > 0 else 0.0
            daily_avg_temp_sum += day_avg
            days_count += 1

    avg_temp = (daily_avg_temp_sum / days_count) if days_count > 0 else 0.0

    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    lines: list[str] = []
    lines.append("-" * 53)
    lines.append(f"Report for the month: {month_names[month - 1]}")
    lines.append(f"- Total consumption: {format_comma(cons_sum)} kWh")
    lines.append(f"- Total production: {format_comma(prod_sum)} kWh")
    lines.append(f"- Average temperature: {format_comma(avg_temp)} °C")
    return lines

def create_yearly_report(daily: dict[date, list[float]]) -> list[str]:
    """Creates a full-year summary report."""
    cons_sum = 0.0
    prod_sum = 0.0
    temp_sum = 0.0
    temp_count = 0.0

    for d in daily:
        if d.year == 2025:
            cons_sum += daily[d][0]
            prod_sum += daily[d][1]
            temp_sum += daily[d][2]
            temp_count += daily[d][3]

    avg_temp = (temp_sum / temp_count) if temp_count > 0 else 0.0

    lines: list[str] = []
    lines.append("Report for the year: 2025")
    lines.append(f"- Total consumption: {format_comma(cons_sum)} kWh")
    lines.append(f"- Total production: {format_comma(prod_sum)} kWh")
    lines.append(f"- Average temperature: {format_comma(avg_temp)} °C")
    return lines

def print_report_to_console(lines: list[str]) -> None:
    """Prints report lines to the console."""
    for line in lines:
        print(line)

def write_report_to_file(lines: list[str]) -> None:
    """Writes report lines to the file report.txt."""
    with open("report.txt", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def main() -> None:
    """Main function: reads data, shows menus, and controls report generation."""
    rows = read_data("2025.csv")
    daily = calculate_daily_totals(rows)

    last_report: list[str] = []

    while True:
        print()
        choice = show_main_menu()

        if choice == "1":
            last_report = create_daily_report(daily)
            print_report_to_console(last_report)

        elif choice == "2":
            last_report = create_monthly_report(daily)
            print_report_to_console(last_report)

        elif choice == "3":
            last_report = create_yearly_report(daily)
            print_report_to_console(last_report)

        elif choice == "4":
            break

        else:
            print("Invalid selection. Please choose 1-4.")
            continue

        while True:
            after = show_after_main_menu()
            if after == "1":
                write_report_to_file(last_report)
                print("Saved to report.txt.")
            elif after == "2":
                break
            elif after == "3":
                return
            else:
                print("Invalid selection. Please choose 1-3.")

if __name__ == "__main__":
    main()
