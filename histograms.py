import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

def create_weekday_plot(metric):
    """Create a beautiful weekday histogram for a specific metric"""
    df = load_data()
    if df is None:
        return None
    
    df["weekday"] = df["date"].dt.day_name()
    
    # Order weekdays
    weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Group by weekday and calculate mean & std
    grouped = df.groupby("weekday")[metric].agg(["mean", "std", "count"])
    grouped = grouped.reindex(weekday_order)  # Ensure correct order
    
    # Create figure with custom styling
    fig, ax = plt.subplots(figsize=(12, 6), dpi=240)
    fig.patch.set_facecolor('#fafbfc')
    ax.set_facecolor('#ffffff')
    
    # Define colors and styling
    colors = {
        'text': '#2c3e50',
        'grid': '#e8f5e8',
        'bar_edge': '#2c2c2c'
    }
    
    # Get bar colors based on performance levels
    def get_bar_color(value, metric_type):
        if metric_type == 'hours_vs_needed':
            if value >= 92.5:
                return (0.180, 0.380, 0.188)  # Darker green
            elif value >= 85:
                return (0.325, 0.635, 0.345)  # Dark green
            elif value >= 77.5:
                return (0.427, 0.749, 0.455)  # Medium green
            elif value >= 70:
                return (0.729, 0.925, 0.749)  # Light green
            else:
                return (0.941, 0.949, 0.961)  # Light gray
        elif metric_type == 'sleep_consistency':
            if value >= 90:
                return (0.325, 0.635, 0.345)  # Dark green
            elif value >= 80:
                return (0.196, 0.455, 0.220)  # Dark green
            elif value >= 70:
                return (0.427, 0.749, 0.455)  # Medium green
            elif value >= 60:
                return (0.729, 0.925, 0.749)  # Light green
            else:
                return (0.941, 0.949, 0.961)  # Light gray
        elif metric_type == 'recovery':
            if value >= 87.5:
                return (0.180, 0.380, 0.188)  # Darker green
            elif value >= 75:
                return (0.325, 0.635, 0.345)  # Dark green
            elif value >= 62.5:
                return (0.427, 0.749, 0.455)  # Medium green
            elif value >= 50:
                return (0.729, 0.925, 0.749)  # Light green
            else:
                return (0.941, 0.949, 0.961)  # Light gray
        else:  # strain or other metrics
            return (0.427, 0.749, 0.455)  # Default medium green
    
    # Create bars with individual colors
    x_pos = np.arange(len(weekday_order))
    bar_colors = [get_bar_color(grouped.loc[day, 'mean'], metric) for day in weekday_order]
    
    bars = ax.bar(x_pos, 
                  grouped['mean'], 
                  yerr=grouped['std'],
                  width=0.7,
                  color=bar_colors,
                  edgecolor=colors['bar_edge'],
                  linewidth=1.5,
                  capsize=8,
                  error_kw={'elinewidth': 2, 'capthick': 2, 'ecolor': colors['bar_edge']},
                  alpha=0.9)
    
    # Add value labels on top of bars
    for i, (bar, day) in enumerate(zip(bars, weekday_order)):
        height = bar.get_height()
        std_val = grouped.loc[day, 'std']
        ax.text(bar.get_x() + bar.get_width()/2., height + std_val + 1,
                f'{height:.1f}%',
                ha='center', va='bottom',
                fontsize=11, fontweight='600',
                color=colors['text'])
    
    # Customize labels and title
    metric_names = {
        'hours_vs_needed': 'Sleep Sufficiency',
        'sleep_consistency': 'Sleep Consistency',
        'recovery': 'Recovery',
        'strain': 'Strain'
    }
    
    title = f"{metric_names.get(metric, metric.replace('_', ' ').title())} by Day of Week"
    ax.set_title(title,
                fontsize=18,
                fontweight='600',
                color=colors['text'],
                pad=25,
                fontfamily='sans-serif')
    
    # Customize axes
    ax.set_xticks(x_pos)
    ax.set_xticklabels([day[:3] for day in weekday_order],  # Abbreviated day names
                      fontsize=12,
                      fontweight='500',
                      color=colors['text'])
    
    ylabel = f"Average {metric_names.get(metric, metric.replace('_', ' ').title())}"
    if metric != 'strain':
        ylabel += " (%)"
    
    ax.set_ylabel(ylabel,
                 fontsize=13,
                 fontweight='500',
                 color=colors['text'],
                 fontfamily='sans-serif')
    
    # Customize grid
    ax.grid(axis="y", linestyle="-", alpha=0.3, color=colors['grid'], linewidth=1)
    ax.set_axisbelow(True)
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(colors['grid'])
    ax.spines['bottom'].set_color(colors['grid'])
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    
    # Customize tick parameters
    ax.tick_params(axis='both',
                  which='major',
                  labelsize=11,
                  colors=colors['text'],
                  length=6,
                  width=1)
    
    # Set y-axis limits with padding
    y_max = max(grouped['mean'] + grouped['std']) + 5
    if metric == 'strain':
        ax.set_ylim(0, y_max)
    else:
        ax.set_ylim(0, min(100, y_max))
    
    plt.tight_layout()
    return fig

