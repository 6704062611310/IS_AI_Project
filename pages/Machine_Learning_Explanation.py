import streamlit as st

st.set_page_config(page_title="Machine Learning Explanation", layout="centered")

st.markdown("""
<style>
header {visibility:hidden;}
[data-testid="stToolbar"] {visibility:hidden;}
.block-container {padding-top: 0.6rem !important; max-width: 1100px;}

.stApp {
    background:
        radial-gradient(circle at top, rgba(34,197,94,0.18), transparent 28%),
        linear-gradient(180deg, #07110a 0%, #0b1b12 45%, #071009 100%);
    color: #effff2;
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
    background:linear-gradient(90deg,#166534,#22c55e);
    border:1px solid rgba(255,255,255,0.08);
}

.hero-box {
    width: 96%;
    margin: 0 auto 24px auto;
    padding: 30px 22px;
    border-radius: 28px;
    text-align: center;
    background: linear-gradient(180deg, rgba(255,255,255,0.07), rgba(255,255,255,0.04));
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(14px);
}

.hero-title {
    font-size: 46px;
    font-weight: 900;
    color: white;
    margin-bottom: 8px;
}

.hero-sub {
    font-size: 15px;
    opacity: 0.82;
    color: #d9ffe3;
}

.section {
    width: 96%;
    margin: 0 auto 20px auto;
    background: rgba(255,255,255,0.05);
    padding: 24px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.08);
}

.section-title {
    font-size: 24px;
    font-weight: 900;
    margin-bottom: 12px;
    color: white;
}

.highlight-grid {
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap:14px;
    margin-top: 14px;
}

.highlight-box {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 16px;
}

.highlight-title {
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 6px;
}

.next-wrap {
    display:flex;
    justify-content:space-between;
    gap:12px;
    margin-top:26px;
    width:96%;
    margin-left:auto;
    margin-right:auto;
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
    <div class="hero-title">Machine Learning Model Development</div>
    <div class="hero-sub">Football Match Prediction using Ensemble Learning</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">⚽ 1. Problem Definition</div>
    This module is designed to predict the outcome of a football match using structured numerical data.
    <br><br>
    It is a <b>multi-class classification problem</b> with three possible outputs:
    <br>
    • 0 = Home Win<br>
    • 1 = Draw<br>
    • 2 = Away Win
    <br><br>
    The objective is to identify patterns from team performance indicators and use them to estimate match outcomes.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">📂 2. Dataset Source and Structure</div>
    The dataset used in this project is a <b>synthetic dataset</b> generated for educational purposes with the assistance of ChatGPT.
    <br><br>
    Each row represents one football match and contains statistical features from both teams.
    <br><br>
    <b>Feature Columns</b><br>
    • Home Rating<br>
    • Away Rating<br>
    • Home Form<br>
    • Away Form<br>
    • Home Average Goals<br>
    • Away Average Goals
    <br><br>
    <b>Target Column</b><br>
    • Result (Home Win / Draw / Away Win)
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">🧹 3. Data Preparation</div>
    Before training the model, the dataset was processed through several steps:
    <br><br>
    • Separating input features (X) and target labels (y)<br>
    • Applying <b>StandardScaler</b> for normalization<br>
    • Splitting the data into training and testing sets
    <br><br>
    These steps help the model learn more effectively and reduce bias caused by different feature scales.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">🤖 4. Algorithms Used</div>
    This project combines multiple algorithms using an <b>Ensemble Learning</b> approach.
    <div class="highlight-grid">
        <div class="highlight-box">
            <div class="highlight-title">Logistic Regression</div>
            A linear model that estimates probabilities for each class.
        </div>
        <div class="highlight-box">
            <div class="highlight-title">Random Forest</div>
            A tree-based ensemble model that improves stability by averaging multiple decision trees.
        </div>
        <div class="highlight-box">
            <div class="highlight-title">Gradient Boosting</div>
            A boosting technique that builds trees sequentially to reduce previous prediction errors.
        </div>
        <div class="highlight-box">
            <div class="highlight-title">Voting Strategy</div>
            Combines outputs from multiple models to improve prediction robustness.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">🛠️ 5. Development Process</div>
    The machine learning workflow followed these stages:
    <br><br>
    1. Data preprocessing and scaling<br>
    2. Training multiple classification models<br>
    3. Combining models using ensemble learning<br>
    4. Testing performance on unseen data<br>
    5. Preparing the trained model for deployment in Streamlit
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">📊 6. Evaluation Metrics</div>
    To assess model performance, several metrics were considered:
    <br><br>
    • Accuracy<br>
    • Precision<br>
    • Recall<br>
    • F1-score<br>
    • Confusion Matrix
    <br><br>
    These metrics provide a balanced understanding of how well the model performs across all classes.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">✅ 7. Strengths of This Model</div>
    • Easy to explain and demonstrate in an academic setting<br>
    • Works well with structured numerical data<br>
    • Ensemble approach improves prediction stability<br>
    • Suitable for showing the difference between ML and DL in one project
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">⚠️ 8. Limitations</div>
    • The dataset is synthetic, not from real competition databases<br>
    • External factors such as injuries, weather, or home crowd are not included<br>
    • The model is intended as an educational prototype rather than a production sports analytics system
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">📚 9. References</div>
    • Scikit-learn Documentation: https://scikit-learn.org/stable/<br>
    • Ensemble Methods in Machine Learning: https://link.springer.com/article/10.1007/s10462-011-9270-2<br>
    • Synthetic dataset generated with the assistance of ChatGPT (OpenAI)<br>
    • This project is developed for educational purposes based on publicly available resources.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="next-wrap">
    <a class="next-btn" href="/" target="_self">⬅️ Back to Home</a>
    <a class="next-btn" href="/Test_ML" target="_self">Next: Test ML ➡️</a>
</div>
""", unsafe_allow_html=True)