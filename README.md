# HR_Analytics
# 📊 HR Analytics - Employee Attrition Prediction

## 📌 Project Overview

This project focuses on analyzing employee attrition data to understand the major factors influencing employee turnover and predict future attrition using Machine Learning.

The project combines **Python** for data analysis and machine learning with **Power BI** for building an interactive dashboard that provides actionable business insights.

---

## 🎯 Objectives

- Analyze employee attrition patterns.
- Identify factors affecting attrition such as:
  - Department
  - Overtime
  - Salary
  - Job Satisfaction
  - Age Group
- Build a Machine Learning model to predict employee attrition.
- Create an interactive Power BI dashboard for visualization and insights.

---

## 🛠️ Technologies Used

### Python Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

### Scikit-Learn Modules

- train_test_split
- LogisticRegression
- accuracy_score
- confusion_matrix
- classification_report

### Visualization Tool

- Power BI

---

## 📂 Dataset Information

- Dataset Size: **1470 employees**
- Total Features: **35**
- Target Variable: **Attrition**
  - Yes → Employee Left
  - No → Employee Stayed

---

## 📈 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Attrition Distribution
- Department-wise Attrition
- Overtime vs Attrition
- Salary vs Attrition
- Job Satisfaction Analysis
- Age Group Analysis
- Correlation Heatmap

### Key Findings

- Employees working overtime are more likely to leave the company.
- Lower monthly income is associated with higher attrition.
- Employees aged **18–30 years** have the highest attrition.
- Research & Development department has the highest attrition count.
- Employees with lower job satisfaction tend to leave more frequently.

---

## 🤖 Machine Learning

### Model Used

**Logistic Regression**

### Model Evaluation

The model was evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

### Results

| Metric | Value |
|--------|-------|
| Accuracy | **86.4%** |
| Precision (Attrition = Yes) | 0.57 |
| Recall (Attrition = Yes) | 0.41 |
| F1-Score (Attrition = Yes) | 0.48 |

---

## 📊 Power BI Dashboard

An interactive dashboard was created in Power BI with the following features:

### KPI Cards

- Total Employees
- Employees Left
- Attrition Rate
- Average Monthly Income

### Visualizations

- Department-wise Attrition
- Overtime vs Attrition
- Age Group vs Attrition
- Salary vs Attrition
- Job Satisfaction vs Attrition
- Attrition by Marital Status
- Gender-wise Attrition
- Attrition by Education Field

### Interactive Features

- Department Filter
- Gender Filter
- Marital Status Filter
- Education Field Filter
- Overtime Filter
- Job Role Filter
- Business Travel Filter

---

## 🚀 Future Improvements

- Implement Decision Tree and Random Forest models.
- Perform Feature Importance Analysis.
- Use SHAP values for model explainability.
- Deploy the model using Streamlit.

---

## ⭐ Conclusion

This project helped me gain practical experience in:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Machine Learning using Logistic Regression
- Data Visualization with Python
- Interactive Dashboard Development using Power BI

The insights generated from this project can help organizations understand employee attrition patterns and make data-driven HR decisions.

---

⭐ If you found this project useful, feel free to give it a star!
