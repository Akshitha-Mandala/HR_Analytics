import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler


df = pd.read_csv(r'C:\Users\lalit\OneDrive\ACHI_BCOM\HR_dataset(in) (1).csv')
print(df.head())
print(df.info())
print(df.isnull().sum())
print('\n')

# Checking Attrition count
print(df['Attrition'].value_counts())
print(df['Attrition'].value_counts(normalize=True)*100)
print('\n')

# Department wise Attrition
print(pd.crosstab(df['Department'], df['Attrition']))
print(pd.crosstab(df['OverTime'],df['Attrition']))
print('\n')

# Salaries Analysis
print(df.groupby('Attrition')['MonthlyIncome'].mean())
print('\n')

# Job Satisfaction Analysis
print(pd.crosstab(df['JobSatisfaction'], df['Attrition']))
print('\n')

# Age Grouping
df['AgeGroup'] = pd.cut(
    df['Age'],
    bins=[18,30,40,50,60],
    labels=['18-30','31-40','41-50','51-60'])
print(pd.crosstab(df['AgeGroup'], df['Attrition']))
print('\n')

# Correlation Analysis
correlation_matrix = df.corr(numeric_only=True)
print('\n')

# Visualizing Correlation Matrix
plt.figure(figsize=(15,10))
corr = df.corr(numeric_only=True)
sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

# Analyze Attrition Distribution
sns.countplot(x='Attrition', data=df)
plt.title("Employee Attrition Distribution")
plt.show()

# Department-wise Attrition
sns.countplot(x='Department', hue='Attrition', data=df)
plt.xticks(rotation=15)
plt.title("Department-wise Attrition")
plt.show()

# Overtime vs Attrition
sns.countplot(x='OverTime',hue='Attrition',data=df)
plt.title("Overtime vs Attrition")
plt.show()

# Salary vs Attrition
sns.boxplot(x='Attrition',y='MonthlyIncome',data=df)
plt.title("Monthly Income vs Attrition")
plt.show()

# Job Satisfaction vs Attrition
sns.countplot(x='JobSatisfaction',hue='Attrition',data=df)
plt.title("Job Satisfaction vs Attrition")
plt.show()

# Age Group Analysis
sns.countplot(x='AgeGroup',hue='Attrition',data=df)
plt.title("Age Group vs Attrition")
plt.show()

#df.to_csv("HR_PowerBI.csv", index=False)

# Convert categorical columns
df = pd.get_dummies(df, drop_first=True)

# Separate features and target
X = df.drop('Attrition_Yes', axis=1)
y = df['Attrition_Yes']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Train model
model = LogisticRegression(max_iter=5000)
model.fit(X_train_scaled, y_train)
pred = model.predict(X_test_scaled)
print(classification_report(y_test, pred))

# Train Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
pred = model.predict(X_test)

# Check Accuracy
print("Accuracy:", accuracy_score(y_test, pred))

# Confusion Matrix
cm = confusion_matrix(y_test, pred)
sns.heatmap(cm,
            annot=True,
            fmt='d',
            cmap='Blues')
plt.title("Confusion Matrix")
plt.show()
