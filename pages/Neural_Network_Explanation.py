import streamlit as st

st.set_page_config(page_title="Neural Network Explanation", layout="centered")

st.markdown("""
<style>
header {visibility:hidden;}
[data-testid="stToolbar"] {visibility:hidden;}
.block-container {padding-top: 0.5rem !important;}

.stApp {
    background: linear-gradient(135deg, #0f0014, #1a0024, #2a0036);
    color: #f2e6ff;
}

.hero-title {
    text-align:center;
    font-size:44px;
    font-weight:900;
    margin-top:20px;
    margin-bottom:30px;
    color:white;
}

.section {
    background:rgba(255,255,255,0.05);
    padding:35px;
    border-radius:20px;
    margin-bottom:30px;
    border:1px solid rgba(255,105,180,0.25);
}

h1, h2, h3 {
    color:white !important;
    text-shadow:0 0 10px rgba(255,105,180,0.6);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero-title">Neural Network Model Development</div>', unsafe_allow_html=True)

# 1 Problem
st.markdown("""
<div class="section">

## 1. Problem Definition

This project implements a deep learning model to detect weapons in images.

It is a **Binary Image Classification problem**:

- 0 = No Weapon  
- 1 = Weapon  

The system aims to identify dangerous objects in visual data.

</div>
""", unsafe_allow_html=True)

# 2 Dataset
st.markdown("""
<div class="section">

## 2. Dataset Sources

Weapon images were collected from multiple Kaggle datasets:

- Weapons in Images & Segmented Videos  
- Weapon Detection Test Dataset  
- CCTV Weapon Dataset  

These datasets contain CCTV images, real-world scenes,
and different lighting conditions to improve generalization.

</div>
""", unsafe_allow_html=True)

# 3 Data Preparation
st.markdown("""
<div class="section">

## 3. Data Preparation

Images were:

1. Resized to 224x224  
2. Converted to RGB  
3. Normalized using MobileNetV2 preprocessing  
4. Split into training and validation sets  

This ensures consistent input size for CNN processing.

</div>
""", unsafe_allow_html=True)

# 4 CNN Theory
st.markdown("""
<div class="section">

## 4. Convolutional Neural Network Theory

CNNs extract visual features using:

- Convolution layers (feature extraction)  
- Pooling layers (dimension reduction)  
- Fully connected layers (classification)  

CNNs are highly effective for image recognition tasks.

</div>
""", unsafe_allow_html=True)

# 5 Transfer Learning
st.markdown("""
<div class="section">

## 5. Transfer Learning

MobileNetV2 pretrained on ImageNet was used.

Transfer Learning allows reuse of learned visual features,
reducing training time and improving performance.

Architecture:

Input → MobileNetV2 → Global Average Pooling → Dense (Sigmoid)

</div>
""", unsafe_allow_html=True)

# 6 Training
st.markdown("""
<div class="section">

## 6. Training Process

Configuration:

- Loss: Binary Cross-Entropy  
- Optimizer: Adam  
- Activation: Sigmoid  

Fine-tuning improved classification accuracy.

</div>
""", unsafe_allow_html=True)

# 7 Evaluation
st.markdown("""
<div class="section">

## 7. Evaluation Metrics

Model performance evaluated using:

- Accuracy  
- Validation Accuracy  
- Loss  

Results show strong classification performance for prototype deployment.

</div>
""", unsafe_allow_html=True)

# 8 Limitations
st.markdown("""
<div class="section">

## 8. Limitations

- Not an object detection system  
- Dataset diversity may be limited  
- Prototype-level system  

</div>
""", unsafe_allow_html=True)

# 9 References
st.markdown("""
<div class="section">

## 9. References

Kaggle Weapon Datasets  
MobileNetV2 Paper (Sandler et al., 2018)  
TensorFlow & Keras Documentation  

</div>
""", unsafe_allow_html=True)