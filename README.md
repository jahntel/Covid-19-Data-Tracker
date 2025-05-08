# Covid-19-Data-Tracker
# COVID-19 Data Analysis using Python 🦠📊  

## **Project Overview**
This project analyzes the **OWID COVID-19 dataset** using Python. It utilizes **Pandas for data manipulation**, **Matplotlib & Seaborn for visualization**, and **basic statistical analysis** to uncover insights. The project performs **data cleaning, exploratory analysis, and visualization** to extract meaningful trends from COVID-19 data.

---

## **Features**
✔ **Data Loading** – Reads the dataset using Pandas  
✔ **Data Cleaning** – Handles missing values for accurate analysis  
✔ **Exploratory Data Analysis** – Computes summary statistics  
✔ **Grouping & Aggregation** – Computes insights per country  
✔ **Visualizations** – Line charts, bar charts, histograms, scatter plots  

---

## **Project Structure**


---

## **Installation & Setup**
### **1️⃣ Clone the repository**
```bash
git clone https://github.com/yourusername/covid-analysis.git
cd covid-analysis

2️⃣ Install required dependencies
pip install -r requirements.txt


Data Processing Steps
Step 1: Load Dataset
import pandas as pd
df = pd.read_csv("owid-covid-data.csv")

Step 2: Clean Data
df.fillna(0, inplace=True)

Step 3: Exploratory Data Analysis
print(df.describe())  # Summary statistics
avg_cases_per_country = df.groupby("location")["new_cases"].mean()
print(avg_cases_per_country)

Visualizations
1️⃣ Line Chart 
import matplotlib.pyplot as plt
df.groupby("date")["total_cases"].sum().plot()
plt.title("COVID-19 Total Cases Over Time")

2️⃣ Bar Chart 
import seaborn as sns
avg_cases_per_country.nlargest(10).plot(kind="bar")

3️⃣ Histogram
sns.histplot(df["new_cases"], bins=30, kde=True)

Error Handling
✔ Handles file errors (FileNotFoundError)
✔ Checks for missing values (df.isnull().sum())
✔ Uses exception handling (try-except)
