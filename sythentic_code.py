from faker import Faker
import pandas as pd
import random

# Initialize Faker and create a list to store data
fake = Faker()
data = []

# Number of synthetic records to generate
num_records = 2500

# Define possible values for attributes
legal_requirements = [
    "HIPAA Compliance",
    "GDPR Compliance",
    "Local Data Protection Laws",
    "International Standards",
]
privacy_regulations = [
    "Confidentiality Agreements",
    "Data Encryption Standards",
    "Access Restrictions",
    "Anonymization",
]
data_ownership = ["Patient", "Healthcare Provider", "Healthcare Organization", "Shared"]
security_risks = [
    "Data Breach",
    "Unauthorized Access",
    "Data Corruption",
    "Phishing Attacks",
]
access_control = [
    "Role-Based Access Control",
    "Attribute-Based Access Control",
    "Discretionary Access Control",
]
punishments_for_violations = [
    "Fines",
    "Legal Action",
    "Revocation of Access",
    "Reputational Damage",
]
proprietary_tools = [
    "Proprietary EHR Systems",
    "Secure Messaging Platforms",
    "Encryption Software",
    "Compliance Monitoring Tools",
]
user_access_procedures = [
    "Secure Login",
    "Two-Factor Authentication",
    "Access Logs",
    "User Training",
]
is_authenticated = ["Authentication", "Not Authenticated"]

used_patient_ids = set()

# Generate synthetic records
for _ in range(num_records):
    while True:
        patient_id = random.randint(1, 3000)
        if patient_id not in used_patient_ids:
            used_patient_ids.add(patient_id)
            break
        record = {
            "Patient_ID": patient_id,
            "Patient_Name": fake.name(),
            "Date_of_Birth": fake.date_of_birth(
                minimum_age=18, maximum_age=90
            ).strftime("%Y-%m-%d"),
            "Gender": random.choice(["Male", "Female"]),
            "Legal_Requirements": random.choice(legal_requirements),
            "Privacy_Regulations": random.choice(privacy_regulations),
            "Data_Ownership": random.choice(data_ownership),
            "Security_Risks": random.choice(security_risks),
            "Access_Control": random.choice(access_control),
            "Punishments_for_Violations": random.choice(punishments_for_violations),
            "Proprietary_Tools": random.choice(proprietary_tools),
            "User_Access_Procedures": random.choice(user_access_procedures),
            "User_Is_Authenticated": random.choice(is_authenticated),
            "Last_Visit": fake.date_between(
                start_date="-2y", end_date="today"
            ).strftime("%Y-%m-%d"),
        }
        data.append(record)

# Create a DataFrame
df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv("new_ehl_data.csv", index=False)

print("Synthetic EHL data generated and saved to 'synthetic_ehl_data.csv'.")
