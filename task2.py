import pandas as pd
import matplotlib.pyplot as plt

#  *** TASK 2: HR DATA ANALYSIS ***

# Path to the dataset file
filepath = "C:\\Users\\asus\\Desktop\\HR Data.csv"
data = pd.read_csv(filepath)

# Dropping unnecessary columns to clean up the data
unwanted_columns = ['EmployeeCount', 'Over18', 'StandardHours']
data_cleaned = data.drop(columns=unwanted_columns, errors='ignore')

# Renaming 'Attrition' column to 'Employee Turnover' for better clarity
if 'Attrition' in data_cleaned.columns:
    data_cleaned.rename(columns={'Attrition': 'Employee Turnover'}, inplace=True)

# Removing rows with missing values
data_cleaned.dropna(inplace=True)

# Ensuring there are no duplicate rows
data_cleaned = data_cleaned.drop_duplicates()

# Saving the cleaned dataset
cleaned_file = filepath.replace('.csv', '_cleaned.csv')
data_cleaned.to_csv(cleaned_file, index=False)
print(f"Cleaned HR data has been saved at: {cleaned_file}")

# Visualization 1: Employee Turnover Count (Bar Chart)
if 'Employee Turnover' in data_cleaned.columns:
    turnover_data = data_cleaned['Employee Turnover'].value_counts()
    plt.figure(figsize=(8, 6))
    turnover_data.plot(kind='bar', color=['blue', 'red'])
    plt.title("Employee Turnover Count")
    plt.xlabel("Turnover Status")
    plt.ylabel("Employee Count")
    plt.grid(axis='y')
    plt.show()

# Visualization 2: Department-Wise Distribution (Pie Chart)
if 'Department' in data_cleaned.columns:
    department_data = data_cleaned['Department'].value_counts()
    plt.figure(figsize=(8, 8))
    department_data.plot(kind='pie', autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'white'}, colors=['lightblue', 'lightgreen', 'lightpink'])
    plt.title("Employee Distribution Across Departments")
    plt.ylabel('')
    plt.show()

# Visualization 3: Employee Turnover by Department (Stacked Bar Chart)
if 'Employee Turnover' in data_cleaned.columns and 'Department' in data_cleaned.columns:
    turnover_by_dept = data_cleaned.groupby('Department')['Employee Turnover'].value_counts().unstack()
    turnover_by_dept.plot(kind='bar', stacked=True, figsize=(10, 6), color=['blue', 'green'])
    plt.title("Employee Turnover by Department")
    plt.xlabel("Department")
    plt.ylabel("Employee Count")
    plt.legend(title="Turnover Status", labels=['Stayed', 'Left'])
    plt.grid(axis='y')
    plt.xticks(rotation=45)
    plt.show()
