import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, boxcox

# Create the "Academic Performance" dataset
data = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'gpa': [3.8, 2.9, 3.5, 2.7, 3.2, 3.9, 2.6, 4.0, 3.1, 2.8],
    'attendance': [90, 85, 92, 75, 88, 95, 70, 92, 82, 80],
    'test_scores': [85, 75, 90, 70, 80, 92, 65, 95, 78, 72],
    'extracurricular': [5, 3, 7, 2, 6, 8, 1, 9, 4, 3]
})

# 1. Scan all variables for missing values and inconsistencies
print("Missing values:")
print(data.isnull().sum())

# There are no missing values in the dataset

# 2. Scan all numeric variables for outliers
numeric_cols = ['gpa', 'attendance', 'test_scores', 'extracurricular']

for col in numeric_cols:
    q1 = data[col].quantile(0.25)
    q3 = data[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    print(f"Outliers in {col}:")
    print(data[(data[col] < lower_bound) | (data[col] > upper_bound)])

# There are no outliers in the dataset

# 3. Apply data transformations
# Purpose: Convert the 'gpa' variable to a normal distribution
skewness = skew(data['gpa'])
print(f"Skewness of 'gpa' before transformation: {skewness:.2f}")

data['gpa_transformed'], lambda_value = boxcox(data['gpa'])
skewness_transformed = skew(data['gpa_transformed'])
print(f"Skewness of 'gpa' after Box-Cox transformation: {skewness_transformed:.2f}")
print(f"Box-Cox transformation lambda value: {lambda_value:.2f}")

# Plot the original and transformed 'gpa' distributions
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(data['gpa'], kde=True)
plt.title('Original GPA Distribution')
plt.subplot(1, 2, 2)
sns.histplot(data['gpa_transformed'], kde=True)
plt.title('Transformed GPA Distribution')
plt.tight_layout()
plt.show()