import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Load the saved models
try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

# Set page config for a modern look
st.set_page_config(
    page_title="EarlyMed - Test Report Interpreter",
    page_icon="🩺",
    layout="wide"
)

# Custom Styles for Premium Glassy UI
def set_glassy_style():
    st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #eef2f3, #8e9eab);
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            padding: 10px 24px;
            border: none;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background: rgba(255, 255, 255, 0.4);
            transform: scale(1.05);
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .stSidebar {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        .stSelectbox>div>div {
            border-radius: 10px;
            box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
    </style>
    """, unsafe_allow_html=True)

set_glassy_style()
# Sidebar Navigation
with st.sidebar:
    st.image("https://i.postimg.cc/vHZ4bWMx/logo.png", width=150)
    selected = option_menu(
        'Test Report Interpreter',
        ['Home', 'Diabetes Prediction', 'Heart Risk Prediction', 'Parkinsons Prediction'],
        icons=['house', 'activity', 'heart', 'person'],
        default_index=0,
        styles={
            "container": {"padding": "5px", "border-radius": "10px", "background": "#ffffff33"},
            "icon": {"color": "#FFD700", "font-size": "20px"},
            "nav-link": {"color": "#ffffff", "font-size": "18px", "text-align": "left", "margin":"5px"},
            "nav-link-selected": {"background": "#FFD700", "color": "black"},
        }
    )

# Home Page
if selected == 'Home':
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://i.postimg.cc/vHZ4bWMx/logo.png", width=250)
    with col2:
        st.title("Welcome to Test Report Interpreter 🩺")
        st.subheader("Your AI-powered early disease detection tool")

    st.markdown("""
    ### 🔍 **How EarlyMed Helps You?**
    - 🏥 **Diabetes Prediction**: Identify diabetes risk using glucose levels, insulin, BMI, and more.
    - ❤️ **Heart Risk Assessment**: Detect potential heart disease risks using cholesterol levels, ECG reports, and more.
    - 🧠 **Parkinson’s Detection**: Analyze vocal biomarkers to assess Parkinson’s disease likelihood.

    🚀 **Get Started Now!** Select a test category from the sidebar and enter your medical test results.
    """)

    st.markdown("---")
    st.markdown("© 2025 EarlyMed. All rights reserved.")

# Data Visualization Section for Better Insights
st.markdown("## 📊 Health Risk Data Visualization")
visual_choice = st.selectbox("Choose Visualization Type:", ["None", "Diabetes Risk Factors", "Heart Disease Patterns", "Parkinson's Trends"])

if visual_choice == "Diabetes Risk Factors":
    st.subheader("Glucose Levels vs. BMI")
    diabetes_data = pd.DataFrame({
        "Glucose": np.random.randint(70, 180, 50),
        "BMI": np.random.uniform(18.5, 35, 50)
    })
    fig, ax = plt.subplots()
    sns.scatterplot(data=diabetes_data, x="Glucose", y="BMI", hue=diabetes_data["Glucose"], palette="coolwarm", ax=ax)
    st.pyplot(fig)

elif visual_choice == "Heart Disease Patterns":
    st.subheader("Cholesterol Levels and Heart Disease")
    heart_data = pd.DataFrame({
        "Cholesterol": np.random.randint(150, 300, 50),
        "Heart Risk": np.random.choice(["Low", "Medium", "High"], 50)
    })
    fig, ax = plt.subplots()
    sns.histplot(data=heart_data, x="Cholesterol", hue="Heart Risk", multiple="stack", palette="Reds", ax=ax)
    st.pyplot(fig)

elif visual_choice == "Parkinson's Trends":
    st.subheader("Vocal Frequency Distribution in Parkinson's")
    parkinsons_data = pd.DataFrame({
        "Frequency (Hz)": np.random.uniform(80, 250, 50)
    })
    fig, ax = plt.subplots()
    sns.kdeplot(parkinsons_data["Frequency (Hz)"], fill=True, color="purple", alpha=0.5, ax=ax)
    st.pyplot(fig)

st.markdown("---")

# 🚀 **Next Part**: Disease Prediction Pages
if selected == 'Diabetes Prediction':
    st.title("🩸 Diabetes Risk Assessment")
    
    # Input Fields in Two Columns for Better UI
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
        Glucose = st.number_input("Glucose Level (mg/dL)", min_value=0, max_value=200, value=0)
        BloodPressure = st.number_input("Blood Pressure (mmHg)", min_value=0, max_value=150, value=0)
        SkinThickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=0)
    with col2:
        Insulin = st.number_input("Insulin Level (µU/mL)", min_value=0, max_value=1000, value=0)
        BMI = st.number_input("BMI", min_value=0.0, max_value=70.0, value=0.0)
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.0)
        Age = st.number_input("Age", min_value=0, max_value=120, value=0)
    
    # Prediction Button
    if st.button("🔍 Predict Diabetes"):
        prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        result = "🔴 **Positive for Diabetes**" if prediction[0] == 1 else "🟢 **No Diabetes Detected**"
        st.success(result)
    if selected == 'Heart Risk Prediction':
    st.title("❤️ Heart Disease Risk Assessment")
    
    # Input Fields in Two Columns for Better UI
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=0)
        sex = st.radio("Sex", ["Male", "Female"])
        cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3, value=0)
        trestbps = st.number_input("Resting Blood Pressure (mmHg)", min_value=0, max_value=200, value=0)
    with col2:
        chol = st.number_input("Serum Cholesterol (mg/dL)", min_value=0, max_value=600, value=0)
        fbs = st.radio("Fasting Blood Sugar > 120 mg/dL", ["No", "Yes"])
        restecg = st.number_input("Resting ECG Results (0-2)", min_value=0, max_value=2, value=0)
    
    # Prediction Button
    if st.button("🔍 Predict Heart Risk"):
        sex_value = 1 if sex == "Male" else 0
        fbs_value = 1 if fbs == "Yes" else 0
        prediction = heart_disease_model.predict([[age, sex_value, cp, trestbps, chol, fbs_value, restecg]])
        result = "🔴 **High Risk of Heart Disease**" if prediction[0] == 1 else "🟢 **Low Risk of Heart Disease**"
        st.success(result)
if selected == 'Parkinsons Prediction':
    st.title("🧠 Parkinson’s Disease Assessment")
    
    # Input Field
    fo = st.number_input("MDVP:Fo(Hz)", min_value=0.0, max_value=300.0, value=0.0)
    
    # Prediction Button
    if st.button("🔍 Predict Parkinson’s"):
        prediction = parkinsons_model.predict([[fo]])
        result = "🔴 **Likely Parkinson’s Detected**" if prediction[0] == 1 else "🟢 **No Parkinson’s Detected**"
        st.success(result)
