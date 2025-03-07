# **Job Salary Prediction in the CSE Field**  

## **Project Description**  
This project focuses on developing a **machine learning model** to predict salaries in the **computer science and engineering (CSE) field**. The objective is to utilize various job-related features to estimate salary levels accurately.  

## **Dataset & Features**  
The dataset includes multiple attributes related to job positions, employee experience, and industry trends. Key features include:  

- **Job Title:** e.g., Software Developer, Data Scientist  
- **Required Experience:** Categorized into different experience levels  
- **Industry Sector:** Technology  
- **Job Demand:** Trends indicating job market growth  
- **Work Model:** Onsite/Remote  
- **Overall Satisfaction:** Job satisfaction levels  
- **Job Switching Intent:** Whether an employee plans to switch jobs  

## **Data Processing**  
To improve model performance, extensive data preprocessing was performed:  

### **Preprocessing Techniques:**  
✔ **Handling Missing Values:** Mean/mode imputation and interpolation  
✔ **Normalization:** Min-Max Scaling & Standardization  
✔ **Categorical Encoding:** One-Hot Encoding & Label Encoding  
✔ **Feature Selection:**  
  - Correlation Analysis  
  - Recursive Feature Elimination (RFE)  
  - Forward & Backward Selection  

## **Machine Learning Models**  
Several machine learning algorithms were implemented and evaluated:  

- **Linear Regression**  
- **Logistic Regression**  
- **K-Nearest Neighbors (KNN)**  
- **Support Vector Machine (SVM)**  
- **Decision Tree**  

## **Results & Model Performance**  
The models were evaluated using multiple metrics, including accuracy, precision, recall, and F1-score. A summary of key results:  

| Model                | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |
|----------------------|-------------|--------------|------------|-------------|
| **Decision Tree**    | 39.5 - 65   | 62.4         | 65.6       | 63          |
| **KNN**             | 60          | 57           | 55.8       | 54.8        |
| **SVM**             | 40 - 54.4   | 37           | 28         | 29          |
| **Linear Regression** | 50.14       | Nan          | Nan        | Nan         |
| **Logistic Regression** | 63      | 64           | 58         | 63          |

## **Challenges & Discussion**  
📌 **Overfitting Issues:** Addressed through feature selection and cross-validation  
📌 **Feature Selection Variations:** Different selections impacted model accuracy  
📌 **Data Biasing:** Imbalanced distribution of job roles and experience levels  
📌 **Future Job Switching & Reason Analysis:** Explored factors influencing job transitions  

## **Technologies Used**  
- **Programming Language:** Python  
- **Libraries & Tools:** Pandas, NumPy, Scikit-learn, Matplotlib  

## **Future Improvements**  
🚀 Incorporate **Deep Learning** models like Neural Networks for better accuracy  
🚀 Improve **feature engineering** by adding external economic/job market data  
🚀 Expand dataset to include a broader industry scope  
