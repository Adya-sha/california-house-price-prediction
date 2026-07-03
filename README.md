# 🏠 California House Price Prediction using Linear Regression

## 📌 Project Overview

This project builds and evaluates a Linear Regression model to predict house prices using the California Housing dataset from Scikit-Learn.

The project demonstrates the complete machine learning workflow, including:
- Data Loading
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Model Training
- Model Evaluation
- Model Saving
- Interactive Prediction using Streamlit

---

## 📂 Dataset

- Source: California Housing Dataset (Scikit-Learn)
- Number of Samples: 20,640
- Number of Features: 8
- Target Variable: `MedHouseVal`

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Jupyter Notebook

---

## 📊 Machine Learning Workflow

1. Import Libraries
2. Load Dataset
3. Exploratory Data Analysis
4. Train-Test Split
5. Train Linear Regression Model
6. Evaluate Model
7. Save Model
8. Build Prediction App

---

## 📈 Evaluation Metrics

The trained Linear Regression model achieved the following performance on the test dataset:

| Metric | Value |
|---------|-------|
| Mean Absolute Error (MAE) | **0.5332** |
| Root Mean Squared Error (RMSE) | **0.7456** |
| R² Score | **0.5758** |

### Interpretation

- **MAE = 0.5332** means that, on average, the predicted house value differs from the actual value by about **0.53** (in the dataset's target units).
- **RMSE = 0.7456** indicates the model penalizes larger prediction errors more heavily.
- **R² = 0.5758** means the model explains approximately **57.6%** of the variation in house prices, making it a reasonable baseline model.

---

## 🚀 Run the Project

Clone the repository:

```bash
git clone https://github.com/Adya-sha/california-house-price-prediction.git
```

Install dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
california-house-price-prediction/
│
├── task1_ml_linear_regression.ipynb
├── california_house_model.pkl
├── app.py
├── README.md
└── .gitignore
```

---

## 👤 Author

Adyasha Sahu