import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import heat_maps
import main
import styles

st.set_page_config(
    page_title="Health Analytics Dashboard",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(styles.STYLES, unsafe_allow_html=True)

def plot_heatmap(grid):
    # Set up the figure with higher DPI for better quality
    fig, ax = plt.subplots(figsize=(16, 4), dpi=240)
    # fig.patch.set_facecolor('#fafbfc')
    
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
    month_positions, month_labels = heat_maps.get_dynamic_month_labels()
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

def do_sleep_section(stats, hours_vs_needed_grid, sleep_consistency_grid):
    # Sleep section
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">🛏️ Sleep Performance</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="content-card">
        <p style="font-size: 1.1rem; line-height: 1.7; color: #4a5568;">
            Sleep is one of the most critical factors influencing your recovery, performance, and 
            overall health. WHOOP measures your sleep in two key dimensions: <strong>Sleep Sufficiency</strong> and 
            <strong>Sleep Consistency</strong>. Sleep Sufficiency reflects how much sleep you got compared to your 
            personalized sleep need, which adjusts daily based on your recent strain, baseline sleep, 
            and other recovery demands. Rather than applying a fixed 7-9 hour standard, WHOOP calculates 
            how much sleep your body truly requires each night. Falling short, even by a small percentage, 
            can lead to accumulating sleep debt and diminished recovery over time. Complementing this, 
            Sleep Consistency tracks how aligned your bedtime and wake times are across consecutive days. 
            Even if you're getting the right quantity of sleep, irregular timing can disrupt your circadian 
            rhythm, impair hormonal balance, and reduce time spent in restorative deep and REM sleep. 
            Together, these two metrics provide a deeper, more personalized understanding of your sleep 
            quality and its impact on daily readiness.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="left-header">
                <h3 class="subsection-title">😴 Sleep Sufficiency</h3>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center;">
            <a href="https://www.whoop.com/us/en/thelocker/how-much-sleep-do-i-need/?srsltid=AfmBOoo1g8Wxz-9LwJZsyYMWgTiI9bVAE8jH6TXdonBwJTdsJ-49DJQY" class="doc-link" target="_blank">
                📚 DOCUMENTATION &rarr;
            </a>
        </div>
        """, unsafe_allow_html=True)
        fig1 = plot_heatmap(hours_vs_needed_grid)
        st.pyplot(fig1, use_container_width=True)
        avg_hours = stats['avg_hours_vs_needed']
        if avg_hours >= 85:
            st.success(f"🌟 Optimal! My average sleep sufficiency this week is {avg_hours:.2f}%")
        elif avg_hours >= 70:
            st.info(f"✅ Sufficient! My average sleep sufficiency this week is {avg_hours:.2f}%")
        else:
            st.warning(f"⚠️ Poor. My average sleep sufficiency this week is {avg_hours:.2f}%")
    with col2:
        st.markdown("""
            <div class="right-header">
                <h3 class="subsection-title">⏰ Sleep Consistency</h3>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align: center;">
            <a href="https://www.whoop.com/us/en/thelocker/new-feature-sleep-consistency-why-we-track-it/?srsltid=AfmBOoptQmcwOq7fRmA_bREINiwvGZkwuZUvaNW_OVazsHdu2omb-FPj" class="doc-link" target="_blank">
                📚 DOCUMENTATION &rarr;
            </a>        
        </div>
        """, unsafe_allow_html=True)
        fig2 = plot_heatmap(sleep_consistency_grid)
        st.pyplot(fig2, use_container_width=True)
        avg_consistency = stats['avg_sleep_consistency']
        if avg_consistency >= 80:
            st.success(f"🌟 Optimal! My average sleep consistency this week is {avg_consistency:.2f}%")
        elif avg_consistency >= 70:
            st.info(f"✅ Sufficient! My average sleep consistency this week is {avg_consistency:.2f}%")
        else:
            st.warning(f"⚠️ Poor. My average sleep consistency this week is {avg_consistency:.2f}%")

    
def main_app():

    # =============================================================================================
    # ========================================== HEADER ===========================================       
    # =============================================================================================


    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">Health Analytics Dashboard</h1>
        <p class="main-subtitle">
            This project is a comprehensive personal health monitoring and visualization 
            platform, powered by my WHOOP data. It continuously tracks, analyzes, and visualizes 
            key biometric data—including sleep, recovery, strain, and cardiovascular metrics 
            to uncover meaningful trends, highlight performance insights, and support more informed 
            decisions around training, rest, and long-term wellbeing. Through intuitive dashboards 
            and personalized feedback, the system helps optimize physical readiness, prevent burnout, 
            and foster a deeper connection between my lifestyle habits and physiological outcomes.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # =============================================================================================
    # ==================================== DASHBOARD OVERVIEW =====================================       
    # =============================================================================================

    # Get basic statistics
    stats = main.get_basic_stats()
    
    st.markdown("### 📊 Dashboard Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("**📅 Days Tracked**", f"{stats['total_days']}")
    with col2:
        st.metric("**🕐 Last Updated**", f"{stats['last_updated'].strftime('%A, %B %d, %Y')}")
    
    st.markdown("#### This Week's Key Metrics")
    col3, col4, col5, col6, col7 = st.columns(5)
    with col3:
        st.metric("**😴 Avg Sleep Sufficiency**", f"{stats['avg_hours_vs_needed']:.2f}%")
    with col4:
        st.metric("**⏰ Avg Sleep Consistency**", f"{stats['avg_sleep_consistency']:.2f}%")
    with col5:
        st.metric("**🔋 Avg Recovery**", f"{stats['avg_recovery']:.2f}%")
    with col6:
        st.metric("**💪 Avg Strain**", f"{stats['avg_strain']:.2f}")
    with col7:
        st.metric("**❤️ Avg HRV**", f"{stats['avg_hrv']:.2f} ms")
    
    # =============================================================================================
    # ======================================= DATA SECTION ========================================       
    # =============================================================================================
    
    # Create grids using the sleep module
    with st.spinner("🔄 Loading heatmap data..."):
        hours_vs_needed_grid, sleep_consistency_grid, recovery_grid = heat_maps.fill_grids()
        
    do_sleep_section(stats, hours_vs_needed_grid, sleep_consistency_grid)

    # do_recovery_strain_section()

    # Recovery and Strain section
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">🥇 Recovery and Strain</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="content-card">
        <p style="font-size: 1.1rem; line-height: 1.7; color: #4a5568;">
            WHOOP measures your Recovery as a dynamic indicator of how ready your body is to perform, 
                based on biometric signals such as heart rate variability (HRV), resting heart rate (RHR), 
                respiratory rate, and sleep quality. Expressed as a percentage and color-coded (green, 
                yellow, or red), Recovery reflects how well your body has adapted to recent strain and 
                whether you're in a state of readiness or need rest. High Recovery signals strong parasympathetic 
                activity and good physiological balance, while low Recovery can indicate stress, fatigue, illness, 
                or inadequate sleep. Complementing this is Strain, WHOOP's cumulative measure of cardiovascular 
                load throughout the day. Unlike step counts or calories, Strain is personalized based on your fitness 
                level and previous activity, allowing you to train in alignment with your body's current capacity. 
                By comparing daily Strain to your Recovery, you gain insight into whether you're training optimally, 
                overreaching, or undertraining — enabling smarter decisions for performance, fitness gains, and long-term 
                resilience.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <a href="https://www.whoop.com/eu/en/thelocker/how-does-whoop-recovery-work-101/?srsltid=AfmBOorJ-ddeY6KL9P_uVgBrrj_bFIhZ7I6tIiIbCJiCe3Wqc6FqDZgk" class="doc-link" target="_blank">
        📚 RECOVERY DOCUMENTATION →
    </a>
    """, unsafe_allow_html=True)
    st.markdown("""
    <a href="https://www.whoop.com/us/en/thelocker/how-does-whoop-strain-work-101/?srsltid=AfmBOopjXT4iy1QQTkIskw19chbwJkkfTVwzED97Jb5TTaOxoeiNRGo5" class="doc-link" target="_blank">
        📚 STRAIN DOCUMENTATION →
    </a>
    """, unsafe_allow_html=True)
        
    st.markdown("### 📈 Recovery")
    fig3 = plot_heatmap(recovery_grid)
    st.pyplot(fig3, use_container_width=True)
    
    # Display insights
    
    # Color coding explanation
    
    st.markdown("""
    <div class="color-guide">
        <h3 class="color-guide-title">🎨 Color Guide</h3>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🛌 Sleep Sufficiency**
        - **🟢 Dark Green (≥92.5%)**: Excellent sleep duration
        - **🟢 Medium Green (85-92.5%)**: Good sleep duration  
        - **🟡 Light Green (77.5-85%)**: Adequate sleep duration
        - **🟡 Very Light Green (70-77.5%)**: Below optimal
        - **⚪ Gray (<70%)**: Insufficient sleep
        """)
    
    with col2:
        st.markdown("""
        **⏰ Sleep Consistency**
        - **🟢 Dark Green (≥90%)**: Very consistent schedule
        - **🟢 Medium Green (80-90%)**: Good consistency
        - **🟡 Light Green (70-80%)**: Moderate consistency
        - **🟡 Very Light Green (60-70%)**: Poor consistency
        - **⚪ Gray (<60%)**: Very inconsistent
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main_app()