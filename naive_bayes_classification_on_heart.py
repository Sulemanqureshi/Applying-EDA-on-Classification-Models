# -*- coding: utf-8 -*-
"""Naive Bayes Classification on heart.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YKVqa9K3hoWO_dw7e7roDvnULxu-QrTV

#Naive Bayes Classification

---

##Import Libraries
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

"""#Load the Dataset"""

df = pd.read_csv('heart.csv')

"""# Split the data into features (X) and target (y)"""

X = df.drop('target', axis=1)
y = df['target']

"""#Train-Test Split"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""# Feature Scaling (Optional for Decision Tree, but we include it for consistency)

"""

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""# Initialize the Naive Bayes model

"""

nb = GaussianNB()

"""# Train the model and make Predication"""

nb.fit(X_train_scaled, y_train)

y_pred_nb = nb.predict(X_test_scaled)

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
    sns.histplot(df_train[col], kde=True, bins=30, color='blue', label='Training Set')
    sns.histplot(df_test[col], kde=True, bins=30, color='red', label='Testing Set')
    plt.title(f'Distribution of {col}')
    plt.legend()
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
    sns.histplot(df_train_scaled[col], kde=True, bins=30, color='blue', label='Training Set (scaled)')
    sns.histplot(df_test_scaled[col], kde=True, bins=30, color='red', label='Testing Set (scaled)')
    plt.title(f'Distribution of {col} (scaled)')
    plt.legend()
    plt.tight_layout()
plt.show()

"""# 4. Model Training and Evaluation


"""

y_pred_nb = nb.predict(X_test_scaled)  # Generate predictions

# Evaluate the model
accuracy_nb = accuracy_score(y_test, y_pred_nb)
conf_matrix_nb = confusion_matrix(y_test, y_pred_nb)
class_report_nb = classification_report(y_test, y_pred_nb)

# Print the evaluation results
print("Model Performance")
print(f'Accuracy: {accuracy_nb:.2f}')
print('Confusion Matrix:\n', conf_matrix_nb)
print('Classification Report:\n', class_report_nb)

"""# Visualizing Model Performance

"""

# Plot Confusion Matrix
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix_nb, annot=True, fmt='d', cmap='Blues', xticklabels=['Class 0', 'Class 1'], yticklabels=['Class 0', 'Class 1'])
plt.title('Confusion Matrix for Naive Bayes')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

"""# Feature Importances (Naive Bayes does not have feature importances directly, but you can visualize feature means)

"""

# Verify the feature lengths
num_features = X_train.shape[1]  # Get number of features directly from X_train

# Ensure that all arrays have the same length
assert len(X_train.mean(axis=0)) == num_features, "Mismatch in number of features for X_train"
assert len(X_test.mean(axis=0)) == num_features, "Mismatch in number of features for X_test"
assert len(X_train_scaled.mean(axis=0)) == num_features, "Mismatch in number of features for X_train_scaled"
assert len(X_test_scaled.mean(axis=0)) == num_features, "Mismatch in number of features for X_test_scaled"

# Create the DataFrame
# Get feature names directly from X_train if it has column names
if hasattr(X_train, 'columns'):
    feature_names = X_train.columns
else:
    feature_names = [f"Feature {i}" for i in range(num_features)]  # Use generic names if no column names

feature_means = pd.DataFrame({
    'Feature': feature_names,
    'Mean (Training Set)': X_train.mean(axis=0),
    'Mean (Testing Set)': X_test.mean(axis=0),
    'Mean (Scaled Training Set)': X_train_scaled.mean(axis=0),
    'Mean (Scaled Testing Set)': X_test_scaled.mean(axis=0)
})

# Plot feature means comparison
plt.figure(figsize=(14, 10))
feature_means.set_index('Feature').plot(kind='bar', figsize=(14, 8))
plt.title('Feature Means Comparison')
plt.ylabel('Mean Value')
plt.xlabel('Feature')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

"""**Explanation of Additional Visualizations**   
Feature Distribution Analysis Before Scaling:

**Histograms with KDE:** Visualize the distributions of each feature in both the training and testing sets before scaling. This helps identify any potential distribution differences between the two datasets.
Feature Distribution Analysis After Scaling:

**Histograms with KDE**: Visualize the distributions of each feature after scaling for both the training and testing sets. This helps ensure that scaling was applied consistently and observe the standardized feature distributions.
Confusion Matrix:

**Heatmap of Confusion Matrix:** Displays the confusion matrix for the Naive Bayes model's predictions. This helps visualize the number of true positives, true negatives, false positives, and false negatives.
Feature Means Comparison:

**Bar Plot of Feature Means**: Shows the means of features in the training and testing sets before and after scaling. This helps compare the central tendencies of features and ensures that scaling had the intended effect.
These visualizations provide additional insights into the data and the performance of the Naive Bayes model, helping you understand both the features and the model's predictions.
"""