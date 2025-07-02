from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

# =================================================================================================
# -------------------------------------- CREATING DATAFRAME ---------------------------------------
# =================================================================================================
FILENAME = "data.csv"

df = pd.read_csv(FILENAME, usecols=["date", "hours_vs_needed", "sleep_consistency"],parse_dates=["date"])

def get_hours_vs_needed_rGb(row):
    if row["hours_vs_needed"] >= 92.5:
        return (0.180, 0.380, 0.188)
    elif row["hours_vs_needed"] >= 85:
        return (0.325, 0.635, 0.345)
    elif row["hours_vs_needed"] >= 77.5:
        return (0.427, 0.749, 0.455)
    elif row["hours_vs_needed"] >= 70:
        return (0.729, 0.925, 0.749)
    else:
        return (0.941, 0.949, 0.961)
    
def get_sleep_consistency_rGb(row):
    if row["sleep_consistency"] >= 90:
        return (0.180, 0.380, 0.188)
    elif row["sleep_consistency"] >= 80:
        return (0.325, 0.635, 0.345)
    elif row["sleep_consistency"] >= 70:
        return (0.427, 0.749, 0.455)
    elif row["sleep_consistency"] >= 60:
        return (0.729, 0.925, 0.749)
    else:
        return (0.941, 0.949, 0.961)

df["hours_vs_needed_rgb"] = df.apply(lambda row: get_hours_vs_needed_rGb(row), axis=1)
df["sleep_consistency_rgb"] = df.apply(lambda row: get_sleep_consistency_rGb(row), axis=1)

# =================================================================================================
# ---------------------------------------- CREATING GRIDS -----------------------------------------
# =================================================================================================

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
    # Go to Monday of this week
    this_monday = today - timedelta(days=today.weekday())  # Monday=0
    # Go back 51 full weeks
    return this_monday - timedelta(weeks=51)

def get_week_and_day(date, start_date):
    days_since_start = (date - start_date).days
    if not 0 <= days_since_start < 364:  # Exactly 52 weeks
        return None
    week = days_since_start // 7
    day = date.weekday()  # Monday = 0 , Sunday = 6
    return week, day

def fill_grids():
    start_date = get_heatmap_start_date()
    for _, row in df.iterrows():
        date = row["date"].date()
        week, day = get_week_and_day(date, start_date)
        hours_vs_needed_grid[week][day] = row["hours_vs_needed_rgb"]
        sleep_consistency_grid[week][day] = row["sleep_consistency_rgb"]

fill_grids()
print(hours_vs_needed_grid)
print(sleep_consistency_grid)

# =================================================================================================
# ---------------------------------------- CREATING PLOTS -----------------------------------------
# =================================================================================================

def plot_rgb_grid(grid, title):
    fig, ax = plt.subplots()  # Wider = more GitHub-like

    # Loop over each cell
    for week in range(52):
        for day in range(7):
            color = grid[week][day]
            if color is None:
                color = (0.941, 0.949, 0.961)
            rect = plt.Rectangle((week, 6 - day), 1, 1, color=color)  # flip Y axis: Monday at top
            ax.add_patch(rect)

    ax.set_xlim(0, 52)
    ax.set_ylim(0, 7)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.title(title, fontsize=14, pad=10)
    plt.tight_layout()
    plt.show()

plot_rgb_grid(hours_vs_needed_grid, "Hours vs Needed")
plot_rgb_grid(sleep_consistency_grid, "Sleep Consistency")
