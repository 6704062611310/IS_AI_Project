import streamlit as st
import joblib
import numpy as np
import time

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Euro Match AI",
    layout="centered"
)

# ======================
# STYLE
# ======================
st.markdown("""
<style>

header {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden;}
.block-container {padding-top: 0.5rem !important;}

.stApp {
    background: linear-gradient(135deg, #0f0014, #1a0024, #2a0036);
    color: #f2e6ff;
}

/* Title */
.hero-title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    letter-spacing: 3px;
    margin-top: 15px;
    margin-bottom: 5px;
    background: linear-gradient(90deg, #ff66cc, #cc66ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    text-align: center;
    font-size: 13px;
    opacity: 0.6;
    margin-bottom: 30px;
}

/* SCORE HERO */
.score-hero {
    width: 80%;
    margin: 20px auto 40px auto;
    padding: 50px;
    border-radius: 30px;
    text-align: center;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(25px);
    border: 1px solid rgba(255,105,180,0.2);
    box-shadow: 0 0 30px rgba(255,105,180,0.2);
}

.score-line {
    font-size: 65px;
    font-weight: 900;
    margin: 15px 0;
}

.team-row {
    font-size: 22px;
    font-weight: bold;
}

/* Probability */
.prob-box {
    width: 80%;
    margin: auto;
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    margin-top: 25px;
}

/* Labels */
label {
    color: #ffb3ff !important;
    font-weight: 600 !important;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #cc0066, #ff66cc);
    color: white;
    border-radius: 12px;
    padding: 10px 25px;
    font-weight: bold;
}

.stButton>button:hover {
    box-shadow: 0 0 15px #ff66cc;
}

/* Progress */
div[data-testid="stProgress"] > div > div > div > div {
    background: linear-gradient(90deg, #cc0066, #ff66cc) !important;
}

</style>
""", unsafe_allow_html=True)

# ======================
# TITLE
# ======================
st.markdown('<div class="hero-title">EURO MATCH AI</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Ensemble Model • Score Prediction</div>', unsafe_allow_html=True)

# ======================
# SCORE PLACEHOLDER
# ======================
score_placeholder = st.empty()

score_placeholder.markdown(
    '<div class="score-hero"><div class="score-line">Select Teams</div></div>',
    unsafe_allow_html=True
)

# ======================
# LOAD MODEL
# ======================
@st.cache_resource
def load_model():
    model = joblib.load("models/ensemble_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    return model, scaler

model, scaler = load_model()

# ======================
# TEAM DATA
# ======================
teams = {
    "France 🇫🇷": [90, 85, 2.1],
    "Germany 🇩🇪": [88, 82, 1.9],
    "Spain 🇪🇸": [87, 80, 1.8],
    "England 🏴": [89, 84, 2.0],
    "Italy 🇮🇹": [86, 78, 1.7],
    "Portugal 🇵🇹": [88, 83, 1.95],
    "Netherlands 🇳🇱": [85, 79, 1.75],
    "Belgium 🇧🇪": [87, 81, 1.85],
    "Croatia 🇭🇷": [84, 77, 1.6],
    "Denmark 🇩🇰": [82, 75, 1.5],
    "Switzerland 🇨🇭": [83, 76, 1.55],
    "Austria 🇦🇹": [80, 73, 1.45],
    "Turkey 🇹🇷": [81, 74, 1.5],
    "Poland 🇵🇱": [78, 70, 1.3],
    "Czech Republic 🇨🇿": [79, 71, 1.35],
    "Serbia 🇷🇸": [80, 72, 1.4],
}

# ======================
# SELECT TEAMS
# ======================
col1, col2 = st.columns(2)

with col1:
    home = st.selectbox("Home Team", list(teams.keys()))
with col2:
    away = st.selectbox("Away Team", list(teams.keys()))

if st.button("Predict Match"):

    with st.spinner("Analyzing match..."):
        time.sleep(1)

    hr, hf, hg = teams[home]
    ar, af, ag = teams[away]

    features = np.array([[hr, ar, hf, af, hg, ag]])
    features_scaled = scaler.transform(features)
    prob = model.predict_proba(features_scaled)[0]

    home_prob, draw_prob, away_prob = prob
    total_goals = 2.6

    if draw_prob > 0.4:
        home_goals = away_goals = round(total_goals / 2)
    else:
        home_share = home_prob / (home_prob + away_prob)
        home_goals = round(total_goals * home_share)
        away_goals = round(total_goals * (1 - home_share))

    if home_goals == away_goals and draw_prob < 0.4:
        if home_prob > away_prob:
            home_goals += 1
        else:
            away_goals += 1

    # ===== UPDATE SCORE WITH FLAGS =====
    score_placeholder.markdown(
        f'''
        <div class="score-hero">
            <div class="team-row">{home}</div>
            <div class="score-line">{home_goals} - {away_goals}</div>
            <div class="team-row">{away}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    # ===== PROBABILITY BACK =====
    st.markdown('<div class="prob-box">', unsafe_allow_html=True)

    labels = ["🏠 Home Win", "🤝 Draw", "✈️ Away Win"]

    for i in range(3):
        percentage = prob[i] * 100
        st.write(f"{labels[i]}: {percentage:.1f}%")
        st.progress(int(percentage))

    st.markdown('</div>', unsafe_allow_html=True)