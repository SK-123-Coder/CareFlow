import pandas as pd

# 1. Load healthcare datasets
patients = pd.read_csv("patients.csv")
encounters = pd.read_csv("encounters.csv")

# 2. Display first 5 records
print("Patients Data:")
print(patients.head())

print("\nEncounters Data:")
print(encounters.head())

# 3. Check missing values
print("\nMissing Values in Patients:")
print(patients.isnull().sum())

print("\nMissing Values in Encounters:")
print(encounters.isnull().sum())

# 4. Remove duplicate records
patients = patients.drop_duplicates()
encounters = encounters.drop_duplicates()

# 5. Convert START and STOP to datetime
encounters["START"] = pd.to_datetime(
    encounters["START"], errors="coerce"
)
encounters["STOP"] = pd.to_datetime(
    encounters["STOP"], errors="coerce"
)

# 6. Calculate encounter duration in hours
encounters["duration_hours"] = (
    encounters["STOP"] - encounters["START"]
).dt.total_seconds() / 3600

# 7. Check invalid and unusual durations
print("\nNegative Durations:")
print((encounters["duration_hours"] < 0).sum())

# 8. Display cleaned data
print("\nCleaned Encounters Data:")
print(encounters.head())

# 9. Basic analysis
print("\nTotal Patients:", len(patients))
print("Total Encounters:", len(encounters))

# 10. Encounter duration statistics
print("\nEncounter Duration Statistics:")
print(encounters["duration_hours"].describe())

# 11. Save cleaned datasets
patients.to_csv("cleaned_patients.csv", index=False)
encounters.to_csv("cleaned_encounters.csv", index=False)

# 12. Export dataset for Power BI
encounters.to_csv("careflow_analysis.csv", index=False)

print("\nCleaned datasets saved successfully!")
print("Power BI dataset saved as careflow_analysis.csv")