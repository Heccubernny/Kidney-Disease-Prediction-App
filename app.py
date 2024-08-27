import streamlit as st
import pandas as pd
import pickle

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
loaded_model = pickle.load(open("kidney_model.pkl", "rb"))

st.title("Kidney Disease Prediction App")
st.write()
st.write("Please enter the following details to predict if you have a kidney disease")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10.0, max_value=120.0)
    bp = st.number_input("Blood Pressure", min_value=10.0, max_value=200.0)
    sg = st.number_input("Serum Glucose", min_value=0.0, max_value=2.0)
    al = st.number_input("Albumin", min_value=0, max_value=4)
    htn = st.selectbox("Hypertension", ["Yes", "No"])
    dm = st.selectbox("Diabetes Mellitus", ["Yes", "No"])
    cad = st.selectbox("Coronary Artery Disease", ["Yes", "No"])
with col2:
    bgr = st.number_input("Blood Glucose Ratio", min_value=10.0, max_value=500.0)
    sc = st.number_input(
        "Serum Creatinine",
        min_value=0.0,
        max_value=50.0,
    )
    pcv = st.number_input("Platelet Count", min_value=10.0, max_value=60.0)
    rc = st.number_input("Red Blood Cell Count", min_value=1, max_value=7)
    pcc = st.selectbox("Pus Cell Count", ["Present", "Not Present"])
    appet = st.selectbox("Appetite", ["Good", "Poor"])
    pe = st.selectbox("Pedal Edema", ["Yes", "No"])

# Convert categorical inputs to numerical
pcc = 1 if pcc == "Present" else 0
htn = 1 if htn == "Yes" else 0
dm = 1 if dm == "Yes" else 0
cad = 1 if cad == "Yes" else 0
appet = 1 if appet == "Good" else 0
pe = 1 if pe == "Yes" else 0

feature_names = [
    "age",
    "bp",
    "sg",
    "al",
    "pcc",
    "bgr",
    "sc",
    "pcv",
    "rc",
    "htn",
    "dm",
    "cad",
    "appet",
    "pe",
]


input_data = pd.DataFrame(
    [[age, bp, sg, al, pcc, bgr, sc, pcv, rc, htn, dm, cad, appet, pe]],
    columns=feature_names,
)


@st.dialog("Result")
def show_result(prediction, prediction_probability):
    if prediction == 0:
        st.markdown(
            "<span>Based on your provided details, you do not have a kidney disease.</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<span>The prediction accuracy is approximately</span> <span style='font-size: 1rem'>{prediction_probability[0][0]}%.</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<span>Please consult with a healthcare professional for further guidance.</span>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<span>Based on your provided details, you have a kidney disease.</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<span>The prediction accuracy is approximately</span> <span style='font-size: 1rem'>{prediction_probability[0][1]}%.</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<span>Please consult with a healthcare professional for further guidance.</span>",
            unsafe_allow_html=True,
        )


if st.button("Predict"):
    prediction = loaded_model.predict(input_data)

    prediction_probability = loaded_model.predict_proba(input_data)

    show_result(prediction, prediction_probability)
