import matplotlib.pyplot as plt
import seaborn as sns

# Line Chart: Trends over time (e.g., total cases over time)
plt.figure(figsize=(10,5))
df.groupby("date")["total_cases"].sum().plot()
plt.title("COVID-19 Total Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.show()

# Bar Chart: Comparison across categories (e.g., average new cases per country)
plt.figure(figsize=(12,6))
avg_cases_per_country.nlargest(10).plot(kind="bar", color="blue")
plt.title("Top 10 Countries with Highest Average New Cases")
plt.xlabel("Country")
plt.ylabel("Avg New Cases")
plt.show()

# Histogram: Distribution of new cases
plt.figure(figsize=(10,5))
sns.histplot(df["new_cases"], bins=30, kde=True)
plt.title("Distribution of New Cases")
plt.xlabel("New Cases")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Relationship between total cases and total deaths
plt.figure(figsize=(10,5))
sns.scatterplot(x=df["total_cases"], y=df["total_deaths"], alpha=0.5)
plt.title("Total Cases vs. Total Deaths")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.show()