from datetime import datetime, timedelta
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

FILENAME = "data.csv"

def load_data():
    try:
        if not os.path.exists(FILENAME):
            print(f"Warning: {FILENAME} not found. Please run main.py to create data first.")
            return None
        
        df = pd.read_csv(FILENAME, usecols=["date", "hours_vs_needed", "sleep_consistency", "recovery", "strain"], parse_dates=["date"])
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def get_hours_vs_needed_rgb(row):
    value = row["hours_vs_needed"]
    if pd.isna(value):
        return (0.235, 0.235, 0.235)  # Dark gray for missing data
    elif value >= 92.5:
        return (0.180, 0.380, 0.188)  # Darker green
    elif value >= 85:
        return (0.325, 0.635, 0.345)  # Dark green
    elif value >= 77.5:
        return (0.427, 0.749, 0.455)  # Medium green
    elif value >= 70:
        return (0.729, 0.925, 0.749)  # Light green
    else:
        return (0.941, 0.949, 0.961)  # Light gray

def get_sleep_consistency_rgb(row):
    value = row["sleep_consistency"]
    if pd.isna(value):
        return (0.235, 0.235, 0.235)  # Dark gray for missing data
    elif value >= 90:
        return (0.180, 0.380, 0.188)  # Dark green
    elif value >= 80:
        return (0.325, 0.635, 0.345)  # Dark green
    elif value >= 70:
        return (0.427, 0.749, 0.455)  # Medium green
    elif value >= 60:
        return (0.729, 0.925, 0.749)  # Light green
    else:
        return (0.941, 0.949, 0.961)  # Light gray

def get_recovery_rgb(row):
    value = row["recovery"]
    if pd.isna(value):
        return (0.235, 0.235, 0.235)  # Dark gray for missing data
    elif value >= 87.5:
        return (0.180, 0.380, 0.188)  # Darker green
    elif value >= 75:
        return (0.325, 0.635, 0.345)  # Dark green
    elif value >= 62.5:
        return (0.427, 0.749, 0.455)  # Medium green
    elif value >= 50:
        return (0.729, 0.925, 0.749)  # Light green
    else:
        return (0.941, 0.949, 0.961)  # Light gray

def get_strain_rgb(row):
    value = row["strain"]
    if pd.isna(value):
        return (0.235, 0.235, 0.235)  # Dark gray for missing data
    elif value >= 17.5:
        return (0.180, 0.380, 0.188)  # Darker green
    elif value >= 14:
        return (0.325, 0.635, 0.345)  # Dark green
    elif value >= 10.5:
        return (0.427, 0.749, 0.455)  # Medium green
    elif value >= 7:
        return (0.729, 0.925, 0.749)  # Light green
    else:
        return (0.941, 0.949, 0.961)  # Light gray

def get_heatmap_start_date():
    """
    Get the start date for the heatmap (52 weeks ago from this Monday)
    """
    today = datetime.today().date()
    # Go to Monday of this week
    this_monday = today - timedelta(days=today.weekday())  # Monday=0
    # Go back 51 full weeks
    return this_monday - timedelta(weeks=51)

def get_week_and_day(date, start_date):
    """
    Get week and day indices for a given date
    """
    days_since_start = (date - start_date).days
    if not 0 <= days_since_start < 364:  # Exactly 52 weeks
        return None, None
    week = days_since_start // 7
    day = date.weekday()  # Monday = 0, Sunday = 6
    return week, day

