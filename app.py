# Building a Heart Disease Prediction Web Application using Streamlit and Scikit-Learn
import streamlit as st
import pandas as pd
import joblib
import warnings
warnings.filterwarnings("ignore")

# Page Configuration
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# Load the trained model and preprocessor
model = joblib.load("models\heart_disease_model.pkl")
preprocessor = joblib.load("models\preprocessor.pkl")

# Sidebar
st.sidebar.title("❤️ Heart Disease Prediction")
st.sidebar.markdown("---")
st.sidebar.write("Machine Learning Project")
st.sidebar.write("Algorithm")
st.sidebar.success("Random Forest")
st.sidebar.write("Accuracy")
st.sidebar.info("89.67 %")

# Main Page
st.title("❤️ AI Powered Heart Disease Prediction")
st.markdown(
"""
Predict whether a patient is likely to have Heart Disease using Machine Learning.
"""
)
st.markdown("---")

# Input Form
col1,col2 = st.columns(2)
# Left Column
with col1:

    age = st.number_input("Age",min_value=18, max_value=100, value=40)

    sex = st.selectbox("Sex",["M","F"])

    chest = st.selectbox("Chest Pain Type",["ATA","NAP","ASY","TA"])

    bp = st.number_input("Resting Blood Pressure",min_value=50,max_value=250,value=120)

    chol = st.number_input("Cholesterol",min_value=0,max_value=700,value=200)

    fasting = st.selectbox("Fasting Blood Sugar",[0,1])
# Right Column
with col2:

    ecg = st.selectbox("Resting ECG",["Normal","ST","LVH"])

    hr = st.number_input("Maximum Heart Rate",min_value=60,max_value=220,value=150)

    exercise = st.selectbox("Exercise Angina",["N","Y"])

    oldpeak = st.number_input("Oldpeak",min_value=0.0,max_value=8.0,value=1.0)

    slope = st.selectbox("ST Slope",["Up","Flat","Down"])

# Prediction Button
predict = st.button("🔍 Predict Heart Disease",use_container_width=True)

# Creating a DataFrame from the input values
input_df = pd.DataFrame({

'Age':[age],

'Sex':[sex],

'ChestPainType':[chest],

'RestingBP':[bp],

'Cholesterol':[chol],

'FastingBS':[fasting],

'RestingECG':[ecg],

'MaxHR':[hr],

'ExerciseAngina':[exercise],

'Oldpeak':[oldpeak],

'ST_Slope':[slope]

})

# Preprocess the input data
processed = preprocessor.transform(input_df)
# Make predictions
prediction = model.predict(processed)
probability = model.predict_proba(processed)

# Display the results
if predict:
    if prediction[0] == 1:
        st.error(f"""
                    ### 🔴 High Risk
                        Probability
                        {probability[0][1]*100:.2f}%
                """)
    else:
        st.success(f"""
                    ### 🟢 Low Risk
                        Probability
                        {probability[0][0]*100:.2f}%
                """)
else:
    st.info("Please enter the patient's details and click the predict button to see the results.")

# Patient Summary
st.subheader("Patient Summary")
st.write(input_df)

# Footer
st.markdown("---")
st.caption("Developed using Python, Streamlit and Scikit-Learn")
