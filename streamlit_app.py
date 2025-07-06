import streamlit as st
import heat_maps
import main
import styles
import line_graphs
import histograms

st.set_page_config(
    page_title="Health Analytics Dashboard",
    page_icon="🍎",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(styles.STYLES, unsafe_allow_html=True)

# =================================================================================================
# ======================================== SUFFICIENCY TAB ========================================
# =================================================================================================

def do_sufficiency_tab():
    st.markdown("""
        <div class="section-header">
            <h2 class="section-title">😴 Sleep Sufficiency Analysis</h2>
        </div>`
        """, unsafe_allow_html=True)
    st.markdown(styles.SLEEP_SUFFICIENCY_DESC, unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center;">
        <a href="https://www.whoop.com/us/en/thelocker/how-much-sleep-do-i-need/?srsltid=AfmBOoo1g8Wxz-9LwJZsyYMWgTiI9bVAE8jH6TXdonBwJTdsJ-49DJQY" class="doc-link" target="_blank">
            📚 WHOOP DOCUMENTATION &rarr;
        </a>
    </div>
    """, unsafe_allow_html=True)

    with st.spinner(text="⏳ Generating sleep sufficiency plots...", show_time=True):
        fig1 = line_graphs.make_sleep_sufficiency_plot()
        fig2 = heat_maps.plot_sufficiency_heatmap()
        fig3 = histograms.create_sleep_sufficiency_weekday_plot()
        st.pyplot(fig2, use_container_width=True)
        st.pyplot(fig1, use_container_width=True)
        st.pyplot(fig3, use_container_width=True)

# =================================================================================================
# ======================================== CONSISTENCY TAB ========================================
# =================================================================================================

def do_consistency_tab():
    st.markdown("""
        <div class="section-header">
            <h2 class="section-title">⏰ Sleep Consistency Analysis</h2>
        </div>
        """, unsafe_allow_html=True)
    st.markdown(styles.SLEEP_CONSISTENCY_DESC, unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center;">
            <a href="https://www.whoop.com/us/en/thelocker/new-feature-sleep-consistency-why-we-track-it/?srsltid=AfmBOoptQmcwOq7fRmA_bREINiwvGZkwuZUvaNW_OVazsHdu2omb-FPj" class="doc-link" target="_blank">
                📚 WHOOP DOCUMENTATION &rarr;
            </a>        
        </div>
        """, unsafe_allow_html=True)

    with st.spinner(text="⏳ Generating sleep consistency plots...", show_time=True):
        fig1 = line_graphs.make_sleep_consistency_plot()
        fig2 = heat_maps.plot_consistency_heatmap()
        fig3 = histograms.create_sleep_consistency_weekday_plot()
        st.pyplot(fig1, use_container_width=True)
        st.pyplot(fig2, use_container_width=True)
        st.pyplot(fig3, use_container_width=True)

# =================================================================================================
# ========================================= RECOVERY TAB ==========================================
# =================================================================================================

def do_recovery_tab():
    st.markdown("""
        <div class="section-header">
            <h2 class="section-title">🔋 Recovery Analysis</h2>
        </div>`
        """, unsafe_allow_html=True)
    st.markdown(styles.RECOVERY_DESC, unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center;">
            <a href="https://www.whoop.com/eu/en/thelocker/how-does-whoop-recovery-work-101/?srsltid=AfmBOorJ-ddeY6KL9P_uVgBrrj_bFIhZ7I6tIiIbCJiCe3Wqc6FqDZgk" class="doc-link" target="_blank">
                📚 WHOOP DOCUMENTATION &rarr;
            </a>
        </div>
        """, unsafe_allow_html=True)

    with st.spinner(text="⏳ Generating recovery plots...", show_time=True):
        fig1 = line_graphs.make_recovery_plot()
        fig2 = heat_maps.plot_recovery_heatmap()
        fig3 = histograms.create_recovery_weekday_plot()
        st.pyplot(fig1, use_container_width=True)
        st.pyplot(fig2, use_container_width=True)
        st.pyplot(fig3, use_container_width=True)

# =================================================================================================
# ========================================== STRAIN TAB ===========================================
# =================================================================================================

def do_strain_tab():
    st.markdown("""
        <div class="section-header">
            <h2 class="section-title">💪 Strain Analysis</h2>
        </div>
        """, unsafe_allow_html=True)
    st.markdown(styles.STRAIN_DESC, unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center;">
            <a href="https://www.whoop.com/us/en/thelocker/how-does-whoop-strain-work-101/?srsltid=AfmBOopjXT4iy1QQTkIskw19chbwJkkfTVwzED97Jb5TTaOxoeiNRGo5" class="doc-link" target="_blank">
                📚 WHOOP DOCUMENTATION →
            </a>
        </div>
        """, unsafe_allow_html=True)

    with st.spinner(text="⏳ Generating strain plots...", show_time=True):
        fig1 = line_graphs.make_strain_plot()
        fig2 = heat_maps.plot_strain_heatmap()
        fig3 = histograms.create_strain_weekday_plot()
        st.pyplot(fig1, use_container_width=True)
        st.pyplot(fig2, use_container_width=True)
        st.pyplot(fig3, use_container_width=True)


# =================================================================================================
# ============================================ MAIN ===============================================
# =================================================================================================

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
    deltas = main.get_stats_deltas()

    st.markdown("### 📊 Dashboard Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("**📅 Days Tracked**", f"{stats['total_days']}")
    with col2:
        st.metric("**🕐 Last Updated**", f"{stats['last_updated'].strftime('%B %d, %Y')}")
        
    st.markdown("#### This Week's Key Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("**😴 Avg Sleep Sufficiency**", f"{stats['avg_hours_vs_needed']:.2f}%", 
                  delta=deltas['avg_hours_vs_needed'])
    with col2:
        st.metric("**⏰ Avg Sleep Consistency**", f"{stats['avg_sleep_consistency']:.2f}%", 
                  delta=deltas['avg_sleep_consistency'])
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("**🔋 Avg Recovery**", f"{stats['avg_recovery']:.2f}%",
                  delta=deltas['avg_recovery'])
    with col2:
        st.metric("**💪 Avg Strain**", f"{stats['avg_strain']:.2f}",
                   delta=deltas['avg_strain'])
    with col3:
        st.metric("**❤️ Avg HRV**", f"{stats['avg_hrv']:.2f} ms",
            delta=deltas['avg_hrv'])

    
    # =============================================================================================
    # ======================================= TABBED SECTIONS ===================================       
    # =============================================================================================
    
    st.markdown("---")
    tab1, tab2, tab3, tab4 = st.tabs(["😴 **Sleep Sufficiency**", "⏰ **Sleep Consistency**", "🔋 **Recovery**", "💪 **Strain**"])
    with tab1:
        do_sufficiency_tab()
    with tab2:
        do_consistency_tab()
    with tab3:
        do_recovery_tab()
    with tab4:
        do_strain_tab()


if __name__ == "__main__":
    main_app()