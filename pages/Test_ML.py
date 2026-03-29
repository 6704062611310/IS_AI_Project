import streamlit as st
import joblib
import numpy as np
import time

st.set_page_config(
    page_title="Euro Match AI",
    layout="centered"
)

st.markdown("""
<style>
header {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden;}
.block-container {padding-top: 0.5rem !important;}

.stApp {
    background:
        radial-gradient(circle at top, rgba(20,70,30,0.35), transparent 35%),
        linear-gradient(180deg, #06110a 0%, #0b1f12 45%, #08140d 100%);
    color: #f4fff6;
    font-family: 'Segoe UI', sans-serif;
}

/* top nav-ish hint */
.info-box {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 12px 16px;
    border-radius: 14px;
    margin-bottom: 18px;
    text-align: center;
    color: #d8ffe3;
}

/* Title */
.hero-title {
    text-align: center;
    font-size: 48px;
    font-weight: 900;
    letter-spacing: 3px;
    margin-top: 10px;
    margin-bottom: 6px;
    color: #ffffff;
    text-shadow: 0 0 18px rgba(120,255,160,0.22);
}

.hero-sub {
    text-align: center;
    font-size: 14px;
    opacity: 0.85;
    margin-bottom: 25px;
    color: #d7f7de;
}

/* main scoreboard */
.score-hero {
    width: 92%;
    margin: 18px auto 30px auto;
    padding: 28px 24px;
    border-radius: 28px;
    text-align: center;
    background: linear-gradient(180deg, rgba(255,255,255,0.07), rgba(255,255,255,0.04));
    backdrop-filter: blur(16px);
    border: 1px solid rgba(120,255,160,0.18);
    box-shadow: 0 0 28px rgba(0,0,0,0.25);
}

.match-label {
    font-size: 13px;
    letter-spacing: 2px;
    opacity: 0.75;
    margin-bottom: 18px;
    text-transform: uppercase;
}

.match-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
}

.team-box {
    width: 36%;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 18px 10px;
}

.team-flag {
    font-size: 44px;
    margin-bottom: 8px;
}

.team-name {
    font-size: 20px;
    font-weight: 700;
    line-height: 1.3;
}

.vs-box {
    width: 18%;
}

.vs-text {
    font-size: 18px;
    opacity: 0.7;
    margin-bottom: 6px;
}

.score-line {
    font-size: 52px;
    font-weight: 900;
    line-height: 1.1;
    color: #ffffff;
    text-shadow: 0 0 12px rgba(120,255,160,0.18);
}

/* control card */
.form-card {
    width: 92%;
    margin: auto;
    background: rgba(255,255,255,0.05);
    padding: 22px;
    border-radius: 22px;
    border: 1px solid rgba(120,255,160,0.12);
    margin-bottom: 24px;
}

/* prob card */
.prob-box {
    width: 92%;
    margin: auto;
    background: rgba(255,255,255,0.05);
    padding: 22px;
    border-radius: 20px;
    margin-top: 20px;
    border: 1px solid rgba(120,255,160,0.12);
}

.result-box {
    width: 92%;
    margin: 18px auto 0 auto;
    background: linear-gradient(90deg, rgba(88,255,144,0.13), rgba(255,255,255,0.04));
    padding: 16px 18px;
    border-radius: 16px;
    border-left: 4px solid #78ff9b;
    font-size: 18px;
    font-weight: 700;
}

/* labels */
label {
    color: #d8ffe3 !important;
    font-weight: 700 !important;
}

/* button */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #1f9d55, #46d369);
    color: white;
    border-radius: 14px;
    padding: 12px 24px;
    font-weight: bold;
    border: none;
    font-size: 16px;
}

.stButton>button:hover {
    box-shadow: 0 0 18px rgba(70,211,105,0.45);
    border: none;
}

/* progress */
div[data-testid="stProgress"] > div > div > div > div {
    background: linear-gradient(90deg, #22c55e, #86efac) !important;
}

/* messages */
.stAlert {
    border-radius: 14px;
}

/* footer buttons */
.next-wrap {
    display:flex;
    justify-content:space-between;
    gap:12px;
    margin-top:30px;
}

.next-btn {
    display:inline-block;
    width:48%;
    text-align:center;
    text-decoration:none;
    padding:12px 16px;
    border-radius:12px;
    font-weight:bold;
    color:white !important;
    background:linear-gradient(90deg,#166534,#22c55e);
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div style="display:flex; flex-wrap:wrap; gap:10px; justify-content:center; margin-bottom:20px;">
    <a href="/" target="_self" style="text-decoration:none; padding:10px 14px; border-radius:12px; font-weight:bold; color:white; background:linear-gradient(90deg,#14532d,#22c55e);">🏠 Home</a>
    <a href="/Machine_Learning_Explanation" target="_self" style="text-decoration:none; padding:10px 14px; border-radius:12px; font-weight:bold; color:white; background:linear-gradient(90deg,#14532d,#22c55e);">📘 ML Explain</a>
    <a href="/Neural_Network_Explanation" target="_self" style="text-decoration:none; padding:10px 14px; border-radius:12px; font-weight:bold; color:white; background:linear-gradient(90deg,#14532d,#22c55e);">🧠 NN Explain</a>
    <a href="/Test_ML" target="_self" style="text-decoration:none; padding:10px 14px; border-radius:12px; font-weight:bold; color:white; background:linear-gradient(90deg,#14532d,#22c55e);">⚽ Test ML</a>
    <a href="/Test_NN" target="_self" style="text-decoration:none; padding:10px 14px; border-radius:12px; font-weight:bold; color:white; background:linear-gradient(90deg,#14532d,#22c55e);">🖼️ Test NN</a>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="hero-title">EURO MATCH AI</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Football Match Prediction • Ensemble Learning </div>', unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model = joblib.load("models/ensemble_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    return model, scaler

model, scaler = load_model()

teams = {
    "France": {"flag": "🇫🇷", "rating": 90, "form": 85, "goals": 2.10},
    "Germany": {"flag": "🇩🇪", "rating": 88, "form": 82, "goals": 1.90},
    "Spain": {"flag": "🇪🇸", "rating": 87, "form": 80, "goals": 1.80},
    "England": {"flag": "🏴", "rating": 89, "form": 84, "goals": 2.00},
    "Italy": {"flag": "🇮🇹", "rating": 86, "form": 78, "goals": 1.70},
    "Portugal": {"flag": "🇵🇹", "rating": 88, "form": 83, "goals": 1.95},
    "Netherlands": {"flag": "🇳🇱", "rating": 85, "form": 79, "goals": 1.75},
    "Belgium": {"flag": "🇧🇪", "rating": 87, "form": 81, "goals": 1.85},
    "Croatia": {"flag": "🇭🇷", "rating": 84, "form": 77, "goals": 1.60},
    "Denmark": {"flag": "🇩🇰", "rating": 82, "form": 75, "goals": 1.50},
    "Switzerland": {"flag": "🇨🇭", "rating": 83, "form": 76, "goals": 1.55},
    "Austria": {"flag": "🇦🇹", "rating": 80, "form": 73, "goals": 1.45},
    "Turkey": {"flag": "🇹🇷", "rating": 81, "form": 74, "goals": 1.50},
    "Poland": {"flag": "🇵🇱", "rating": 78, "form": 70, "goals": 1.30},
    "Czech Republic": {"flag": "🇨🇿", "rating": 79, "form": 71, "goals": 1.35},
    "Serbia": {"flag": "🇷🇸", "rating": 80, "form": 72, "goals": 1.40},
}

team_names = list(teams.keys())

def render_scoreboard(home_team, away_team, score_text="VS"):
    home_flag = teams[home_team]["flag"]
    away_flag = teams[away_team]["flag"]

    st.markdown(
        f"""
        <div class="score-hero">
            <div class="match-label">Match Preview</div>
            <div class="match-row">
                <div class="team-box">
                    <div class="team-flag">{home_flag}</div>
                    <div class="team-name">{home_team}</div>
                </div>
                <div class="vs-box">
                    <div class="vs-text">HOME VS AWAY</div>
                    <div class="score-line">{score_text}</div>
                </div>
                <div class="team-box">
                    <div class="team-flag">{away_flag}</div>
                    <div class="team-name">{away_team}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with st.container():
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        home = st.selectbox("Home Team", team_names, index=0)
    with col2:
        away = st.selectbox("Away Team", team_names, index=1)

    st.markdown('</div>', unsafe_allow_html=True)

render_scoreboard(home, away, "VS")

if home == away:
    st.error("Please select two different teams. You cannot predict a match with the same team on both sides.")
else:
    if st.button("Predict Match"):
        with st.spinner("Analyzing match data..."):
            time.sleep(1)

        hr = teams[home]["rating"]
        hf = teams[home]["form"]
        hg = teams[home]["goals"]

        ar = teams[away]["rating"]
        af = teams[away]["form"]
        ag = teams[away]["goals"]

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

        render_scoreboard(home, away, f"{home_goals} - {away_goals}")

        if home_goals > away_goals:
            result_text = f"Predicted Winner: {teams[home]['flag']} {home}"
        elif away_goals > home_goals:
            result_text = f"Predicted Winner: {teams[away]['flag']} {away}"
        else:
            result_text = "Predicted Result: Draw"

        st.markdown(
            f'<div class="result-box">{result_text}</div>',
            unsafe_allow_html=True
        )

        st.markdown('<div class="prob-box">', unsafe_allow_html=True)
        st.subheader("Match Probabilities")

        labels = ["🏠 Home Win", "🤝 Draw", "✈️ Away Win"]

        for i in range(3):
            percentage = prob[i] * 100
            st.write(f"{labels[i]}: {percentage:.1f}%")
            st.progress(int(percentage))

        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="next-wrap">
    <a class="next-btn" href="/Machine_Learning_Explanation" target="_self">⬅️ Back: ML Explain</a>
    <a class="next-btn" href="/Test_NN" target="_self">Next: Test NN ➡️</a>
</div>
""", unsafe_allow_html=True)