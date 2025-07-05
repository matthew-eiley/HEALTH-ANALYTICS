STYLES = """
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styling */
    .main {
        padding-top: 2rem;
    }
    
    /* Custom font */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(45deg, #2e6130 0%, #baecbf 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-subtitle {
        font-size: 1.2rem;
        font-weight: 300;
        opacity: 0.9;
        line-height: 1.6;
    }
    
    /* Metrics container */
    .metrics-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        margin: 2rem 0;
        border: 1px solid #f0f2f6;
    }
    
    /* Section headers */
    .section-header {
        background: linear-gradient(45deg, #2e6130 0%, #baecbf 100%);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 2rem 0 1rem 0;
        color: white;
        text-align: center;
    }
    .left-header {
        background: linear-gradient(90deg, #baecbf 0%, #2e6130 100%);
        padding: 0.5rem 1rem;
        border-radius: 12px;
        margin: 2rem 0 1rem 0;
        color: white;
        text-align: center;
    }
    .right-header {
        background: linear-gradient(90deg, #2e6130 0%, #baecbf 100%);
        padding: 0.5rem 1rem;
        border-radius: 12px;
        margin: 2rem 0 1rem 0;
        color: white;
        text-align: center;
    }

    .subsection-title {
        font-size: 1rem;
        margin: 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }

    
    .section-title {
        font-size: 2rem;
        font-weight: 600;
        margin: 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    /* Content cards */
    .content-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 3px 15px rgba(0,0,0,0.06);
        margin: 1rem 0;
    }
    
    /* Insights container */
    .insights-container {
        background: linear-gradient(45deg, #2e6130 0%, #baecbf 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
    }
    
    .insights-title {
        color: #8b4513;
        font-weight: 600;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        text-align: left;
    }
    
    /* Color guide styling */
    .color-guide {
        background: linear-gradient(45deg, #2e6130 0%, #baecbf 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
    }
    
    .color-guide-title {
        color: #2c3e50;
        font-weight: 600;
        font-size: 1.8rem;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    /* Metric styling */
    .stMetric {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        border: 1px solid #f0f2f6;
    }
    
    /* Spinner styling */
    .stSpinner {
        text-align: center;
    }
    
    /* Documentation link styling */
    .doc-link {
        background: rgb(240, 242, 245);
        color: #2e6130 !important;
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        text-decoration: none !important;
        font-weight: 500;
        display: inline-block;
        margin: 1rem 0;
        box-shadow: 0 3px 15px #2e6130;
        transition: transform 0.2s ease;
    }
    
    .doc-link:hover {
        transform: translateY(-2px);
        color: rgb(109, 191, 116) !important;
        box-shadow: 0 3px 15px rgb(109, 191, 116);

    }
    
    /* Divider styling */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(45deg, #2e6130 0%, #baecbf 100%);
        margin: 3rem 0;
        border-radius: 2px;
    }
    
    /* Success/Info/Warning message styling */
    .stSuccess, .stInfo, .stWarning {
        border-radius: 10px;
        border: none;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
</style>"""

SLEEP_DESC = """
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
    """

RECOVERY_STRAIN_DESC = """
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
    """