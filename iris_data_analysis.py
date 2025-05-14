
# Analyzing Data with Pandas and Visualizing Results with Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    print("First five rows of the dataset:")
    print(df.head())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

except Exception as e:
    print(f"Error loading dataset: {e}")

# Task 2: Basic Data Analysis
print("\nDescriptive statistics:")
print(df.describe())

grouped = df.groupby('species').mean()
print("\nMean of numerical columns grouped by species:")
print(grouped)

# Task 3: Data Visualization

# Line chart - simulate trend with cumulative sum
df['index'] = range(len(df))
df_sorted = df.sort_values(by='index')
plt.figure(figsize=(10, 5))
plt.plot(df_sorted['index'], df_sorted['sepal length (cm)'].cumsum(), label='Cumulative Sepal Length')
plt.title("Line Chart - Cumulative Sepal Length")
plt.xlabel("Index")
plt.ylabel("Cumulative Sepal Length")
plt.legend()
plt.grid(True)
plt.show()

# Bar chart - average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title("Bar Chart - Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length")
plt.grid(True)
plt.show()

# Histogram - distribution of sepal width
plt.figure(figsize=(8, 5))
plt.hist(df['sepal width (cm)'], bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram - Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Scatter plot - sepal length vs petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title("Scatter Plot - Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.grid(True)
plt.show()

# Findings/Observations
print("\nObservations:")
print("- Setosa has generally shorter petal lengths compared to Versicolor and Virginica.")
print("- There’s a clear positive correlation between petal length and sepal length.")
print("- Distribution of sepal width is somewhat skewed with most values around 3.0.")
