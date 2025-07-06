from datetime import datetime
import pandas as pd
import os
import heat_maps

FILENAME = "data.csv"
TODAY = datetime.today()

def get_date():
    date = input("Input the date for which you are entering values.\nIf you just want to use today's date, press enter.\nIf you want to use a different date, enter it in the form mm/dd/yyyy:\n")
    if date == "":
        date = datetime(month=TODAY.month, day=TODAY.day, year=TODAY.year)
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

def get_basic_stats():    
    df = pd.read_csv(FILENAME, parse_dates=["date"])
    stats = {
        'total_days': len(df),
        'last_updated': df.iloc[len(df)-1]["date"],
        'avg_hours_vs_needed': df.tail(7)["hours_vs_needed"].mean(),
        'avg_sleep_consistency': df.tail(7)["sleep_consistency"].mean(),
        'avg_recovery': df.tail(7)["recovery"].mean(),
        'avg_strain': pd.to_numeric(df.tail(7)["strain"], errors='coerce').mean(),
        'avg_hrv': df.tail(7)["hrv"].mean()
    }
    return stats

def get_prev_stats():
    df = pd.read_csv(FILENAME, parse_dates=["date"])
    prev = {
        'avg_hours_vs_needed': df.iloc[-14:-7]["hours_vs_needed"].mean(),
        'avg_sleep_consistency': df.iloc[-14:-7]["sleep_consistency"].mean(),
        'avg_recovery': df.iloc[-14:-7]["recovery"].mean(),
        'avg_strain': pd.to_numeric(df.iloc[-14:-7]["strain"], errors='coerce').mean(),
        'avg_hrv': df.iloc[-14:-7]["hrv"].mean()
    }
    return prev

def get_stats_deltas():    
    stats = get_basic_stats()
    prev = get_prev_stats()
    deltas = {
        'avg_hours_vs_needed': round(stats['avg_hours_vs_needed']-prev['avg_hours_vs_needed'], 1),
        'avg_sleep_consistency': round(stats['avg_sleep_consistency']-prev['avg_sleep_consistency'], 1),
        'avg_recovery': round(stats['avg_recovery']-prev['avg_recovery'], 1),
        'avg_strain': round(stats['avg_strain']-prev['avg_strain'], 1),
        'avg_hrv': round(stats['avg_hrv']-prev['avg_hrv'], 1)
    }
    return deltas


def get_recent_data(days=7):
    """Get recent data for insights"""
    if not os.path.exists(FILENAME):
        return None
    
    df = pd.read_csv(FILENAME, parse_dates=["date"])
    df_sorted = df.sort_values('date', ascending=False)
    return df_sorted.head(days)

def main():
    get_and_store_data()
    heat_maps.fill_grids()

if __name__ == "__main__":
    main()
