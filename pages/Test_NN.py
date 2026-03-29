import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import time

st.set_page_config(
    page_title="Weapon Detection AI",
    layout="centered"
)

st.markdown("""
<style>
header {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden;}
[data-testid="stDecoration"] {visibility: hidden;}
[data-testid="stStatusWidget"] {visibility: hidden;}

.block-container {
    padding-top: 0.6rem !important;
    max-width: 1000px;
}

/* Background */
.stApp {
    background:
        radial-gradient(circle at top, rgba(120, 0, 30, 0.28), transparent 32%),
        linear-gradient(180deg, #0c0c12 0%, #15111b 45%, #0c0b10 100%);
    color: #f4f4f8;
    font-family: 'Segoe UI', sans-serif;
}

/* Navigation */
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
    background:linear-gradient(90deg,#7f1d1d,#dc2626);
    border:1px solid rgba(255,255,255,0.08);
    box-shadow:0 0 10px rgba(220,38,38,0.18);
}

.nav-btn:hover {
    box-shadow:0 0 18px rgba(239,68,68,0.38);
}

/* Hero */
.hero-title {
    text-align: center;
    font-size: 48px;
    font-weight: 900;
    letter-spacing: 2px;
    margin-top: 12px;
    margin-bottom: 6px;
    color: white;
    text-shadow: 0 0 20px rgba(255, 80, 80, 0.22);
}

.hero-sub {
    text-align: center;
    font-size: 14px;
    opacity: 0.82;
    margin-bottom: 28px;
    color: #f8d7da;
}

/* Info banner */
.top-info {
    width: 94%;
    margin: 0 auto 18px auto;
    padding: 12px 16px;
    border-radius: 14px;
    text-align: center;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    color: #f9d7db;
}

/* Cards */
.main-card {
    width: 94%;
    margin: 0 auto 22px auto;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 22px;
    backdrop-filter: blur(14px);
}

.section-title {
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 14px;
    color: #fff1f2;
}

/* Upload area */
section[data-testid="stFileUploader"] {
    width: 100%;
    margin: auto;
    background: rgba(220, 38, 38, 0.06);
    border-radius: 16px;
    padding: 14px;
    border: 1px solid rgba(239, 68, 68, 0.16);
}

/* Image preview */
.preview-frame {
    width: 94%;
    margin: 0 auto 22px auto;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    padding: 18px;
}

.preview-title {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 14px;
    text-align: center;
    color: #ffe4e6;
}

/* Result banner */
.result-banner {
    width: 94%;
    margin: 0 auto 22px auto;
    padding: 28px 20px;
    border-radius: 24px;
    text-align: center;
    font-size: 30px;
    font-weight: 900;
    backdrop-filter: blur(16px);
}

.waiting {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    color: #f3f4f6;
}

.weapon {
    background: linear-gradient(135deg, #7f1d1d, #dc2626);
    color: white;
    box-shadow: 0 0 24px rgba(239,68,68,0.28);
}

.safe {
    background: linear-gradient(135deg, #14532d, #16a34a);
    color: white;
    box-shadow: 0 0 24px rgba(34,197,94,0.24);
}

/* Summary card */
.summary-card {
    width: 94%;
    margin: 0 auto 22px auto;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    padding: 20px;
}

.summary-title {
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 10px;
    color: #fff1f2;
}

/* Confidence */
.conf-label {
    font-size: 16px;
    font-weight: 700;
    margin-top: 8px;
    margin-bottom: 8px;
    color: #ffe4e6;
}

div[data-testid="stProgress"] > div > div > div > div {
    background: linear-gradient(90deg, #ef4444, #f87171) !important;
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #991b1b, #ef4444);
    color: white;
    border-radius: 14px;
    padding: 11px 24px;
    font-weight: bold;
    border: none;
    font-size: 16px;
}

.stButton>button:hover {
    box-shadow: 0 0 18px rgba(239,68,68,0.35);
}

/* Bottom links */
.next-wrap {
    display:flex;
    justify-content:space-between;
    gap:12px;
    margin-top:26px;
    width:94%;
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
    background:linear-gradient(90deg,#7f1d1d,#ef4444);
}

/* Make images prettier */
img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    border-radius: 14px;
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

st.markdown('<div class="hero-title">WEAPON DETECTION AI</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Image Classification • Deep Learning • MobileNetV2</div>', unsafe_allow_html=True)
st.markdown('<div class="top-info">Upload an image to check whether the system detects a weapon.</div>', unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("models/weapon_model.h5")

model = load_model()

result_placeholder = st.empty()
result_placeholder.markdown(
    '<div class="result-banner waiting">System Ready · Waiting for Image</div>',
    unsafe_allow_html=True
)

def preprocess(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))
    img_array = np.array(image)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Upload Image</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.markdown('<div class="preview-frame">', unsafe_allow_html=True)
    st.markdown('<div class="preview-title">Image Preview</div>', unsafe_allow_html=True)
    st.image(image, use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Analyze Image"):
        with st.spinner("Analyzing image..."):
            time.sleep(1)
            img = preprocess(image)
            prediction = model.predict(img, verbose=0)[0][0]

        if prediction > 0.5:
            result_placeholder.markdown(
                '<div class="result-banner weapon">🚨 WEAPON DETECTED</div>',
                unsafe_allow_html=True
            )
            confidence = float(prediction)
            label_text = "Weapon"
            detail_text = "The system predicts that the uploaded image contains a weapon-like object."
        else:
            result_placeholder.markdown(
                '<div class="result-banner safe">✅ SAFE · NO WEAPON DETECTED</div>',
                unsafe_allow_html=True
            )
            confidence = float(1 - prediction)
            label_text = "No Weapon"
            detail_text = "The system predicts that the uploaded image does not contain a weapon."

        st.markdown('<div class="summary-card">', unsafe_allow_html=True)
        st.markdown('<div class="summary-title">Detection Result</div>', unsafe_allow_html=True)
        st.write(f"**Predicted Class:** {label_text}")
        st.write(detail_text)
        st.markdown('<div class="conf-label">Confidence Score</div>', unsafe_allow_html=True)
        st.progress(int(confidence * 100))
        st.write(f"**Confidence:** {confidence * 100:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="summary-card">', unsafe_allow_html=True)
    st.markdown('<div class="summary-title">How to Use</div>', unsafe_allow_html=True)
    st.write("1. Upload a JPG, JPEG, or PNG image.")
    st.write("2. Click **Analyze Image**.")
    st.write("3. The system will show whether a weapon is detected and the confidence score.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="next-wrap">
    <a class="next-btn" href="/Neural_Network_Explanation" target="_self">⬅️ Back: NN Explain</a>
    <a class="next-btn" href="/" target="_self">🏠 Back to Home</a>
</div>
""", unsafe_allow_html=True)