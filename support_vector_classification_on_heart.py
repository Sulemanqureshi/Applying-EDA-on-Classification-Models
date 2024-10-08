# -*- coding: utf-8 -*-
"""Support Vector Classification on heart.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YKVqa9K3hoWO_dw7e7roDvnULxu-QrTV

#Support Vector Classification

##Import Libraries
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

"""#Load the Dataset"""

df = pd.read_csv('heart.csv')

"""# Split the data into features (X) and target (y)"""

X = df.drop('target', axis=1)
y = df['target']

"""#Train-Test Split"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""# Feature Scaling

"""

from sklearn.preprocessing import StandardScaler

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""# Retrain the SVM model with scaled data

"""

# Create an instance of the SVM model
svm_model = SVC()
svm_model.fit(X_train_scaled, y_train)

"""# Make predictions

"""

y_pred_svm_scaled = svm_model.predict(X_test_scaled)

"""#EDA

# 1. Initial Data Exploration
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split


# Create DataFrames for better visualization
df_train = pd.DataFrame(X_train, columns=[
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
])
df_test = pd.DataFrame(X_test, columns=df_train.columns)

print("Initial Data Overview")
print(df_train.describe())
print(df_train.info())
print(df_train.head())

"""# 2. Feature Distribution Analysis Before Scaling

"""

plt.figure(figsize=(14, 12))
for i, col in enumerate(df_train.columns, 1):
    plt.subplot(4, 4, i)
    sns.histplot(df_train[col], kde=True, bins=30)
    plt.title(f'Distribution of {col}')
    plt.tight_layout()
plt.show()

"""# 3. Apply Feature Scaling

"""

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""# Create DataFrames for scaled data

"""

df_train_scaled = pd.DataFrame(X_train_scaled, columns=df_train.columns)
df_test_scaled = pd.DataFrame(X_test_scaled, columns=df_train.columns)

"""
# Plot feature distributions after scaling
"""

plt.figure(figsize=(14, 12))
for i, col in enumerate(df_train_scaled.columns, 1):
    plt.subplot(4, 4, i)
    sns.histplot(df_train_scaled[col], kde=True, bins=30)
    plt.title(f'Distribution of {col} (scaled)')
    plt.tight_layout()
plt.show()

"""# 4. Model Performance Comparison

# Initialize and train the SVM model
"""

svm_model = SVC()
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)

"""# Evaluate the model before scaling and after scaling

"""

#Evaluate the model before scaling

accuracy_svm = accuracy_score(y_test, y_pred_svm)
conf_matrix_svm = confusion_matrix(y_test, y_pred_svm)
class_report_svm = classification_report(y_test, y_pred_svm)

print("Model Performance Before Scaling")
print(f'Accuracy: {accuracy_svm:.2f}')
print('Confusion Matrix:\n', conf_matrix_svm)
print('Classification Report:\n', class_report_svm)

# Retrain the SVM model with scaled data
svm_model.fit(X_train_scaled, y_train)
y_pred_svm_scaled = svm_model.predict(X_test_scaled)

# Evaluate the model after scaling
accuracy_svm_scaled = accuracy_score(y_test, y_pred_svm_scaled)
conf_matrix_svm_scaled = confusion_matrix(y_test, y_pred_svm_scaled)
class_report_svm_scaled = classification_report(y_test, y_pred_svm_scaled)

print("Model Performance After Scaling")
print(f'Accuracy: {accuracy_svm_scaled:.2f}')
print('Confusion Matrix:\n', conf_matrix_svm_scaled)
print('Classification Report:\n', class_report_svm_scaled)

"""#Explanation of the EDA Steps
**Initial Data Exploration:**

**Descriptive Statistics:** Shows basic statistics (mean, std, min, max) for each feature.
Info and Head: Provides information about data types, non-null counts, and a preview of the first few rows.
Feature Distribution Analysis Before Scaling:

**Histograms with KDE:** Visualizes the distribution of each feature before scaling, which helps in understanding the range and spread of feature values.
Feature Scaling Impact:

**Scaling:** Applies StandardScaler to standardize features so they have a mean of 0 and a standard deviation of 1.
Post-Scaling Histograms: Plots the distributions of features after scaling, verifying that they are standardized.   
**Model Performance Comparison:**

Model Training and Evaluation (Before Scaling): Trains an SVM model on the original data and evaluates its performance.
Model Training and Evaluation (After Scaling): Trains an SVM model on the scaled data and evaluates its performance.
Comparison: Compares the accuracy, confusion matrix, and classification report before and after scaling to assess the impact of scaling on model performance.
This comprehensive EDA helps you understand the data distributions, the effect of scaling, and how feature scaling impacts the performance of your SVM model.
"""