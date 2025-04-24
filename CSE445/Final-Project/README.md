# Bangladesh Job Salary Prediction – Predictive Analytics Project

## Project Overview
This project focuses on building a machine learning model to predict job salaries in Bangladesh based on real-world job market data. The full data lifecycle has been implemented: from data collection and preprocessing to model development and evaluation.

## Key Features

### Real-World Data Collection
- Collected and cleaned job market data reflecting various features such as job title, required experience, education, industry sector, and satisfaction levels.
- Hypothesis formed based on experience, satisfaction, and industry trends.

### Advanced Data Preprocessing
- Missing values handled using:
  - Mean/Mode imputation
  - KNN imputation
  - Interpolation
- Normalization using:
  - Min-Max Scaling
  - Standardization

### Categorical Encoding
- Applied:
  - One-Hot Encoding
  - Ordinal Encoding
  - Custom level encoding for target salary column

### Model Development
- Trained and evaluated the following models:
  - Linear Regression
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Decision Tree

### Exploratory Analysis & Visualization
- Used **Pandas** and **Matplotlib** to:
  - Visualize data distribution
  - Analyze feature importance
  - Explore joint plots and correlation matrices

### Model Evaluation
- Evaluated using:
  - Accuracy
  - Precision
  - Recall
  - F1 Score

| Model               | Accuracy (%) | Precision (%) | Recall (%) | F1 Score (%) |
|--------------------|--------------|----------------|-------------|---------------|
| Decision Tree       | 39.5 & 65     | 62.4           | 65.6        | 63            |
| KNN                 | 60           | 57             | 55.8        | 54.8          |
| SVM                 | 40 & 54.4     | 37             | 28          | 29            |
| Linear Regression   | 50.14        | NaN            | NaN         | NaN           |
| Logistic Regression | 63           | 64             | 58          | 63            |

## Challenges & Discussion
- **Overfitting** issues in some models
- **Data noise** affected prediction quality
- Feature selection played a critical role in model performance
- Analysis of job switching tendency and satisfaction

## Future Work
- Integrate external datasets for improved generalization
- Develop a **Streamlit** app for interactive predictions
- Enhance model interpretability and deployment readiness

## Technologies Used
- **Python**
- **Pandas**
- **scikit-learn**
- **Matplotlib**

---
Thank you for checking out our project! Feel free to contribute or reach out with feedback or suggestions.

> "Does anyone have any questions or suggestions?" — *Team 4, CSE445*