def create_sleep_sufficiency_weekday_plot():
    """Create weekday plot for sleep sufficiency"""
    return create_weekday_plot('hours_vs_needed')

def create_sleep_consistency_weekday_plot():
    """Create weekday plot for sleep consistency"""
    return create_weekday_plot('sleep_consistency')

def create_recovery_weekday_plot():
    """Create weekday plot for recovery"""
    return create_weekday_plot('recovery')

def create_strain_weekday_plot():
    """Create weekday plot for strain"""
    return create_weekday_plot('strain')

def create_combined_sleep_plot():
    """Create a side-by-side comparison of sleep metrics"""
    df = load_data()
    if df is None:
        return None
    
    df["weekday"] = df["date"].dt.day_name()
    weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Group data
    grouped = df.groupby("weekday")[["hours_vs_needed", "sleep_consistency"]].agg(["mean", "std"])
    grouped = grouped.reindex(weekday_order)
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=240)
    fig.patch.set_facecolor('#fafbfc')
    
    colors = {
        'text': '#2c3e50',
        'grid': '#e8f5e8',
        'bar_edge': '#2c2c2c'
    }
    
    # Helper function for individual subplot
    def style_subplot(ax, metric, title):
        ax.set_facecolor('#ffffff')
        
        # Get bar colors
        def get_bar_color(value, metric_type):
            if metric_type == 'hours_vs_needed':
                if value >= 92.5: return (0.180, 0.380, 0.188)
                elif value >= 85: return (0.325, 0.635, 0.345)
                elif value >= 77.5: return (0.427, 0.749, 0.455)
                elif value >= 70: return (0.729, 0.925, 0.749)
                else: return (0.941, 0.949, 0.961)
            else:  # sleep_consistency
                if value >= 90: return (0.325, 0.635, 0.345)
                elif value >= 80: return (0.196, 0.455, 0.220)
                elif value >= 70: return (0.427, 0.749, 0.455)
                elif value >= 60: return (0.729, 0.925, 0.749)
                else: return (0.941, 0.949, 0.961)
        
        x_pos = np.arange(len(weekday_order))
        means = grouped[(metric, 'mean')]
        stds = grouped[(metric, 'std')]
        bar_colors = [get_bar_color(means[day], metric) for day in weekday_order]
        
        bars = ax.bar(x_pos, means, yerr=stds,
                     width=0.7, color=bar_colors,
                     edgecolor=colors['bar_edge'], linewidth=1.5,
                     capsize=8, error_kw={'elinewidth': 2, 'capthick': 2, 'ecolor': colors['bar_edge']},
                     alpha=0.9)
        
        # Add value labels
        for i, (bar, day) in enumerate(zip(bars, weekday_order)):
            height = bar.get_height()
            std_val = stds[day]
            ax.text(bar.get_x() + bar.get_width()/2., height + std_val + 1,
                   f'{height:.1f}%', ha='center', va='bottom',
                   fontsize=10, fontweight='600', color=colors['text'])
        
        # Styling
        ax.set_title(title, fontsize=16, fontweight='600', color=colors['text'], pad=20)
        ax.set_xticks(x_pos)
        ax.set_xticklabels([day[:3] for day in weekday_order], fontsize=11, color=colors['text'])
        ax.set_ylabel("Average (%)", fontsize=12, fontweight='500', color=colors['text'])
        ax.grid(axis="y", linestyle="-", alpha=0.3, color=colors['grid'])
        ax.set_axisbelow(True)
        
        # Remove spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(colors['grid'])
        ax.spines['bottom'].set_color(colors['grid'])
        
        ax.set_ylim(0, min(100, max(means + stds) + 5))
    
    # Style both subplots
    style_subplot(ax1, 'hours_vs_needed', '😴 Sleep Sufficiency by Day')
    style_subplot(ax2, 'sleep_consistency', '⏰ Sleep Consistency by Day')
    
    plt.tight_layout()
    return fig
