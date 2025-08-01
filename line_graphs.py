import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import styles

FILENAME = "data.csv"
COLORS = styles.COLORS
SUFFICIENCY_RANGES = styles.SUFFICIENCY_RANGES
CONSISTENCY_RANGES = styles.CONSISTENCY_RANGES
RECOVERY_RANGES = styles.RECOVERY_RANGES
STRAIN_RANGES = styles.STRAIN_RANGES

def load_data():
    try:
        if not os.path.exists(FILENAME):
            print(f"Warning: {FILENAME} not found. Please run main.py to create data first.")
            return None
        
        df = pd.read_csv(FILENAME, usecols=["date", "hours_vs_needed", "sleep_consistency", "recovery", "strain"], parse_dates=["date"])
        return df.iloc[-365:]
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

    fig, ax = plt.subplots(figsize=(12, 6), dpi=240)
    
    
    # Define colors that match your app's green theme
    colors = {
        'daily': '#ffffff',        # White for daily values
        '7d_ma': '#dadada',       # Dark grey for 7-day MA
        '30d_ma': '#000000',      # black for 30-day MA
        'grid': '#ffffff',        # Very light green for grid
        'text': '#000000'         # Dark text color
    }
    
    # Plot the lines with improved styling and higher zorder to appear above background
    ax.plot(df['date'], df[col], 
            label="Daily Values", 
            color=colors['daily'], 
            linewidth=2, 
            alpha=1.0,
            zorder=1)

    ax.plot(df['date'], df["7d_ma"], 
            label="7-Day Moving Average", 
            color=colors['7d_ma'], 
            linewidth=4,
            alpha=1.0,
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
        'recovery': 'Recovery',
        'strain': 'Strain'
    }
    
    if col == 'strain':
        ax.set_ylabel(f"{metric_names.get(col, col.replace('_', ' ').title())}", 
                    fontsize=10, 
                    fontweight='500',
                    color=colors['text'],
                    fontfamily='sans-serif')
    else:
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
    
    legend = ax.legend(loc='upper center', 
                      bbox_to_anchor=(0.5, 1.08),
                      ncol=3,
                      frameon=True,
                      fancybox=True,
                      fontsize=10,
                      framealpha=0.95)
    legend.get_frame().set_facecolor(COLORS['col3'])
    legend.get_frame().set_edgecolor(COLORS['col1'])
    
    # Remove top and right spines for cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(colors['grid'])
    ax.spines['bottom'].set_color(colors['grid'])
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    
    # Add background coloring based on performance zones using your heatmap colors
    if col == 'hours_vs_needed':
        ax.axhspan(SUFFICIENCY_RANGES['tier1'], SUFFICIENCY_RANGES['tier0'], alpha=0.9, color=COLORS['col1'], zorder=0)  # Darker green
        ax.axhspan(SUFFICIENCY_RANGES['tier2'], SUFFICIENCY_RANGES['tier1'], alpha=0.9, color=COLORS['col2'], zorder=0)   # Dark green
        ax.axhspan(SUFFICIENCY_RANGES['tier3'], SUFFICIENCY_RANGES['tier2'], alpha=0.9, color=COLORS['col3'], zorder=0)   # Medium green
        ax.axhspan(SUFFICIENCY_RANGES['tier4'], SUFFICIENCY_RANGES['tier3'], alpha=0.9, color=COLORS['col4'], zorder=0)   # Light green
        ax.axhspan(SUFFICIENCY_RANGES['tier5'], SUFFICIENCY_RANGES['tier4'], alpha=0.9, color=COLORS['col5'], zorder=0)      # Light gray
    elif col == 'sleep_consistency':
        ax.axhspan(CONSISTENCY_RANGES['tier1'], CONSISTENCY_RANGES['tier0'], alpha=0.9, color=COLORS['col1'], zorder=0)  # Darker green
        ax.axhspan(CONSISTENCY_RANGES['tier2'], CONSISTENCY_RANGES['tier1'], alpha=0.9, color=COLORS['col2'], zorder=0)   # Dark green
        ax.axhspan(CONSISTENCY_RANGES['tier3'], CONSISTENCY_RANGES['tier2'], alpha=0.9, color=COLORS['col3'], zorder=0)   # Medium green
        ax.axhspan(CONSISTENCY_RANGES['tier4'], CONSISTENCY_RANGES['tier3'], alpha=0.9, color=COLORS['col4'], zorder=0)   # Light green
        ax.axhspan(CONSISTENCY_RANGES['tier5'], CONSISTENCY_RANGES['tier4'], alpha=0.9, color=COLORS['col5'], zorder=0)      # Light gray
    elif col == 'recovery':
        ax.axhspan(RECOVERY_RANGES['tier1'], RECOVERY_RANGES['tier0'], alpha=0.9, color=COLORS['col1'], zorder=0)  # Darker green
        ax.axhspan(RECOVERY_RANGES['tier2'], RECOVERY_RANGES['tier1'], alpha=0.9, color=COLORS['col2'], zorder=0)   # Dark green
        ax.axhspan(RECOVERY_RANGES['tier3'], RECOVERY_RANGES['tier2'], alpha=0.9, color=COLORS['col3'], zorder=0)   # Medium green
        ax.axhspan(RECOVERY_RANGES['tier4'], RECOVERY_RANGES['tier3'], alpha=0.9, color=COLORS['col4'], zorder=0)   # Light green
        ax.axhspan(RECOVERY_RANGES['tier5'], RECOVERY_RANGES['tier4'], alpha=0.9, color=COLORS['col5'], zorder=0)      # Light gray
    elif col == 'strain':
        ax.axhspan(STRAIN_RANGES['tier1'], STRAIN_RANGES['tier0'], alpha=0.9, color=COLORS['col1'], zorder=0)  # Darker green
        ax.axhspan(STRAIN_RANGES['tier2'], STRAIN_RANGES['tier1'], alpha=0.9, color=COLORS['col2'], zorder=0)   # Dark green
        ax.axhspan(STRAIN_RANGES['tier3'], STRAIN_RANGES['tier2'], alpha=0.9, color=COLORS['col3'], zorder=0)   # Medium green
        ax.axhspan(STRAIN_RANGES['tier4'], STRAIN_RANGES['tier3'], alpha=0.9, color=COLORS['col4'], zorder=0)   # Light green
        ax.axhspan(STRAIN_RANGES['tier5'], STRAIN_RANGES['tier4'], alpha=0.9, color=COLORS['col5'], zorder=0)      # Light gray

    # Set y-axis limits with some padding
    if col == 'strain':
        offset = 2
        real_max = 21
    else:
        offset = 5
        real_max = 100
    
    y_min = min(df[col].min(), df["7d_ma"].min(), df["30d_ma"].min()) - offset
    y_max = max(df[col].max(), df["7d_ma"].max(), df["30d_ma"].max()) + offset
    ax.set_ylim(max(0, y_min), min(real_max, y_max))
    
    # Tight layout with extra padding for legend
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.25)
    
    return fig

def make_sleep_sufficiency_plot():
    return make_plot('hours_vs_needed')

def make_sleep_consistency_plot():
    return make_plot('sleep_consistency')

def make_recovery_plot():
    return make_plot('recovery')

def make_strain_plot():
    return make_plot('strain')
