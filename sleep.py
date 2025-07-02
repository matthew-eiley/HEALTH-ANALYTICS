from datetime import datetime, timedelta
import pandas as pd

FILENAME = "data.csv"

df = pd.read_csv(FILENAME, usecols=["date", "hours_vs_needed", "sleep_consistency"],parse_dates=["date"])

def get_rGb(row, col):
    val = round((row[col] / 100) * 255)
    return (val, 255, val)

df["hours_vs_needed_rgb"] = df.apply(lambda row: get_rGb(row, "hours_vs_needed"), axis=1)
df["sleep_consistency_rgb"] = df.apply(lambda row: get_rGb(row, "sleep_consistency"), axis=1)

# grid[week][day] to access a specific cell (52 weeks, 7 days)
hours_vs_needed_grid = []
for week in range(52):
    hours_vs_needed_grid.append([])
    for day in range(7):
        hours_vs_needed_grid[week].append(None)
sleep_consistency_grid = []
for week in range(52):
    sleep_consistency_grid.append([])
    for day in range(7):
        sleep_consistency_grid[week].append(None)

def get_heatmap_start_date():
    today = datetime.today().date()
    return today - timedelta(days=364)

def get_week_and_day(date, start_date):
    days_since_start = (date - start_date).days
    if not 0 <= days_since_start < 364:  # outside the 52-week grid
        return None
    week = days_since_start // 7
    day = date.weekday()
    return week, day

def fill_grids():
    for _, row in df.iterrows():
        start_date = get_heatmap_start_date()
        date = row["date"]
        week, day = get_week_and_day(date, start_date)
        hours_vs_needed_grid[week][day] = row["hours_vs_needed_rgb"]
        sleep_consistency_grid[week][day] = row["sleep_consistency_rgb"]

print(hours_vs_needed_grid)
print(sleep_consistency_grid)