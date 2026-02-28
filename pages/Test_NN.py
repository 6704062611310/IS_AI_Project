import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import time

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Weapon Detection AI",
    layout="centered"
)

# ======================
# STYLE
# ======================
st.markdown("""
<style>

/* Hide Streamlit default header */
header {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden;}
[data-testid="stDecoration"] {visibility: hidden;}
[data-testid="stStatusWidget"] {visibility: hidden;}

/* Reduce top spacing */
.block-container {
    padding-top: 0.5rem !important;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f0014, #1a0024, #2a0036);
    background-size: 400% 400%;
    animation: gradientBG 18s ease infinite;
    color: #f2e6ff;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* HERO TITLE */
.hero-title {
    text-align: center;
    font-size: 46px;
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
    opacity: 0.5;
    letter-spacing: 2px;
    margin-bottom: 35px;
}

/* Result Banner */
.result-banner {
    width: 65%;
    margin: 0 auto 35px auto;
    padding: 45px;
    border-radius: 22px;
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    backdrop-filter: blur(20px);
}

/* Waiting */
.waiting {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,105,180,0.2);
}

/* Weapon */
.weapon {
    background: linear-gradient(135deg, #99004d, #cc0066);
    color: white;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% { box-shadow: 0 0 10px #ff0066; }
    50% { box-shadow: 0 0 35px #ff3399; }
    100% { box-shadow: 0 0 10px #ff0066; }
}

/* Safe */
.safe {
    background: linear-gradient(135deg, #330033, #660066);
    color: white;
    animation: softGlow 2s infinite alternate;
}

@keyframes softGlow {
    from { box-shadow: 0 0 10px #cc66ff; }
    to { box-shadow: 0 0 25px #ff99ff; }
}

/* Upload styling */
section[data-testid="stFileUploader"] {
    width: 65%;
    margin: auto;
    background: rgba(255, 105, 180, 0.05);
    border-radius: 15px;
    padding: 15px;
    border: 1px solid rgba(255, 105, 180, 0.15);
}

/* Center image */
img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

/* Progress bar */
div[data-testid="stProgress"] > div > div > div > div {
    background: linear-gradient(90deg, #cc0066, #ff66cc) !important;
}

</style>
""", unsafe_allow_html=True)

# ======================
# HERO TITLE
# ======================
st.markdown('<div class="hero-title">WEAPON DETECTION AI</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Deep Learning • MobileNetV2 </div>', unsafe_allow_html=True)

# ======================
# LOAD MODEL
# ======================
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("models/weapon_model.h5")

model = load_model()

# ======================
# RESULT PLACEHOLDER
# ======================
result_placeholder = st.empty()
result_placeholder.markdown(
    '<div class="result-banner waiting">System Ready • Waiting for Image</div>',
    unsafe_allow_html=True
)

# ======================
# PREPROCESS
# ======================
def preprocess(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))
    img_array = np.array(image)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# ======================
# FILE UPLOAD
# ======================
uploaded_file = st.file_uploader("Upload Image", type=["jpg","jpeg","png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)

    with st.spinner("Analyzing image..."):
        time.sleep(1)
        img = preprocess(image)
        prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        result_placeholder.markdown(
            '<div class="result-banner weapon">🚨 WEAPON DETECTED</div>',
            unsafe_allow_html=True
        )
        confidence = prediction
    else:
        result_placeholder.markdown(
            '<div class="result-banner safe">SAFE • NO WEAPON DETECTED</div>',
            unsafe_allow_html=True
        )
        confidence = 1 - prediction

    st.progress(int(confidence * 100))
    st.write(f"Confidence: {confidence*100:.2f}%")

st.markdown("---")
st.markdown(
    "<div style='text-align:center; opacity:0.4;'>• Powered by TensorFlow</div>",
    unsafe_allow_html=True
)