import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

FILENAME = "data.csv"

def load_data():
    try:
        if not os.path.exists(FILENAME):
            print(f"Warning: {FILENAME} not found. Please run main.py to create data first.")
            return None
        
        df = pd.read_csv(FILENAME, usecols=["date", "hours_vs_needed", "sleep_consistency", "recovery"], parse_dates=["date"])
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def create_mas(col):
    df = load_data()
    if df is None:
        return None
    df["7d_ma"] = df[col].rolling(window=7, min_periods=1).mean()
    df["30d_ma"] = df[col].rolling(window=30, min_periods=1).mean()
    return df

def make_plot(col):
    df = create_mas(col)
    if df is None:
        return None
    
    # Create figure with custom styling to match your app
    fig, ax = plt.subplots(figsize=(12, 6), dpi=240)
    
    
    # Define colors that match your app's green theme
    colors = {
        'daily': '#ffffff',        # White for daily values
        '7d_ma': '#909090',       # Dark grey for 7-day MA
        '30d_ma': '#000000',      # black for 30-day MA
        'grid': '#ffffff',        # Very light green for grid
        'text': '#000000'         # Dark text color
    }
    
    # Plot the lines with improved styling and higher zorder to appear above background
    ax.plot(df['date'], df[col], 
            label="Daily Values", 
            color=colors['daily'], 
            linewidth=3, 
            alpha=0.75,
            zorder=1)

    ax.plot(df['date'], df["7d_ma"], 
            label="7-Day Moving Average", 
            color=colors['7d_ma'], 
            linewidth=4,
            alpha=0.75,
            zorder=2)

    ax.plot(df['date'], df["30d_ma"], 
            label="30-Day Moving Average", 
            color=colors['30d_ma'], 
            linewidth=4,
            alpha=1.0,
            zorder=3)
    
    # Customize the title and labels to match your app style
    metric_names = {
        'hours_vs_needed': 'Sleep Sufficiency',
        'sleep_consistency': 'Sleep Consistency', 
        'recovery': 'Recovery'
    }
    
    
    ax.set_ylabel(f"{metric_names.get(col, col.replace('_', ' ').title())} (%)", 
                 fontsize=10, 
                 fontweight='500',
                 color=colors['text'],
                 fontfamily='sans-serif')
        
    # Customize the grid to match your app
    ax.grid(True, 
           linestyle="-", 
           alpha=0.3, 
           color=colors['grid'],
           linewidth=1)
    ax.set_axisbelow(True)
    
    # Format the x-axis dates - always show exactly 5 evenly spaced dates
    date_range = df['date'].max() - df['date'].min()
    date_interval = date_range / 4  # 4 intervals = 5 dates
    date_ticks = [df['date'].min() + i * date_interval for i in range(5)]

    ax.set_xticks(date_ticks)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))

    # Rotate date labels for better readability
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=22.5, ha='right')
    
    # Customize tick parameters
    ax.tick_params(axis='both', 
                  which='major', 
                  labelsize=10,
                  colors=colors['text'],
                  length=6,
                  width=1)
    ax.tick_params(axis='both', 
                  which='minor', 
                  length=3,
                  width=0.5)
    
    # Style the legend to appear underneath the graph
    legend = ax.legend(loc='upper center', 
                      bbox_to_anchor=(0.5, -0.15),
                      ncol=3,
                      frameon=True,
                      fancybox=True,
                      fontsize=10,
                      framealpha=0.95)
    legend.get_frame().set_facecolor("#6dbf74")
    legend.get_frame().set_edgecolor(colors['grid'])
    
    # Remove top and right spines for cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(colors['grid'])
    ax.spines['bottom'].set_color(colors['grid'])
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    
    # Add background coloring based on performance zones using your heatmap colors
    if col == 'hours_vs_needed':
        ax.axhspan(92.5, 100, alpha=0.8, color=(0.180, 0.380, 0.188), zorder=0)  # Darker green
        ax.axhspan(85, 92.5, alpha=0.8, color=(0.325, 0.635, 0.345), zorder=0)   # Dark green
        ax.axhspan(77.5, 85, alpha=0.8, color=(0.427, 0.749, 0.455), zorder=0)   # Medium green
        ax.axhspan(70, 77.5, alpha=0.8, color=(0.729, 0.925, 0.749), zorder=0)   # Light green
        ax.axhspan(0, 70, alpha=0.8, color=(0.941, 0.949, 0.961), zorder=0)      # Light gray
    elif col == 'sleep_consistency':
        ax.axhspan(90, 100, alpha=0.8, color=(0.180, 0.380, 0.188), zorder=0)    # Dark green
        ax.axhspan(80, 90, alpha=0.8, color=(0.196, 0.455, 0.220), zorder=0)     # Dark green
        ax.axhspan(70, 80, alpha=0.8, color=(0.427, 0.749, 0.455), zorder=0)     # Medium green
        ax.axhspan(60, 70, alpha=0.8, color=(0.729, 0.925, 0.749), zorder=0)     # Light green
        ax.axhspan(0, 60, alpha=0.8, color=(0.941, 0.949, 0.961), zorder=0)      # Light gray
    elif col == 'recovery':
        ax.axhspan(87.5, 100, alpha=0.8, color=(0.180, 0.380, 0.188), zorder=0)  # Darker green
        ax.axhspan(75, 87.5, alpha=0.8, color=(0.325, 0.635, 0.345), zorder=0)   # Dark green
        ax.axhspan(62.5, 75, alpha=0.8, color=(0.427, 0.749, 0.455), zorder=0)   # Medium green
        ax.axhspan(50, 62.5, alpha=0.8, color=(0.729, 0.925, 0.749), zorder=0)   # Light green
        ax.axhspan(0, 50, alpha=0.8, color=(0.941, 0.949, 0.961), zorder=0)      # Light gray
    
    # Set y-axis limits with some padding
    y_min = min(df[col].min(), df["7d_ma"].min(), df["30d_ma"].min()) - 5
    y_max = max(df[col].max(), df["7d_ma"].max(), df["30d_ma"].max()) + 5
    ax.set_ylim(max(0, y_min), min(100, y_max))
    
    # Tight layout with extra padding for legend
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.25)
    
    return fig

def make_recovery_plot():
    """Create a specialized recovery plot"""
    return make_plot('recovery')

def make_sleep_sufficiency_plot():
    """Create a specialized sleep sufficiency plot"""
    return make_plot('hours_vs_needed')

def make_sleep_consistency_plot():
    """Create a specialized sleep consistency plot"""
    return make_plot('sleep_consistency')
