
import pandas as pd


# 1. Load healthcare datasets
patients = pd.read_csv("patients.csv")
encounters = pd.read_csv("encounters.csv")


# 2. Display the first 5 records to understand the data
print("Patients Data:")
print(patients.head())

print("\nEncounters Data:")
print(encounters.head())


# 3. Check for missing values in each dataset
print("\nMissing Values in Patients:")
print(patients.isnull().sum())

print("\nMissing Values in Encounters:")
print(encounters.isnull().sum())


# 4. Remove duplicate records
patients = patients.drop_duplicates()
encounters = encounters.drop_duplicates()


# 5. Convert START and STOP columns into date-time format
encounters["START"] = pd.to_datetime(encounters["START"])
encounters["STOP"] = pd.to_datetime(encounters["STOP"])


# 6. Calculate encounter duration in hours
# Subtract the start time from the stop time
encounters["duration_hours"] = (
    encounters["STOP"] - encounters["START"]
).dt.total_seconds() / 3600


# 7. Display the cleaned encounter data
print("\nCleaned Encounters Data:")
print(encounters.head())


# 8. Save the cleaned datasets as CSV files
# index=False prevents pandas from adding an extra index column
patients.to_csv("cleaned_patients.csv", index=False)
encounters.to_csv("cleaned_encounters.csv", index=False)

print("\nCleaned datasets saved successfully!")


# 9. Perform basic data analysis
print("\nBasic Data Analysis:")
print("Total Patients:", len(patients))
print("Total Encounters:", len(encounters))


# 10. Calculate statistics for encounter duration
# Shows count, average, standard deviation, minimum, and maximum
print("\nEncounter Duration Statistics:")
print(encounters["duration_hours"].describe())


# 11. Export encounter data for Power BI
# This file can be imported into Power BI for visualization
encounters.to_csv("careflow_analysis.csv", index=False)

print("\nAnalysis completed successfully!")
print("Power BI dataset saved as careflow_analysis.csv")