import streamlit as st
import pandas as pd
import pickle

# Load the model
loaded_model = pickle.load(open("kidney_model_2.pkl", "rb"))

feature_names = [
    "age",
    "bp",
    "sg",
    "su",
    "rbc",
    "pc",
    "pcc",
    "bgr",
    "bu",
    "pot",
    "hemo",
    "pcv",
    "htn",
    "dm",
    "cad",
    "appet",
    "pe",
    "ane",
]

# Collect user input
st.title("Kidney Disease Prediction App")
st.write("Please enter the following details to predict if you have a kidney disease")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10.0, max_value=120.0)
    bp = st.number_input("Blood Pressure", min_value=10.0, max_value=200.0)
    sg = st.number_input("Serum Glucose", min_value=0.0, max_value=2.0)
    su = st.number_input("Sugar", min_value=0, max_value=5)
    rbc = st.selectbox("Red Blood Cells", ["Normal", "Abnormal"])
    pc = st.selectbox("Pus Cell", ["Normal", "Abnormal"])
    pcc = st.selectbox("Pus Cell Clumps", ["Present", "Not Present"])
    bgr = st.number_input("Blood Glucose Ratio", min_value=10.0, max_value=500.0)
    bu = st.number_input("Blood Urea", min_value=0.0, max_value=250.0)

with col2:
    pcv = st.number_input("Packed Cell Volume", min_value=10.0, max_value=60.0)
    htn = st.selectbox("Hypertension", ["Yes", "No"])
    dm = st.selectbox("Diabetes Mellitus", ["Yes", "No"])
    cad = st.selectbox("Coronary Artery Disease", ["Yes", "No"])
    appet = st.selectbox("Appetite", ["Good", "Poor"])
    pe = st.selectbox("Pedal Edema", ["Yes", "No"])
    ane = st.selectbox("Anemia", ["Yes", "No"])
    pot = st.number_input("Potassium", min_value=0.0, max_value=10.0)
    hemo = st.number_input("Hemoglobin", min_value=0.0, max_value=20.0)

# Convert categorical inputs to numerical
rbc = 1 if rbc == "Abnormal" else 0
pc = 1 if pc == "Abnormal" else 0
pcc = 1 if pcc == "Present" else 0
htn = 1 if htn == "Yes" else 0
dm = 1 if dm == "Yes" else 0
cad = 1 if cad == "Yes" else 0
appet = 1 if appet == "Good" else 0
pe = 1 if pe == "Yes" else 0
ane = 1 if ane == "Yes" else 0

# Create a DataFrame with the input values
input_data = pd.DataFrame(
    [
        [
            age,
            bp,
            sg,
            su,
            rbc,
            pc,
            pcc,
            bgr,
            bu,
            pot,
            hemo,
            pcv,
            htn,
            dm,
            cad,
            appet,
            pe,
            ane,
        ]
    ],
    columns=feature_names,
)


@st.dialog("Result")
def show_result(prediction, prediction_probability):
    if prediction == 0:
        st.markdown(
            "<span style='color:red'>Based on your provided details, you do not have a kidney disease.</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<span style='color:red'>The prediction accuracy is approximately {(prediction_probability[0][0])*100}%.</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<span style='color:red'>Please consult with a healthcare professional for further guidance.</span>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<span style='color:red'>Based on your provided details, you have a kidney disease.</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<span style='color:red'>The prediction accuracy is approximately {(prediction_probability[0][1])*100}%.</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<span style='color:red'>Please consult with a healthcare professional for further guidance.</span>",
            unsafe_allow_html=True,
        )


if st.button("Predict", type="primary"):
    prediction = loaded_model.predict(input_data)
    prediction_probability = loaded_model.predict_proba(input_data)
    show_result(prediction, prediction_probability)
