from datetime import datetime, timedelta
import pandas as pd
import os

# Constants
FILENAME = "data.csv"

def load_data():
    """Load data from the local CSV file"""
    try:
        if not os.path.exists(FILENAME):
            print(f"Warning: {FILENAME} not found. Please run main.py to create data first.")
            return None
        
        df = pd.read_csv(FILENAME, usecols=["date", "hours_vs_needed", "sleep_consistency"], parse_dates=["date"])
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def get_hours_vs_needed_rgb(row):
    """Get RGB color for hours vs needed percentage"""
    value = row["hours_vs_needed"]
    if pd.isna(value):
        return (0.235, 0.235, 0.235)  # Dark gray for missing data
    elif value >= 92.5:
        return (0.106, 0.271, 0.125)  # Darker green
    elif value >= 85:
        return (0.196, 0.455, 0.220)  # Dark green
    elif value >= 77.5:
        return (0.314, 0.624, 0.345)  # Medium green
    elif value >= 70:
        return (0.565, 0.792, 0.596)  # Light green
    else:
        return (0.906, 0.906, 0.906)  # Light gray

def get_sleep_consistency_rgb(row):
    """Get RGB color for sleep consistency percentage"""
    value = row["sleep_consistency"]
    if pd.isna(value):
        return (0.235, 0.235, 0.235)  # Dark gray for missing data
    elif value >= 90:
        return (0.106, 0.271, 0.125)  # Darker green
    elif value >= 80:
        return (0.196, 0.455, 0.220)  # Dark green
    elif value >= 70:
        return (0.314, 0.624, 0.345)  # Medium green
    elif value >= 60:
        return (0.565, 0.792, 0.596)  # Light green
    else:
        return (0.906, 0.906, 0.906)  # Light gray

def get_heatmap_start_date():
    """Get the start date for the heatmap (52 weeks ago from this Monday)"""
    today = datetime.today().date()
    # Go to Monday of this week
    this_monday = today - timedelta(days=today.weekday())  # Monday=0
    # Go back 51 full weeks
    return this_monday - timedelta(weeks=51)

def get_week_and_day(date, start_date):
    """Get week and day indices for a given date"""
    days_since_start = (date - start_date).days
    if not 0 <= days_since_start < 364:  # Exactly 52 weeks
        return None, None
    week = days_since_start // 7
    day = date.weekday()  # Monday = 0, Sunday = 6
    return week, day

def fill_grids():
    """Create and fill the heatmap grids"""
    df = load_data()
    if df is None:
        return None, None
    
    # Add RGB columns
    df["hours_vs_needed_rgb"] = df.apply(lambda row: get_hours_vs_needed_rgb(row), axis=1)
    df["sleep_consistency_rgb"] = df.apply(lambda row: get_sleep_consistency_rgb(row), axis=1)
    
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
    
    start_date = get_heatmap_start_date()
    
    for _, row in df.iterrows():
        date = row["date"].date()
        week, day = get_week_and_day(date, start_date)
        
        if week is not None and day is not None:
            hours_vs_needed_grid[week][day] = [date, row["hours_vs_needed_rgb"]]
            sleep_consistency_grid[week][day] = [date, row["sleep_consistency_rgb"]]
    
    return hours_vs_needed_grid, sleep_consistency_grid

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
                month_positions.append(week)
                month_labels.append(check_date.strftime('%b'))
                break  # Only add one label per week
    
    return month_positions, month_labels