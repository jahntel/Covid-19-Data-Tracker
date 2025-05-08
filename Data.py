import pandas as pd


try:
    df = pd.read_csv("owid-covid-data.csv")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")


print(df.head())


print(df.info())
print("Missing values:\n", df.isnull().sum())


df.fillna(0, inplace=True)


print("Missing values after cleaning:\n", df.isnull().sum())

# Compute basic statistics
print(df.describe())

# Group by a categorical column (e.g., 'location') and compute the mean for a numerical column (e.g., 'new_cases')
avg_cases_per_country = df.groupby("location")["new_cases"].mean()
print(avg_cases_per_country)

# Identify interesting findings
print("Countries with highest average new cases:\n", avg_cases_per_country.nlargest(10))