import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load the models
with open("pkl/naive_bayes.pkl", "rb") as model_file:
    naive_bayes = pickle.load(model_file)

with open("pkl/isolation_forest.pkl", "rb") as iso_file:
    isolationforest = pickle.load(iso_file)

with open("pkl/svm.pkl", "rb") as svm_file:
    svm = pickle.load(svm_file)

st.title("Model Prediction App")

model_choice = st.selectbox(
    "Choose a model", ("Naive Bayes", "Isolation Forest", "SVM")
)

# Define features for each model
naive_bayes_features = [
    "Legal_Requirements",
    "Privacy_Regulations",
    "Data_Ownership",
    "Security_Risks",
    "Access_Control",
    "Punishments_for_Violations",
    "Proprietary_Tools",
    "User_Access_Procedures",
    "Patient_ID",
    "Gender",
    "Age",
    "Days_Since_Last_Visit",
]

isolationforest_features = [
    "Legal_Requirements",
    "Privacy_Regulations",
    "Data_Ownership",
    "Security_Risks",
    "Access_Control",
    "Punishments_for_Violations",
    "Proprietary_Tools",
    "User_Access_Procedures",
    "Patient_ID",
    "Gender",
    "Age",
    "Days_Since_Last_Visit",
]

svm_features = [
    "Privacy_Regulations",
    "Security_Risks",
    "Access_Control",
    "Patient_ID",
    "Gender",
]


# Function to display feature input tables
def display_input_table(features, model_name):
    input_data = []
    for feature in features:
        value = st.number_input(
            f"{model_name} - {feature}", key=f"{model_name}_{feature}", value=0.0
        )
        input_data.append(value)
    return np.array(input_data).reshape(1, -1)


# Display model-specific input tables and features
if model_choice == "Naive Bayes":
    st.write("### Naive Bayes Input Data")
    naive_bayes_input_data = display_input_table(naive_bayes_features, "Naive Bayes")
    st.table(pd.DataFrame(naive_bayes_input_data, columns=naive_bayes_features))

elif model_choice == "Isolation Forest":
    st.write("### Isolation Forest Input Data")
    isolationforest_input_data = display_input_table(
        isolationforest_features, "Isolation Forest"
    )
    st.table(pd.DataFrame(isolationforest_input_data, columns=isolationforest_features))

elif model_choice == "SVM":
    st.write("### SVM Input Data")
    svm_input_data = display_input_table(svm_features, "SVM")
    st.table(pd.DataFrame(svm_input_data, columns=svm_features))

# Predict button
if st.button("Predict"):
    if model_choice == "Naive Bayes":
        prediction = naive_bayes.predict(naive_bayes_input_data)
        st.write(f"Naive Bayes Prediction: {prediction[0]}")
    elif model_choice == "Isolation Forest":
        prediction = isolationforest.predict(isolationforest_input_data)
        prediction = np.where(prediction == 1, "Normal", "Anomaly")
        st.write(f"Isolation Forest Prediction: {prediction[0]}")
    elif model_choice == "SVM":
        prediction = svm.predict(svm_input_data)
        st.write(f"SVM Prediction: {prediction[0]}")