def fill_grids():
    """
    Create and fill the heatmap grids
    """
    df = load_data()
    if df is None:
        return None, None
    
    # Add RGB columns
    df["hours_vs_needed_rgb"] = df.apply(lambda row: get_hours_vs_needed_rgb(row), axis=1)
    df["sleep_consistency_rgb"] = df.apply(lambda row: get_sleep_consistency_rgb(row), axis=1)
    df["recovery_rgb"] = df.apply(lambda row: get_recovery_rgb(row), axis=1)
    df["strain_rgb"] = df.apply(lambda row: get_strain_rgb(row), axis=1)

    # Initialize grids (52 weeks, 7 days)
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

    recovery_grid = []
    for week in range(52):
        recovery_grid.append([])
        for day in range(7):
            recovery_grid[week].append(None)

    strain_grid = []
    for week in range(52):
        strain_grid.append([])
        for day in range(7):
            strain_grid[week].append(None)

    
    start_date = get_heatmap_start_date()
    
    for _, row in df.iterrows():
        date = row["date"].date()
        week, day = get_week_and_day(date, start_date)
        
        if week is not None and day is not None:
            hours_vs_needed_grid[week][day] = [date, row["hours_vs_needed_rgb"]]
            sleep_consistency_grid[week][day] = [date, row["sleep_consistency_rgb"]]
            recovery_grid[week][day] = [date, row["recovery_rgb"]]
            strain_grid[week][day] = [date, row["strain_rgb"]]

    # make rest of this week white
    for i in range(7):
        if hours_vs_needed_grid[51][i] is None:
            hours_vs_needed_grid[51][i] = [[], (1, 1, 1)]
    for i in range(7):
        if sleep_consistency_grid[51][i] is None:
            sleep_consistency_grid[51][i] = [[], (1, 1, 1)]
    for i in range(7):
        if recovery_grid[51][i] is None:
            recovery_grid[51][i] = [[], (1, 1, 1)]
    for i in range(7):
        if strain_grid[51][i] is None:
            strain_grid[51][i] = [[], (1, 1, 1)]


    return hours_vs_needed_grid, sleep_consistency_grid, recovery_grid, strain_grid

def get_dynamic_month_labels():
    """Get month labels that appear under weeks containing the 1st of each month"""
    start_date = get_heatmap_start_date()
    
    month_positions = []
    month_labels = []
    
    # Go through each week and check if it contains the 1st of a month
    for week in range(52):
        # Calculate the date range for this week
        week_start = start_date + timedelta(weeks=week)
        
        # Check each day in this week to see if it's the 1st of a month
        for day_offset in range(7):
            check_date = week_start + timedelta(days=day_offset)
            
            # If this date is the 1st of a month, add a label for this week
            if check_date.day == 1:
                month_positions.append(week+0.5)
                month_labels.append(check_date.strftime('%b'))
                break  # Only add one label per week
    
    return month_positions, month_labels

def plot_heatmap(grid):

    fig, ax = plt.subplots(figsize=(16, 4), dpi=240)
    
    # Create the heatmap with rounded rectangles
    for week in range(52):
        for day in range(7):
            cell_data = grid[week][day]
            if cell_data is not None:
                color = cell_data[1]  # RGB color
            else:
                color = (0.941, 0.949, 0.961)  # Light gray for empty cells
            
            # Create rounded rectangle using FancyBboxPatch
            rounded_rect = FancyBboxPatch(
                (week, 6-day), 0.85, 0.85,  # Slightly smaller for spacing
                boxstyle="round, pad=0.1, rounding_size=0.5",
                linewidth=1.75,
                edgecolor='white',
                facecolor=color,
                mutation_scale=0.5
            )
            ax.add_patch(rounded_rect)
    
    # Set up the plot
    ax.set_xlim(-0.5, 52.5)
    ax.set_ylim(-0.5, 7.5)
    ax.set_aspect('equal')
    
    # Add day labels
    day_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ax.set_yticks([6.5, 5.5, 4.5, 3.5, 2.5, 1.5, 0.5])
    ax.set_yticklabels(day_labels, fontsize=11, fontweight='500')
    
    # Add dynamic month labels
    month_positions, month_labels = get_dynamic_month_labels()
    ax.set_xticks(month_positions)
    ax.set_xticklabels(month_labels, fontsize=11, fontweight='500')
    
    # Style the plot
    ax.tick_params(axis='both', which='major', labelsize=11)
    ax.tick_params(axis='x', which='major', pad=12)
    ax.tick_params(axis='y', which='major', pad=8)
    
    # Remove spines and grid
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)
    
    plt.tight_layout()
    
    return fig

hours_vs_needed_grid, sleep_consistency_grid, recovery_grid, strain_grid = fill_grids()

def plot_sufficiency_heatmap():
    return plot_heatmap(hours_vs_needed_grid)
def plot_consistency_heatmap():
    return plot_heatmap(sleep_consistency_grid)
def plot_recovery_heatmap():
    return plot_heatmap(recovery_grid)
def plot_strain_heatmap():
    return plot_heatmap(strain_grid)