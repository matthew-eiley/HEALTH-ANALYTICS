from datetime import datetime
import pandas as pd
import os

FILENAME = "data.csv"

def get_date():
    date = input("Input the date for which you are entering values.\nIf you just want to use today's date, press enter.\nIf you want to use a different date, enter it in the form mm/dd/yyyy:\n")
    if date == "":
        today = datetime.today()
        date = datetime(month=today.month, day=today.day, year=today.year)
    else:
        specs = date.split("/")
        date = datetime(month=int(specs[0]), day=int(specs[1]), year=int(specs[2]))
    return date

def get_float_input(prompt):
    return float(input("\n" + prompt + ":\n"))

def get_and_store_data():
    entry = {
        "date": get_date(),
        "hours_vs_needed": get_float_input("Sleep vs needed (%)"),
        "sleep_consistency": get_float_input("Sleep consistency (%)"),
        "recovery": get_float_input("Recovery (%)"),
        "strain": get_float_input("Strain"),
        "hrv": get_float_input("Heart Rate Variability (ms)")
    }

    if os.path.exists(FILENAME):
        df = pd.read_csv(FILENAME, parse_dates=["date"])
    else:
        df = pd.DataFrame(columns=entry.keys())
    df = df[df["date"] != pd.to_datetime(entry["date"])]
    df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    df.sort_values("date", inplace=True)
    df.to_csv(FILENAME, index=False)
    print("\nEntry saved.")

def main():
    get_and_store_data()

main()