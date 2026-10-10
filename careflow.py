import pandas as pd

# Load healthcare data
patients = pd.read_csv("patients.csv")
encounters = pd.read_csv("encounters.csv")

# Check the data
print(patients.head())
print(encounters.head())

# Check missing values
print(patients.isnull().sum())
print(encounters.isnull().sum())

# Remove duplicate records
patients = patients.drop_duplicates()
encounters = encounters.drop_duplicates()

# Convert dates
encounters["START"] = pd.to_datetime(encounters["START"])
encounters["STOP"] = pd.to_datetime(encounters["STOP"])

# Calculate encounter duration in hours
encounters["duration_hours"] = (
    encounters["STOP"] - encounters["START"]
).dt.total_seconds() / 3600

print(encounters.head())

patients.to_csv("cleaned_patients.csv", index=False)
encounters.to_csv("cleaned_encounters.csv", index=False)

print("Data cleaned and saved successfully!")

# Basic analysis
print("Total Patients:", len(patients))
print("Total Encounters:", len(encounters))

print("\nEncounter Duration Statistics:")
print(encounters["duration_hours"].describe())

# Save analysis data for Power BI
encounters.to_csv("careflow_analysis.csv", index=False)

print("\nAnalysis completed!")