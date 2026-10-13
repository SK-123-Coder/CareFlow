# Healthcare Data Cleaning and Analysis

A Python-based data cleaning and analysis project that processes healthcare patient and encounter datasets using **Pandas**. It prepares clean CSV files for further analysis and visualization in **Power BI**.

## 📌 Project Overview

Healthcare datasets often contain duplicate records, missing values, and date columns that need proper formatting before analysis.

This project helps prepare healthcare data by:
- Loading patient and encounter datasets.
- Exploring the data and checking for missing values.
- Removing duplicate records.
- Converting encounter dates into datetime format.
- Calculating encounter duration in hours.
- Generating basic statistics.
- Exporting cleaned datasets for further analysis in Power BI.

## 🛠️ Technologies Used

- **Python** — Programming language
- **Pandas** — Data cleaning and analysis
- **CSV** — Input and output data format
- **Power BI** — Data visualization and reporting

## 📂 Project Structure

```text
healthcare-data-analysis/
│
├── patients.csv              # Original patient dataset
├── encounters.csv            # Original encounter dataset
├── careflow.py               # Main Python script
├── requirements.txt          # Project dependencies
│
├── cleaned_patients.csv      # Cleaned patient dataset
├── cleaned_encounters.csv    # Cleaned encounter dataset
└── careflow_analysis.csv     # Encounter data for Power BI
```

The output CSV files are generated automatically when the script runs successfully.

## ⚙️ How It Works

### 1. Load the datasets

The script reads `patients.csv` and `encounters.csv` into Pandas DataFrames.

### 2. Explore the data

It displays the first five records from each dataset to help understand their structure and columns.

### 3. Check missing values

It counts missing values in every column so that incomplete data can be identified.

**Note:** Missing values are reported but are not automatically removed or filled.

### 4. Remove duplicate records

Duplicate rows are removed from both datasets to reduce repeated records.

### 5. Convert date columns

The `START` and `STOP` columns in the encounters dataset are converted into datetime format.

### 6. Calculate encounter duration

The script calculates how long each encounter lasted using the following formula:

```text
Duration (hours) = (STOP - START) / 3600 seconds
```

The result is stored in a new column named `duration_hours`.

### 7. Generate basic statistics

The script displays:
- Total number of patients.
- Total number of encounters.
- Encounter duration count.
- Average encounter duration.
- Standard deviation.
- Minimum and maximum duration.
- Other descriptive statistics.

### 8. Export the results

The cleaned data and analysis results are saved as CSV files for reuse and visualization.

## 🔄 Project Workflow

```text
Original CSV Files
        |
        v
Load Data Using Pandas
        |
        v
Explore Data and Check Missing Values
        |
        v
Remove Duplicate Records
        |
        v
Convert Date Columns
        |
        v
Calculate Encounter Duration
        |
        v
Generate Basic Statistics
        |
        v
Save Cleaned CSV Files
        |
        v
Import Data into Power BI
        |
        v
Create Charts and Reports
```

## 💻 Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

Install the following:
- Python 3.10 or later
- pip (Python package installer)
- A code editor such as Visual Studio Code

### Step 1: Clone the repository

If your project is hosted on GitHub, run:

```bash
git clone <YOUR_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd healthcare-data-analysis
```

Alternatively, download the project files and open the folder in your code editor.

### Step 2: Create a virtual environment

A virtual environment keeps the project's Python dependencies separate from other projects.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

Create a file named `requirements.txt` with the following content:

```text
pandas
```

Install the dependency:

```bash
pip install -r requirements.txt
```

### Step 4: Add the input datasets

Place the following files in the project directory:

```text
patients.csv
encounters.csv
```

Make sure the encounter dataset contains the `START` and `STOP` columns used by the script.

### Step 5: Run the project

Save the Python code in a file named `careflow.py`.

Run the script from the project directory:

```bash
python careflow.py
```

If your system uses `python3` instead, run:

```bash
python3 careflow.py
```

### Step 6: Check the output

After successful execution, the following files should be created:

| File | Purpose |
|---|---|
| `cleaned_patients.csv` | Patient data after duplicate removal |
| `cleaned_encounters.csv` | Encounter data with formatted dates and duration |
| `careflow_analysis.csv` | Encounter data prepared for Power BI |

The terminal will also display dataset previews, missing-value counts, patient and encounter totals, and encounter duration statistics.

## 📊 Using the Data in Power BI

1. Open Power BI Desktop.
2. Select **Get Data → Text/CSV**.
3. Select `careflow_analysis.csv`.
4. Load the data into Power BI.
5. Create visualizations using the available columns.

### Suggested visualizations

- **Card:** Total encounters.
- **Card:** Average encounter duration.
- **Bar chart:** Encounter counts by category, if suitable columns exist.
- **Histogram:** Distribution of encounter durations.
- **Table:** Encounter details and duration in hours.

Use the actual columns available in your dataset when building reports.

## ⚠️ Important Notes

- The input CSV files must exist in the directory from which the script is run, unless their paths are updated in the code.
- Missing values are only identified; they are not automatically handled.
- Rows with missing `START` or `STOP` dates may have missing encounter durations.
- The script does not remove invalid dates, negative durations, or outliers.
- The cleaned files are overwritten when the script runs again.
- Removing duplicates removes identical rows; it does not necessarily identify duplicate patients by patient ID.
- The exported encounter data is intended for analysis and should not be treated as validated clinical data.

## 🚀 Future Improvements

- Handle missing values automatically using configurable rules.
- Validate date ranges and encounter durations.
- Detect duplicate patients using unique patient identifiers.
- Generate additional healthcare metrics.
- Add automated data quality reports.
- Build interactive Power BI dashboards.
- Add logging and error handling for missing or invalid files.

## 👨‍💻 Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Submit a pull request.

## 📄 License

Add a license to this project if you intend to distribute or publish it publicly.

---

**Project Goal:** Transform raw healthcare patient and encounter CSV files into cleaner, analysis-ready datasets that can be used for reporting and visualization in Power BI.
