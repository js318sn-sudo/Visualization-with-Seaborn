# Data Visualization with Seaborn

## Project Objective

The objective of this project is to understand and implement data visualization techniques using the Seaborn library. The project focuses on creating a Correlation Heatmap to analyze relationships between numerical variables and identify patterns within the dataset.

---

# Introduction

This project demonstrates Data Visualization using Seaborn, a powerful Python library built on top of Matplotlib. A Correlation Heatmap is used to visualize relationships between variables, making it easier to identify strong positive, negative, or weak correlations in the dataset.

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

# Topics Covered

* Data Visualization
* Seaborn Fundamentals
* Correlation Analysis
* Correlation Matrix
* Heatmap Visualization
* Data Interpretation

---

# Dataset

The dataset contains employee information including Age, Salary, Experience, and Performance Score.

| Name  | Age | Salary | Experience | PerformanceScore |
| ----- | --- | ------ | ---------- | ---------------- |
| Ravi  | 25  | 45000  | 2          | 78               |
| Sita  | 30  | 52000  | 5          | 88               |
| Kiran | 28  | 48000  | 3          | 82               |
| Anu   | 35  | 65000  | 8          | 91               |
| Rahul | 40  | 80000  | 12         | 95               |

---

# Project Workflow

1. Import Required Libraries
2. Create and Load Dataset
3. Explore Dataset Information
4. Generate Correlation Matrix
5. Create Correlation Heatmap
6. Analyze Relationships
7. Draw Insights and Conclusions

---

# Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# Create Dataset

```python
df = pd.DataFrame(data)

print(df)
```

---

# Correlation Matrix

```python
correlation = df.select_dtypes(include=np.number).corr()

print(correlation)
```

---

# Correlation Heatmap

```python
plt.figure(figsize=(8,5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()
```

---

# Visualization

## Correlation Heatmap

![Correlation Heatmap](correlation_heatmap.png)

---

# Key Insights

* Salary increases with experience.
* Performance score improves with experience.
* Age and salary show a positive relationship.
* The heatmap makes correlations easy to identify.
* Stronger correlations are represented by darker colors.

---

# Conclusion

This project demonstrates Data Visualization using Seaborn and Correlation Heatmaps. The heatmap provides a clear visual representation of relationships between numerical variables, helping identify trends and patterns within the dataset. Correlation analysis is an important technique in exploratory data analysis and data science.
