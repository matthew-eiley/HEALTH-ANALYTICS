import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import sleep
import main

# Page configuration
st.set_page_config(
    page_title="Health Analytics Dashboard",
    page_icon="🍎",
    layout="wide"
)

def plot_heatmap(grid, title):
    """Create a GitHub-style heatmap with rounded corners"""
    # Set up the figure with higher DPI for better quality
    fig, ax = plt.subplots(figsize=(16, 4), dpi=100)
    fig.patch.set_facecolor('white')
    
    # Create the heatmap with rounded rectangles
    for week in range(52):
        for day in range(7):
            cell_data = grid[week][day]
            
            if cell_data is not None:
                color = cell_data[1]  # RGB color
            else:
                color = (0.906, 0.906, 0.906)  # Light gray for empty cells
            
            # Create rounded rectangle using FancyBboxPatch
            rounded_rect = FancyBboxPatch(
                (week, 6-day), 0.85, 0.85,  # Slightly smaller for spacing
                boxstyle="round,pad=0.5",
                linewidth=1,
                edgecolor='white',
                facecolor=color,
                mutation_scale=0.1
            )
            ax.add_patch(rounded_rect)
    
    # Set up the plot
    ax.set_xlim(-0.5, 52.5)
    ax.set_ylim(-0.5, 7.5)
    ax.set_aspect('equal')
    
    # Add day labels
    day_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ax.set_yticks([6.5, 5.5, 4.5, 3.5, 2.5, 1.5, 0.5])
    ax.set_yticklabels(day_labels)
    
    # Add dynamic month labels
    month_positions, month_labels = sleep.get_dynamic_month_labels()
    ax.set_xticks(month_positions)
    ax.set_xticklabels(month_labels)
    
    # Style the plot
    ax.tick_params(axis='both', which='major', labelsize=10)
    ax.tick_params(axis='x', which='major', pad=10)
    ax.tick_params(axis='y', which='major', pad=5)
    
    # Remove spines and grid
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)
    
    # Set title
    ax.set_title(title, fontsize=18, fontweight='bold', pad=25)
    
    plt.tight_layout()
    return fig


def display_insights(stats):
    if stats is None:
        return
    
    st.markdown("---")
    st.subheader("Performance Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Sleep Sufficiency Performance")
        avg_hours = stats['avg_hours_vs_needed']
        if avg_hours >= 85:
            st.success(f"Optimal! My average sleep duration this week is {avg_hours:.2f}%")
        elif avg_hours >= 70:
            st.info(f"Sufficient! My average sleep duration this week is {avg_hours:.2f}%")
        else:
            st.warning(f"Poor. My average sleep duration this week is {avg_hours:.2f}%")
    
    with col2:
        st.markdown("### Sleep Consistency Performance")
        avg_consistency = stats['avg_sleep_consistency']
        if avg_consistency >= 80:
            st.success(f"Optimal! My average sleep consistency this week is {avg_consistency:.2f}%")
        elif avg_consistency >= 70:
            st.info(f"Sufficient! My average sleep consistency this week is {avg_consistency:.2f}%")
        else:
            st.warning(f"Poor. My average sleep consistency this week is {avg_consistency:.2f}%")

