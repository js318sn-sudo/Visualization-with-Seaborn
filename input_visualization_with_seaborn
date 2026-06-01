# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create Dataset
data = {
    "Age": [25, 30, 28, 35, 40, 27, 32, 29, 31, 26],
    "Salary": [45000, 52000, 48000, 65000, 80000, 50000, 58000, 62000, 72000, 54000],
    "Experience": [2, 5, 3, 8, 12, 4, 6, 5, 9, 3],
    "PerformanceScore": [78, 88, 82, 91, 95, 85, 89, 92, 90, 84]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("Dataset")
print(df)

# First 5 Rows
print("\nFirst 5 Rows")
print(df.head())

# Dataset Information
print("\nDataset Information")
print(df.info())

# Dataset Shape
print("\nDataset Shape")
print(df.shape)

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Data Types
print("\nData Types")
print(df.dtypes)

# Summary Statistics
print("\nSummary Statistics")
print(df.describe())

# Correlation Matrix
print("\nCorrelation Matrix")
correlation = df.corr()
print(correlation)

# Save Correlation Matrix as Image
plt.figure(figsize=(8,4))
plt.axis("off")
plt.table(
    cellText=correlation.round(2).values,
    colLabels=correlation.columns,
    rowLabels=correlation.index,
    loc="center"
)
plt.title("Correlation Matrix")
plt.savefig("correlation_matrix.png", bbox_inches="tight")
plt.show()

# Heatmap
plt.figure(figsize=(8,5))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)
plt.title("Heatmap")
plt.savefig("heatmap.png")
plt.show()

# Insights
print("\nInsights")
print("1. Age and Salary show a positive relationship.")
print("2. Experience and Salary are positively correlated.")
print("3. Performance Score tends to increase with Experience.")
print("4. Correlation Matrix helps measure relationships between variables.")
print("5. Heatmap provides a visual representation of correlations.")
