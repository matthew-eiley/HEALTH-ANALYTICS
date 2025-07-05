import streamlit as st
import heat_maps
import main
import styles
import line_charts

st.set_page_config(
    page_title="Health Analytics Dashboard",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(styles.STYLES, unsafe_allow_html=True)

# =================================================================================================
# ============================================ SLEEP ==============================================
# =================================================================================================

def do_sleep_section(stats):
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">🛏️ Sleep Performance</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(styles.SLEEP_DESC, unsafe_allow_html=True)
    
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
        fig1 = heat_maps.plot_sufficiency_heatmap()
        st.pyplot(fig1, use_container_width=True)
        fig1 = line_charts.make_sleep_sufficiency_plot()
        st.pyplot(fig1, use_container_width=True)
        avg_sufficiency = stats['avg_hours_vs_needed']
        if avg_sufficiency >= 85:
            st.success(f"🌟 Optimal! My average sleep sufficiency this week was {avg_sufficiency:.2f}%")
        elif avg_sufficiency >= 75:
            st.info(f"✅ Sufficient! My average sleep sufficiency this week was {avg_sufficiency:.2f}%")
        else:
            st.warning(f"⚠️ Poor. My average sleep consistency this week was {avg_sufficiency:.2f}%")
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
        fig2 = heat_maps.plot_consistency_heatmap()
        st.pyplot(fig2, use_container_width=True)
        fig2 = line_charts.make_sleep_consistency_plot()
        st.pyplot(fig2, use_container_width=True)
        avg_consistency = stats['avg_sleep_consistency']
        if avg_consistency >= 80:
            st.success(f"🌟 Optimal! My average sleep consistency this week was {avg_consistency:.2f}%")
        elif avg_consistency >= 70:
            st.info(f"✅ Sufficient! My average sleep consistency this week was {avg_consistency:.2f}%")
        else:
            st.warning(f"⚠️ Poor. My average sleep consistency this week was {avg_consistency:.2f}%")

# =================================================================================================
# ======================================= RECOVERY/STRAIN =========================================
# =================================================================================================

def do_recovery_strain_section(stats):
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">🥇 Recovery and Strain</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(styles.RECOVERY_STRAIN_DESC, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="left-header">
                <h3 class="subsection-title">🔋 Recovery</h3>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center;">
            <a href="https://www.whoop.com/eu/en/thelocker/how-does-whoop-recovery-work-101/?srsltid=AfmBOorJ-ddeY6KL9P_uVgBrrj_bFIhZ7I6tIiIbCJiCe3Wqc6FqDZgk" class="doc-link" target="_blank">
                📚 DOCUMENTATION →
            </a>
        </div>
        """, unsafe_allow_html=True)
        fig1 = heat_maps.plot_recovery_heatmap()
        st.pyplot(fig1, use_container_width=True)
        fig1 = line_charts.make_recovery_plot()
        st.pyplot(fig1, use_container_width=True)
        avg_recovery = stats['avg_recovery']
        if avg_recovery >= 72.5:
            st.success(f"🌟 Optimal! My average recovery this week was {avg_recovery:.2f}%")
        elif avg_recovery >= 65:
            st.info(f"✅ Sufficient! My average recovery this week was {avg_recovery:.2f}%")
        else:
            st.warning(f"⚠️ Poor. My average recovery this week was {avg_recovery:.2f}%")
    with col2:
        st.markdown("""
            <div class="right-header">
                <h3 class="subsection-title">💪 Strain</h3>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center;">
            <a href="https://www.whoop.com/us/en/thelocker/how-does-whoop-strain-work-101/?srsltid=AfmBOopjXT4iy1QQTkIskw19chbwJkkfTVwzED97Jb5TTaOxoeiNRGo5" class="doc-link" target="_blank">
                📚 DOCUMENTATION →
            </a>
        </div>
        """, unsafe_allow_html=True)
        fig2 = heat_maps.plot_strain_heatmap()
        st.pyplot(fig2, use_container_width=True)
        fig2 = line_charts.make_strain_plot()
        st.pyplot(fig2, use_container_width=True)
        avg_strain = stats['avg_strain']
        if avg_strain >= 14:
            st.success(f"🌟 Optimal! My average strain this week was {avg_strain:.2f}%")
        elif avg_strain >= 12.5:
            st.info(f"✅ Sufficient! My average strain this week was {avg_strain:.2f}%")
        else:
            st.warning(f"⚠️ Poor. My average strain this week was {avg_strain:.2f}%")


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
    
        
    do_sleep_section(stats)

    do_recovery_strain_section(stats)
    
if __name__ == "__main__":
    main_app()