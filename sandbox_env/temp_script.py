import numpy as np
import pandas as pd

# Sample data initialization based on provided schema
data = [
    {
        "employee_id": 1,
        "name": "Ali Khan",
        "department": "Engineering",
        "salary": 85000,
        "experience_years": 4,
        "performance_score": 4.5,
    },
    {
        "employee_id": 2,
        "name": "Sara Ahmed",
        "department": "Marketing",
        "salary": 62000,
        "experience_years": 2,
        "performance_score": 3.8,
    },
    {
        "employee_id": 3,
        "name": "Usman Malik",
        "department": "Engineering",
        "salary": 95000,
        "experience_years": 6,
        "performance_score": 4.8,
    },
]

df = pd.DataFrame(data)

# 1. Dataset Schema Analysis
print("--- DATASET SCHEMA & OVERVIEW ---")
schema_info = pd.DataFrame(
    {
        "Data_Type": df.dtypes,
        "Non_Null_Count": df.notnull().sum(),
        "Unique_Values": df.nunique(),
    }
)
print(schema_info)
print("\n" + "=" * 50 + "\n")

# 2. Descriptive Summary Statistics for Numerical Columns
# Excluding 'employee_id' as it is a unique identifier, not a metric
numerical_cols = [
    col
    for col in df.select_dtypes(include=[np.number]).columns
    if col != "employee_id"
]

print("--- DESCRIPTIVE SUMMARY STATISTICS ---")
descriptive_stats = df[numerical_cols].describe().T
descriptive_stats["median"] = df[numerical_cols].median()
descriptive_stats["skew"] = df[numerical_cols].skew()
print(
    descriptive_stats[
        ["count", "mean", "std", "min", "25%", "median", "75%", "max", "skew"]
    ]
)
print("\n" + "=" * 50 + "\n")

# 3. Top Correlations Between Features
print("--- CORRELATION ANALYSIS ---")
corr_matrix = df[numerical_cols].corr()
print("Correlation Matrix:")
print(corr_matrix.round(4))

# Extract and rank top pairwise correlations (excluding self-correlation and duplicates)
corr_pairs = (
    corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    .stack()
    .reset_index()
)
corr_pairs.columns = ["Feature_1", "Feature_2", "Correlation"]
corr_pairs["Abs_Correlation"] = corr_pairs["Correlation"].abs()
top_correlations = corr_pairs.sort_values(
    by="Abs_Correlation", ascending=False
).drop(columns=["Abs_Correlation"])

print("\nRanked Pairwise Feature Correlations:")
print(top_correlations.to_string(index=False))