def main_app():
    st.title("Health Analytics Dashboard")
    st.markdown("""This project is a personal health monitoring and visualization tool powered by WHOOP. 
                It retrieves and analyzes my recovery, sleep, strain, and cardiovascular metrics to help 
                optimize physical performance and daily wellbeing.""")
    st.markdown("---")

    # Get basic statistics
    stats = main.get_basic_stats()
    
    # Display basic stats

    col1, col2 = st.columns(2)
    with col1:
        st.metric("**Days Tracked**", f"{stats['total_days']}")
    with col2:
        st.metric("**Last Updated**", f"{main.TODAY.strftime('%A, %B %d, %Y, %H:%M:%S')}")

    col3, col4, col5, col6, col7 = st.columns(5)
    with col3:
        st.metric("**This Week's Avg Sleep Sufficiency**", f"{stats['avg_hours_vs_needed']:.2f}%")
    with col4:
        st.metric("**This Week's Avg Sleep Consistency**", f"{stats['avg_sleep_consistency']:.2f}%")
    with col5:
        st.metric("**This Week's Avg Recovery**", f"{stats['avg_recovery']:.2f}%")
    with col6:
        st.metric("**This Week's Avg Strain**", f"{stats['avg_strain']:.2f}")
    with col7:
        st.metric("**This Week's Avg HRV**", f"{stats['avg_hrv']:.2f} ms")

    
    # Create grids using the sleep module
    with st.spinner("Loading heatmap data..."):
        hours_vs_needed_grid, sleep_consistency_grid = sleep.fill_grids()
        
    # Display heatmaps
    st.markdown("---")
    
    # Hours vs Needed Heatmap
    st.subheader("Sleep Sufficiency")
    st.markdown("""WHOOP defines Sleep Sufficiency as the percentage of sleep you actually 
                achieved compared to your personalized “sleep need,” which varies nightly 
                based on your strain, sleep debt, and naps. Unlike generic 7-9 hour guidelines, 
                WHOOP dynamically calibrates your individual requirement. So if you only slept 
                85% of what you needed, your body and readiness may feel more impacted than 
                simply missing that 7-9 hour target. Over time, consistent underperformance 
                in this area contributes to mounting sleep debt and can diminish recovery, 
                readiness, and daytime function.""")
    st.markdown("[DOCUMENTATION &rarr;](https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US)")
    
    fig1 = plot_heatmap(hours_vs_needed_grid, "Sleep Sufficiency (%)")
    st.pyplot(fig1, use_container_width=True)
    
    st.markdown("---")
    
    # Sleep Consistency Heatmap
    st.subheader("Sleep Consistency")
    st.markdown("""Sleep Consistency measures how regularly your bedtime and wake time align across 
                consecutive days — WHOOP compares your last night's timing to the preceding four nights. 
                Research shows that consistent sleep schedules — even if total sleep is the same — are 
                linked to better cognitive outcomes, hormonal regulation (like melatonin), more deep and
                REM sleep, higher HRV, and better overall recovery. WHOOP even highlights that irregularity, 
                such as catching up on weekends, can disrupt circadian rhythms and hamper the quality and 
                effectiveness of your sleep, reducing the benefits of even sufficient rest""")
    st.markdown("[DOCUMENTATION &rarr;](https://support.whoop.com/s/article/WHOOP-Sleep?language=en_US)")
    
    fig2 = plot_heatmap(sleep_consistency_grid, "Sleep Consistency (%)")
    st.pyplot(fig2, use_container_width=True)
        
    # Display insights
    display_insights(stats)
    
    # Color coding explanation
    st.markdown("---")
    st.subheader("Color Guide")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Sleep Sufficiency**")
        st.markdown("- **Dark Green (≥92.5%)**: Excellent sleep duration")
        st.markdown("- **Medium Green (85-92.5%)**: Good sleep duration")
        st.markdown("- **Light Green (77.5-85%)**: Adequate sleep duration")
        st.markdown("- **Very Light Green (70-77.5%)**: Below optimal")
        st.markdown("- **Gray (<70%)**: Insufficient sleep")
    
    with col2:
        st.markdown("**Sleep Consistency**")
        st.markdown("- **Dark Green (≥90%)**: Very consistent schedule")
        st.markdown("- **Medium Green (80-90%)**: Good consistency")
        st.markdown("- **Light Green (70-80%)**: Moderate consistency")
        st.markdown("- **Very Light Green (60-70%)**: Poor consistency")
        st.markdown("- **Gray (<60%)**: Very inconsistent")

if __name__ == "__main__":
    main_app()
