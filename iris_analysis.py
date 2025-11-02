# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ------------------------------
# Task 1: Load and Explore Dataset
# ------------------------------

# Load Iris dataset from sklearn
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Check data types and missing values
print("\nDataset Info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# No missing values in this dataset; if there were, you could fill or drop
# Example: df.fillna(0, inplace=True) or df.dropna(inplace=True)

# ------------------------------
# Task 2: Basic Data Analysis
# ------------------------------

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Grouping by species and calculating mean of numerical columns
grouped = df.groupby('species').mean()
print("\nMean values per species:")
print(grouped)

# ------------------------------
# Task 3: Data Visualization
# ------------------------------

# Set Seaborn style
sns.set(style="whitegrid")

# 1️⃣ Line chart (using the mean of features for each species)
grouped.plot(kind='line', marker='o')
plt.title("Mean Feature Values per Iris Species")
plt.xlabel("Features")
plt.ylabel("Mean Value")
plt.legend(title='Species')
plt.show()

# 2️⃣ Bar chart (average petal length per species)
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3️⃣ Histogram (distribution of sepal length)
plt.hist(df['sepal length (cm)'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4️⃣ Scatter plot (sepal length vs. petal length)
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, s=100)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()

# ------------------------------
# Observations / Findings
# ------------------------------
print("\nObservations:")
print("- Setosa species has smaller petal and sepal lengths than Versicolor and Virginica.")
print("- There is a positive correlation between sepal length and petal length.")
print("- Virginica tends to have the largest feature values among the species.")
