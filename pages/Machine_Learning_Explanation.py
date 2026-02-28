import streamlit as st

st.set_page_config(page_title="Machine Learning Explanation", layout="centered")

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

st.markdown('<div class="hero-title">Machine Learning Model Development</div>', unsafe_allow_html=True)

# 1 Problem
st.markdown("""
<div class="section">

## 1. Problem Definition

This project aims to predict football match outcomes using structured numerical data.

It is a **Multi-class Classification problem** with three possible outputs:

- 0 = Home Win  
- 1 = Draw  
- 2 = Away Win  

The goal is to learn patterns between team statistics and match results.

</div>
""", unsafe_allow_html=True)

# 2 Dataset
st.markdown("""
<div class="section">

## 2. Dataset Source and Structure

The dataset is a **Synthetic Dataset generated with the assistance of ChatGPT**.

It was designed to simulate realistic football match statistics.

Each row represents one football match.

### Feature Columns:
1. Home Rating  
2. Away Rating  
3. Home Form  
4. Away Form  
5. Home Average Goals  
6. Away Average Goals  

### Target Column:
Result (0, 1, 2)

Synthetic data was chosen to:
- Control feature structure
- Demonstrate ML workflow clearly
- Avoid licensing issues

</div>
""", unsafe_allow_html=True)

# 3 Data Preparation
st.markdown("""
<div class="section">

## 3. Data Preparation

Before training, the following steps were performed:

1. Separate features (X) and target (y)
2. Apply StandardScaler for normalization
3. Split dataset into Training (80%) and Testing (20%)

Normalization ensures all features contribute equally to model learning.

</div>
""", unsafe_allow_html=True)

# 4 Algorithm Theory
st.markdown("""
<div class="section">

## 4. Algorithm Theory

Three algorithms were combined using an Ensemble approach:

### Logistic Regression
A linear classification model that estimates class probabilities.

### Random Forest
An ensemble of decision trees that reduces overfitting by averaging multiple trees.

### Gradient Boosting
Builds trees sequentially to correct previous errors.

Ensemble learning improves prediction stability and overall accuracy.

</div>
""", unsafe_allow_html=True)

# 5 Development Steps
st.markdown("""
<div class="section">

## 5. Model Development Process

1. Data preprocessing and scaling  
2. Model training using ensemble methods  
3. Hyperparameter tuning  
4. Cross-validation  
5. Final evaluation on test dataset  

</div>
""", unsafe_allow_html=True)

# 6 Evaluation
st.markdown("""
<div class="section">

## 6. Model Evaluation

Evaluation metrics used:

- Accuracy  
- Precision  
- Recall  
- F1-score  
- Confusion Matrix  

The model demonstrates stable performance suitable for academic demonstration.

</div>
""", unsafe_allow_html=True)

# 7 Limitations
st.markdown("""
<div class="section">

## 7. Limitations

- Dataset is synthetic, not real match data  
- External match factors are not included  
- Designed for educational purposes  

</div>
""", unsafe_allow_html=True)

# 8 References
st.markdown("""
<div class="section">

## 8. References

Synthetic dataset generated with ChatGPT (OpenAI).  
Scikit-learn Documentation.  
Ensemble Learning Concepts.

</div>
""", unsafe_allow_html=True)