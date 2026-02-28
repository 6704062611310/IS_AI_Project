import streamlit as st

st.set_page_config(
    page_title="IS2568 AI Project",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
header {visibility:hidden;}
[data-testid="stToolbar"] {visibility:hidden;}
.block-container {padding-top: 0.5rem !important;}

.stApp {
    background: linear-gradient(135deg, #0f0014, #1a0024, #2a0036);
    color: #f2e6ff;
    font-family: 'Segoe UI', sans-serif;
}

/* HERO TITLE */
.hero-title {
    text-align:center;
    font-size:48px;
    font-weight:900;
    margin-top:30px;
    margin-bottom:10px;
    color:white;
    text-shadow:
        0 0 10px rgba(255,105,180,0.6),
        0 0 25px rgba(255,105,180,0.4);
}

.hero-sub {
    text-align:center;
    font-size:16px;
    opacity:0.7;
    margin-bottom:40px;
}

/* CARD */
.card {
    background:rgba(255,255,255,0.05);
    padding:35px;
    border-radius:20px;
    margin-bottom:30px;
    border:1px solid rgba(255,105,180,0.25);
    backdrop-filter: blur(12px);
}

/* GLOW HEADERS */
h2 {
    background: linear-gradient(90deg, #ff66cc, #cc66ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow:
        0 0 12px rgba(255,105,180,0.7),
        0 0 25px rgba(255,105,180,0.4);
}

h3 {
    color: #ffd6ff !important;
    text-shadow: 0 0 10px rgba(255,105,180,0.5);
}

/* BUTTON STYLE */
.nav-btn {
    width:60%;
    padding:15px;
    margin-bottom:15px;
    border-radius:12px;
    border:none;
    font-weight:bold;
    color:white;
    background:linear-gradient(90deg,#cc0066,#ff66cc);
    cursor:pointer;
    transition:0.3s;
}

.nav-btn:hover {
    box-shadow:0 0 25px #ff66cc;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================
st.markdown('<div class="hero-title">AI Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">IS2568 Artificial Intelligence Project</div>', unsafe_allow_html=True)

# =========================
# OVERVIEW CARD
# =========================
st.markdown("""
<div class="card">

## 📌 Project Overview

This web application contains two Artificial Intelligence models:

### ⚽ Machine Learning Model  
Football Match Prediction using Ensemble Learning.

Algorithms used:
- Random Forest  
- Gradient Boosting  
- Voting Classifier  

### 🔫 Neural Network Model  
Weapon Detection using Deep Learning (MobileNetV2).

Techniques used:
- Transfer Learning  
- Fine-tuning  
- Image Classification  

</div>
""", unsafe_allow_html=True)

# =========================
# NAVIGATION BUTTONS
# =========================
st.markdown("## 🚀 Navigate to Model Pages")

st.markdown("""
<div style="text-align:center; margin-top:20px;">

<a href="/Machine_Learning_Explanation" target="_self">
<button class="nav-btn">
⚽ Go to Machine Learning Page
</button>
</a>

<a href="/Neural_Network_Explanation" target="_self">
<button class="nav-btn">
🔫 Go to Neural Network Page
</button>
</a>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<br><br>
<center style="opacity:0.4;">
Developed for IS2568 – Artificial Intelligence Project Demonstration
</center>
""", unsafe_allow_html=True)