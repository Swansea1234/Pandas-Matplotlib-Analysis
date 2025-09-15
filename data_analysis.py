import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# A try-except block to handle potential errors loading the data
try:
    # Task 1: Load and Explore the Dataset
    # We'll use a sample CSV file to mimic a real-world scenario
    # If the file doesn't exist, we'll create a simple DataFrame
    
    # Let's create a dummy Iris-like dataset for demonstration
    data = {
        'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 6.7, 6.0, 7.3, 6.7, 6.5, 5.8, 6.4, 6.5, 7.7, 6.0],
        'sepal_width': [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1, 3.3, 2.7, 2.9, 3.1, 3.0, 2.8, 3.2, 3.0, 3.8, 2.7],
        'petal_length': [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5, 5.7, 5.1, 6.3, 5.6, 5.8, 5.1, 5.3, 5.5, 6.7, 5.1],
        'petal_width': [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1, 2.5, 1.6, 1.8, 2.4, 2.2, 2.4, 2.3, 1.8, 2.2, 1.6],
        'species': ['setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica']
    }
    df = pd.DataFrame(data)
    
    # Let's introduce a couple of missing values for demonstration
    df.loc[3, 'sepal_width'] = np.nan
    df.loc[15, 'petal_width'] = np.nan
    
except FileNotFoundError:
    print("Dataset not found. Please check the file path.")
    exit()

print("-----------------------------------")
print("1. Data Loading and Exploration")
print("-----------------------------------")

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nDataset Info (Data Types and Missing Values):")
df.info()

# Clean the dataset: filling missing values
# We'll fill missing numerical values with the mean of their column
df['sepal_width'].fillna(df['sepal_width'].mean(), inplace=True)
df['petal_width'].fillna(df['petal_width'].mean(), inplace=True)
print("\nDataset Info after cleaning:")
df.info()

print("\n-----------------------------------")
print("2. Basic Data Analysis")
print("-----------------------------------")

# Compute basic statistics
print("Descriptive statistics of numerical columns:")
print(df.describe())

# Grouping and computing mean
print("\nMean sepal_length and petal_length per species:")
grouped_data = df.groupby('species')[['sepal_length', 'petal_length']].mean()
print(grouped_data)

print("\n-----------------------------------")
print("3. Data Visualization")
print("-----------------------------------")

# We'll create a dummy 'date' column for the line chart
df['date'] = pd.to_datetime(pd.Series(range(len(df))), unit='D')

# Scatter plot for sepal length vs. petal length
plt.figure(figsize=(8, 6))
plt.scatter(df['sepal_length'], df['petal_length'], c=df['species'].astype('category').cat.codes)
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.grid(True)
plt.show()

# Bar chart showing the average petal length per species
grouped_petal_length = df.groupby('species')['petal_length'].mean()
plt.figure(figsize=(8, 6))
grouped_petal_length.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# Histogram of sepal width
plt.figure(figsize=(8, 6))
plt.hist(df['sepal_width'], bins=10, edgecolor='black', alpha=0.7)
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

# Line chart showing trends over time (using the dummy date)
# We'll plot sepal length over our dummy date
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['sepal_length'], marker='o', linestyle='-')
plt.title('Sepal Length Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sepal Length (cm)')
plt.grid(True)
plt.show()