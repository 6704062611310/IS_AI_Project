import streamlit as st

st.set_page_config(page_title="Neural Network Explanation", layout="centered")

st.markdown("""
<style>
header {visibility:hidden;}
[data-testid="stToolbar"] {visibility:hidden;}
.block-container {padding-top: 0.6rem !important; max-width: 1100px;}

.stApp {
    background:
        radial-gradient(circle at top, rgba(239,68,68,0.18), transparent 28%),
        linear-gradient(180deg, #120708 0%, #1c0d0f 45%, #100607 100%);
    color: #fff1f2;
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
    background:linear-gradient(90deg,#991b1b,#ef4444);
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
    color: #fecdd3;
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
    background:linear-gradient(90deg,#991b1b,#ef4444);
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
    <div class="hero-title">Neural Network Model Development</div>
    <div class="hero-sub">Weapon Detection using Deep Learning and MobileNetV2</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">🔫 1. Problem Definition</div>
    This module performs <b>binary image classification</b> to determine whether an uploaded image contains a weapon.
    <br><br>
    The model outputs:
    <br>
    • 0 = No Weapon<br>
    • 1 = Weapon
    <br><br>
    The purpose is to demonstrate how deep learning can be used for visual recognition tasks in safety-related applications.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">🖼️ 2. Dataset Sources</div>
    The training data was collected from multiple weapon-related image datasets.
    <br><br>
    Example sources include:
    <br>
    • CCTV weapon image sets<br>
    • Kaggle image classification datasets<br>
    • Real-world scene collections with varied lighting and backgrounds
    <br><br>
    Using multiple sources helps improve generalization across different image styles.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">🧹 3. Data Preparation</div>
    Before training, the image data was preprocessed through these steps:
    <br><br>
    • Resizing images to 224 × 224 pixels<br>
    • Converting all images to RGB format<br>
    • Applying MobileNetV2 preprocessing<br>
    • Splitting the data into training and validation sets
    <br><br>
    These steps ensure consistent input size and help the neural network learn effectively.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">🧠 4. CNN and Transfer Learning</div>
    Instead of training a deep network completely from scratch, this project uses <b>Transfer Learning</b>.
    <br><br>
    The base model is <b>MobileNetV2</b>, which is lightweight, efficient, and suitable for deployment.
    <div class="highlight-grid">
        <div class="highlight-box">
            <div class="highlight-title">Convolution Layers</div>
            Extract edges, shapes, and image patterns.
        </div>
        <div class="highlight-box">
            <div class="highlight-title">Pooling Layers</div>
            Reduce feature map size and keep important information.
        </div>
        <div class="highlight-box">
            <div class="highlight-title">Transfer Learning</div>
            Reuses knowledge learned from large-scale image datasets.
        </div>
        <div class="highlight-box">
            <div class="highlight-title">Fine-Tuning</div>
            Adjusts pretrained layers to better match the weapon detection task.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">🏗️ 5. Model Architecture</div>
    The overall architecture can be summarized as:
    <br><br>
    <b>Input Image → MobileNetV2 Base → Global Average Pooling → Dense Output Layer</b>
    <br><br>
    The final layer uses a sigmoid activation function because this is a binary classification problem.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">⚙️ 6. Training Process</div>
    During training, the following configuration was used:
    <br><br>
    • Loss Function: Binary Cross-Entropy<br>
    • Optimizer: Adam<br>
    • Output Activation: Sigmoid
    <br><br>
    Fine-tuning helped improve performance by adapting the pretrained model to the project dataset.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">📊 7. Evaluation</div>
    Model performance can be evaluated using:
    <br><br>
    • Accuracy<br>
    • Validation Accuracy<br>
    • Loss
    <br><br>
    These metrics show how well the network distinguishes between images with and without weapons.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">✅ 8. Strengths of This Model</div>
    • Suitable for image-based classification problems<br>
    • Efficient enough for web demonstration<br>
    • More realistic for computer vision compared with traditional ML methods<br>
    • Good example of transfer learning in practice
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">⚠️ 9. Limitations</div>
    • This is a classification model, not a full object detection model<br>
    • The dataset may still be limited in diversity<br>
    • Real-world deployment would require larger and more carefully validated datasets
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-title">📚 10. References</div>
    • TensorFlow Documentation: https://www.tensorflow.org/<br>
    • MobileNetV2 Paper: https://arxiv.org/abs/1801.04381<br>
    • Kaggle Datasets: https://www.kaggle.com/<br>
    • This project is developed for educational purposes based on publicly available resources.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="next-wrap">
    <a class="next-btn" href="/" target="_self">⬅️ Back to Home</a>
    <a class="next-btn" href="/Test_NN" target="_self">Next: Test NN ➡️</a>
</div>
""", unsafe_allow_html=True)