import pandas as pd

FILENAME = "data.csv"

df = pd.read_csv(FILENAME, usecols=["date", "hours_vs_needed", "sleep_consistency"],parse_dates=["date"])

def get_rGb(row, col):
    val = round((row[col] / 100) * 255)
    return (val, 255, val)

df["hours_vs_needed_rgb"] = df.apply(lambda row: get_rGb(row, "hours_vs_needed"), axis=1)
df["sleep_consistency_rgb"] = df.apply(lambda row: get_rGb(row, "sleep_consistency"), axis=1)

print(df)

