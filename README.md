# Jusper-week 7

# Iris Data Analysis

This project provides a basic data analysis and visualization of the classic **Iris flower dataset** using Python's data science libraries: `pandas`, `matplotlib`, `seaborn`, and `scikit-learn`.

##  Overview

The script performs the following tasks:

1. **Data Loading and Inspection**  
   - Loads the Iris dataset using `sklearn.datasets.load_iris()`.
   - Displays the first five rows, data types, and checks for missing values.

2. **Basic Analysis**  
   - Shows descriptive statistics of numerical features.
   - Computes the mean values grouped by species.

3. **Data Visualization**  
   - **Line Chart:** Cumulative sepal length to simulate trends.
   - **Bar Chart:** Average petal length per species.
   - **Histogram:** Distribution of sepal width.
   - **Scatter Plot:** Sepal length vs. petal length colored by species.

4. **Observations**  
   - Setosa species has shorter petals.
   - Petal length and sepal length are positively correlated.
   - Sepal width distribution is slightly skewed.

##  Requirements

Install the following Python libraries before running the script:

```bash
pip install pandas matplotlib seaborn scikit-learn
```

## Usage

Run the script using any Python interpreter:

```bash
python iris_data_analysis.py
```

Plots will display sequentially and key statistical outputs will be printed to the console.

## Files

- `iris_data_analysis.py` — Main script for data processing and visualization.

##  Notes

- This project uses only built-in datasets and does not require any external data files.
- The visualizations are generated using `matplotlib` and `seaborn`.
