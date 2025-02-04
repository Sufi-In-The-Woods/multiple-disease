import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Function to predict diabetes
def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    try:
        prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        return 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'
    except Exception as e:
        return f"Error in prediction: {e}"

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Description of terms
    st.markdown("""
    ### Understanding the Input Fields:
    Below are the descriptions of the terms used in this prediction model. Please provide accurate values for better results.

    - **Number of Pregnancies**: The number of times the person has been pregnant. (Normal range: 0–17)
    - **Glucose Level**: The concentration of glucose in the blood, measured in mg/dL. (Normal range: 70–140 mg/dL)
    - **Blood Pressure Value**: The systolic blood pressure, measured in mmHg. (Normal range: 90–120 mmHg)
    - **Skin Thickness Value**: The thickness of the skin fold at the triceps, measured in mm. (Normal range: 10–50 mm)
    - **Insulin Level**: The concentration of insulin in the blood, measured in µU/mL. (Normal range: 16–166 µU/mL)
    - **BMI (Body Mass Index)**: A measure of body fat based on height and weight. (Normal range: 18.5–24.9)
    - **Diabetes Pedigree Function**: A score that indicates the genetic influence of diabetes based on family history. (Normal range: 0.08–2.42)
    - **Age**: The age of the person in years. (Normal range: 21–81 years)
    """)

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0, help="Enter the number of pregnancies (0–17).")
        Glucose = st.number_input('Glucose Level (mg/dL)', min_value=0, max_value=200, value=0, help="Enter the glucose level in mg/dL (70–140 mg/dL is normal).")
    
    with col2:
        BloodPressure = st.number_input('Blood Pressure Value (mmHg)', min_value=0, max_value=150, value=0, help="Enter the systolic blood pressure in mmHg (90–120 mmHg is normal).")
        SkinThickness = st.number_input('Skin Thickness Value (mm)', min_value=0, max_value=100, value=0, help="Enter the skin thickness in mm (10–50 mm is normal).")
    
    with col3:
        Insulin = st.number_input('Insulin Level (µU/mL)', min_value=0, max_value=1000, value=0, help="Enter the insulin level in µU/mL (16–166 µU/mL is normal).")
        BMI = st.number_input('BMI Value', min_value=0.0, max_value=70.0, value=0.0, help="Enter the BMI value (18.5–24.9 is normal).")
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value', min_value=0.0, max_value=3.0, value=0.0, help="Enter the diabetes pedigree function value (0.08–2.42 is normal).")
    
    with col2:
        Age = st.number_input('Age of the Person', min_value=0, max_value=120, value=0, help="Enter the age of the person (21–81 years is normal).")
    
    # Code for Prediction
    diab_diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', min_value=0, max_value=120, value=0)
        sex = st.number_input('Sex (0 = female, 1 = male)', min_value=0, max_value=1, value=0)
    
    with col2:
        cp = st.number_input('Chest Pain types (0-3)', min_value=0, max_value=3, value=0)
        trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=200, value=0)
    
    with col3:
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0, max_value=600, value=0)
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)', min_value=0, max_value=1, value=0)
    
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (0-2)', min_value=0, max_value=2, value=0)
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=0, max_value=300, value=0)
    
    with col2:
        exang = st.number_input('Exercise Induced Angina (1 = yes, 0 = no)', min_value=0, max_value=1, value=0)
        oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0, max_value=10.0, value=0.0)
    
    with col3:
        slope = st.number_input('Slope of the peak exercise ST segment (0-2)', min_value=0, max_value=2, value=0)
        ca = st.number_input('Major vessels colored by flourosopy (0-3)', min_value=0, max_value=3, value=0)
    
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', min_value=0, max_value=2, value=0)
    
    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
            st.success(heart_diagnosis)
        except Exception as e:
            st.error(f"Error in prediction: {e}")

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, max_value=300.0, value=0.0)
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, max_value=300.0, value=0.0)
    
    with col2:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, max_value=300.0, value=0.0)
        Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, max_value=1.0, value=0.0)
    
    with col3:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, max_value=1.0, value=0.0)
        RAP = st.number_input('MDVP:RAP', min_value=0.0, max_value=1.0, value=0.0)
    
    with col4:
        PPQ = st.number_input('MDVP:PPQ', min_value=0.0, max_value=1.0, value=0.0)
        DDP = st.number_input('Jitter:DDP', min_value=0.0, max_value=1.0, value=0.0)
    
    with col5:
        Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, max_value=1.0, value=0.0)
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, max_value=1.0, value=0.0)
    
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, max_value=1.0, value=0.0)
        APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, max_value=1.0, value=0.0)
    
    with col2:
        APQ = st.number_input('MDVP:APQ', min_value=0.0, max_value=1.0, value=0.0)
        DDA = st.number_input('Shimmer:DDA', min_value=0.0, max_value=1.0, value=0.0)
    
    with col3:
        NHR = st.number_input('NHR', min_value=0.0, max_value=1.0, value=0.0)
        HNR = st.number_input('HNR', min_value=0.0, max_value=1.0, value=0.0)
    
    with col4:
        RPDE = st.number_input('RPDE', min_value=0.0, max_value=1.0, value=0.0)
        DFA = st.number_input('DFA', min_value=0.0, max_value=1.0, value=0.0)
    
    with col5:
        spread1 = st.number_input('spread1', min_value=0.0, max_value=1.0, value=0.0)
        spread2 = st.number_input('spread2', min_value=0.0, max_value=1.0, value=0.0)
    
    with col1:
        D2 = st.number_input('D2', min_value=0.0, max_value=1.0, value=0.0)
        PPE = st.number_input('PPE', min_value=0.0, max_value=1.0, value=0.0)
    
    if st.button("Parkinson's Test Result"):
        try:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)
        except Exception as e:
            st.error(f"Error in prediction: {e}")
