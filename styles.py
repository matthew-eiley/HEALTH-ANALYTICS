COLORS = {
    'col0': (0.235, 0.235, 0.235),
    'col1': (0.180, 0.380, 0.188),
    'col2': (0.325, 0.635, 0.345),
    'col3': (0.427, 0.749, 0.455),
    'col4': (0.729, 0.925, 0.749),
    'col5': (0.941, 0.949, 0.961)
}

SUFFICIENCY_RANGES = {
    'tier0': 100,
    'tier1': 92.5,
    'tier2': 85,
    'tier3': 77.5,
    'tier4': 70,
    'tier5': 0,
}
CONSISTENCY_RANGES = {
    'tier0': 100,
    'tier1': 90,
    'tier2': 80,
    'tier3': 70,
    'tier4': 60,
    'tier5': 0,
}
RECOVERY_RANGES = {
    'tier0': 100,
    'tier1': 87.5,
    'tier2': 75,
    'tier3': 62.5,
    'tier4': 50,
    'tier5': 0,
}
STRAIN_RANGES = {
    'tier0': 21,
    'tier1': 17.5,
    'tier2': 14,
    'tier3': 10.5,
    'tier4': 7,
    'tier5': 0,
}


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
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
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
        padding: 1rem 1rem;
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
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }

    .section-title {
        font-size: 2rem;
        font-weight: 600;
        margin: 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    
    /* Content cards */
    .content-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 3px 15px rgba(0,0,0,0.25);
        margin: 1rem 0;
    }
    
    /* Insights container */
    .insights-container {
        background: linear-gradient(45deg, #2e6130 0%, #baecbf 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.25);
    }
    
    .insights-title {
        color: #8b4513;
        font-weight: 600;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        text-align: left;
    }
        
    /* Metric styling */
    .stMetric {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
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
        padding: 0.75rem 2.5rem;
        border-radius: 25px;
        text-decoration: none !important;
        font-weight: 500;
        display: inline-block;
        margin-top: 1rem;
        margin-bottom: 2rem;
        box-shadow: 0 3px 15px #2e6130;
        transition: transform 0.2s ease;
    }
    
    .doc-link:hover {
        transform: translateY(-2px);
        color: rgb(109, 191, 116) !important;
        box-shadow: 0 3px 15px rgb(109, 191, 116);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 8px;
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0px 24px;
        background-color: transparent;
        border-radius: 8px;
        color: #2e6130;
        font-weight: 500;
        border: none;
        transition: all 0.2s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(45deg, #2e6130 0%, #baecbf 100%) !important;
        color: white !important;
        box-shadow: 0 2px 8px rgba(46, 97, 48, 0.5);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(46, 97, 48, 0.25);
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
        box-shadow: 0 2px 10px rgba(0,0,0,0.25);
    }
</style>"""

SLEEP_SUFFICIENCY_DESC = """
    <div class="content-card">
        <p style="font-size: 1rem; line-height: 1.75; color: #4a5568;">
            <strong>Sleep Sufficiency</strong> reflects how much sleep you received compared to what your body needed 
            on a given night. Rather than applying a generic 7-9 hour guideline, WHOOP calculates your individualized 
            sleep need based on recent strain, accumulated sleep debt, and recovery metrics. Achieving or exceeding this 
            target helps your body fully recover and maintain optimal performance. Even small nightly deficits can lead to 
            mounting sleep debt, increasing physiological stress, reducing cognitive clarity, and impairing overall readiness. 
            Monitoring Sleep Sufficiency over time helps ensure your sleep quantity supports your activity levels and recovery demands.
        </p>
    </div>
    """

SLEEP_CONSISTENCY_DESC = """
    <div class="content-card">
        <p style="font-size: 1rem; line-height: 1.75; color: #4a5568;">
            <strong>Sleep Consistency</strong> tracks how stable your bedtime and wake-up times are across consecutive days. 
            WHOOP evaluates consistency by comparing each night's sleep window to the prior four nights. Maintaining a consistent 
            schedule, even if your total sleep hours vary slightly, helps regulate your circadian rhythm, improves hormonal balance, 
            and enhances time spent in restorative deep and REM sleep. Irregular schedules, such as social jet lag or weekend 
            catch-up sleep, can disrupt recovery and reduce overall sleep efficiency. High sleep consistency supports both physical 
            recovery and mental sharpness.
        </p>
    </div>
    """

RECOVERY_DESC = """
    <div class="content-card">
        <p style="font-size: 1rem; line-height: 1.75; color: #4a5568;">
            <strong>Recovery</strong> is WHOOP's primary readiness metric, measuring how prepared your body is to perform 
            on any given day. It synthesizes key physiological signals such as heart rate variability (HRV), resting heart rate (RHR), 
            respiratory rate, and sleep performance into a single percentage score. A high Recovery score indicates strong autonomic 
            balance, effective rest, and resilience to recent stress or strain. Conversely, a low score may suggest fatigue, illness, 
            overtraining, or inadequate recovery. Monitoring Recovery day-to-day helps guide whether to push, maintain, or rest, empowering 
            smarter decisions for long-term physical and mental performance.
        </p>
    </div>
    """

STRAIN_DESC = """
    <div class="content-card">
        <p style="font-size: 1rem; line-height: 1.75; color: #4a5568;">
            <strong>Strain</strong> is WHOOP's personalized measure of cardiovascular and metabolic load, reflecting how much effort 
            you've exerted throughout the day. Calculated on a scale from 0 to 21, Strain accumulates based on workout intensity, 
            heart rate elevation, and sustained physical activity. Unlike simple step counts or calorie burn, WHOOP calibrates 
            Strain to your unique physiology, meaning the same activity may produce different strain levels for different people. 
            By comparing daily Strain to your Recovery score, you can ensure your training aligns with your body's readiness, 
            avoid overreaching, and build sustainable gains over time.
        </p>
    </div>
    """
