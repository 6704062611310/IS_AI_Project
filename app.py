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
.block-container {padding-top: 0.6rem !important; max-width: 1100px;}

.stApp {
    background:
        radial-gradient(circle at top, rgba(170, 80, 255, 0.18), transparent 30%),
        linear-gradient(180deg, #0b0712 0%, #130b1d 45%, #0a0611 100%);
    color: #f5eeff;
    font-family: 'Segoe UI', sans-serif;
}

.nav-wrap {
    display:flex;
    flex-wrap:wrap;
    gap:10px;
    justify-content:center;
    margin: 10px 0 22px 0;
}

.nav-btn {
    display:inline-block;
    text-decoration:none;
    padding:10px 14px;
    border-radius:12px;
    font-weight:bold;
    color:white !important;
    background:linear-gradient(90deg,#7c3aed,#ec4899);
    border:1px solid rgba(255,255,255,0.08);
    box-shadow:0 0 12px rgba(168,85,247,0.18);
}

.nav-btn:hover {
    box-shadow:0 0 18px rgba(236,72,153,0.28);
}

.hero-box {
    width: 96%;
    margin: 0 auto 24px auto;
    padding: 34px 22px;
    border-radius: 28px;
    text-align: center;
    background: linear-gradient(180deg, rgba(255,255,255,0.07), rgba(255,255,255,0.04));
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(14px);
}

.hero-title {
    text-align:center;
    font-size:52px;
    font-weight:900;
    margin-bottom:10px;
    color:white;
    text-shadow: 0 0 18px rgba(236,72,153,0.20);
}

.hero-sub {
    text-align:center;
    font-size:17px;
    opacity:0.86;
    margin-bottom:10px;
    color:#f3d9ff;
}

.hero-mini {
    text-align:center;
    font-size:14px;
    opacity:0.72;
    color:#e9d5ff;
}

.card {
    width: 96%;
    margin: 0 auto 22px auto;
    background: rgba(255,255,255,0.05);
    padding: 26px;
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
}

.section-title {
    font-size: 24px;
    font-weight: 900;
    margin-bottom: 12px;
    color: #fff;
}

.feature-grid {
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap:16px;
    margin-top: 16px;
}

.feature-box {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 18px;
}

.feature-title {
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 8px;
    color: #fdf4ff;
}

.quick-links {
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap:14px;
    margin-top: 16px;
}

.quick-link {
    display:block;
    text-decoration:none;
    padding:18px;
    border-radius:18px;
    color:white !important;
    background: linear-gradient(135deg, rgba(124,58,237,0.85), rgba(236,72,153,0.80));
    font-weight: 700;
    border: 1px solid rgba(255,255,255,0.10);
}

.quick-link small {
    display:block;
    margin-top:8px;
    font-weight:400;
    opacity:0.9;
}

.footer-note {
    text-align:center;
    opacity:0.45;
    margin-top:24px;
    margin-bottom:10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="nav-wrap">
    <a class="nav-btn" href="/" target="_self">🏠 Home</a>
    <a class="nav-btn" href="/Machine_Learning_Explanation" target="_self">⚽ ML Explain</a>
    <a class="nav-btn" href="/Neural_Network_Explanation" target="_self">🧠 NN Explain</a>
    <a class="nav-btn" href="/Test_ML" target="_self">⚽ Test ML</a>
    <a class="nav-btn" href="/Test_NN" target="_self">🔫 Test NN</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-box">
    <div class="hero-title">AI Prediction System</div>
    <div class="hero-sub">IS2568 Artificial Intelligence Project</div>
    <div class="hero-mini">A web-based AI application combining Machine Learning and Deep Learning in one system</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="section-title">📌 Project Overview</div>
    This project presents two different Artificial Intelligence approaches in one application:
    <br><br>
    <b>1. Football Match Prediction</b> using Machine Learning and Ensemble techniques<br>
    <b>2. Weapon Detection</b> using Deep Learning with MobileNetV2
    <br><br>
    The goal is to demonstrate how AI can be applied to both structured numerical data and image-based classification tasks.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="section-title">✨ Main Features</div>
    <div class="feature-grid">
        <div class="feature-box">
            <div class="feature-title">⚽ Football Prediction</div>
            Predict match outcomes from team statistics such as rating, form, and average goals.
        </div>
        <div class="feature-box">
            <div class="feature-title">🧠 Neural Network Detection</div>
            Analyze uploaded images and classify whether a weapon is present.
        </div>
        <div class="feature-box">
            <div class="feature-title">📊 AI Explanation Pages</div>
            Learn about dataset preparation, model training, and evaluation process.
        </div>
        <div class="feature-box">
            <div class="feature-title">📱 Friendly UI</div>
            Designed for both desktop and mobile usage with quick navigation buttons.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="section-title">🚀 Explore the Project</div>
    <div class="quick-links">
        <a class="quick-link" href="/Machine_Learning_Explanation" target="_self">
            ⚽ Machine Learning Explanation
            <small>Read about the football prediction model, dataset, algorithms, and evaluation.</small>
        </a>
        <a class="quick-link" href="/Neural_Network_Explanation" target="_self">
            🧠 Neural Network Explanation
            <small>Read about the image classification model, transfer learning, and training process.</small>
        </a>
        <a class="quick-link" href="/Test_ML" target="_self">
            ⚽ Test Football Prediction
            <small>Choose two teams and let the system predict the match result.</small>
        </a>
        <a class="quick-link" href="/Test_NN" target="_self">
            🔫 Test Weapon Detection
            <small>Upload an image and let the AI classify the result.</small>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="section-title">🎯 Project Objective</div>
    This system was developed to demonstrate the practical use of Artificial Intelligence techniques in real applications.
    It highlights the difference between:
    <br><br>
    • <b>Machine Learning</b> for numerical/tabular prediction problems<br>
    • <b>Deep Learning</b> for image recognition and classification tasks
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer-note">
Developed for IS2568 – Artificial Intelligence Project Demonstration
</div>
""", unsafe_allow_html=True)