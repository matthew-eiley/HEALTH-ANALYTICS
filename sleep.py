from datetime import datetime
import pandas as pd

FILENAME = "data.csv"

df = pd.read_csv(FILENAME, usecols=["date", "hours_vs_needed", "sleep_consistency"],parse_dates=["date"])

def get_rGb(row, col):
    val = round((row[col] / 100) * 255)
    return (val, 255, val)

df["hours_vs_needed_rgb"] = df.apply(lambda row: get_rGb(row, "hours_vs_needed"), axis=1)
df["sleep_consistency_rgb"] = df.apply(lambda row: get_rGb(row, "sleep_consistency"), axis=1)

print(df)

# grid[week][day] to access a specific cell (52 weeks, 7 days)
grid = []
for week in range(52):
    grid.append([])
    for day in range(7):
        grid[week].append(None)

def get_week_and_day(date):
    # find day
    day = date.isocalendar().weekday - 1 # monday=0 , sunday=7
    # find week
    today = datetime.today()
    today_week_number = today.isocalendar().week
    date_week_number = date.isocalendar().week
    if today.year == date.year:
        week_number = 52 - (today_week_number - date_week_number)
    else:
        week_number = 52 - ((today_week_number + 52) - date_week_number)
    print(week_number)

