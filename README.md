# 🌿 Bio-Oil Yield Prediction using Machine Learning

An end-to-end Machine Learning project that predicts **Bio-Oil Yield (%)** obtained from biomass pyrolysis using physicochemical properties of biomass and process parameters.

The project covers the complete ML lifecycle from data preprocessing to model deployment with **Streamlit**.

---

## 📌 Project Overview

Bio-oil is an important renewable energy source produced through biomass pyrolysis. Accurately predicting bio-oil yield helps optimize the pyrolysis process and improve biofuel production.

This project compares multiple regression algorithms and deploys the best-performing model as an interactive web application.

---

## 🚀 Features

- Data Cleaning
- Missing Value Imputation
- Exploratory Data Analysis (EDA)
- Feature Engineering
- One-Hot Encoding
- Model Training
- Hyperparameter Tuning
- SHAP Explainability
- Streamlit Web Application
- Download Prediction Results

---

## 📊 Dataset

The dataset contains biomass characteristics and pyrolysis operating conditions.

### Features

| Feature | Description |
|----------|-------------|
| Biomass Species | Type of biomass |
| Moisture | Moisture (%) |
| Ash | Ash Content (%) |
| Volatile Matter | VM (%) |
| Fixed Carbon | FC (%) |
| Carbon | Carbon (%) |
| Hydrogen | Hydrogen (%) |
| Oxygen | Oxygen (%) |
| Nitrogen | Nitrogen (%) |
| Particle Size | mm |
| Temperature | °C |
| Heating Rate | °C/min |
| Flow Rate | mL/min |
| Biochar Yield | % |
| Gas Yield | % |

Target:

- **Bio-Oil Yield (%)**

---

# Data Preprocessing

The following preprocessing steps were performed:

- Removed invalid values
- Converted string values into numerical values
- Fixed inconsistent formatting
- Handled missing values
- Mean Imputation
- Median Imputation
- One-Hot Encoding for Biomass Species
- Feature Scaling where required

---

# Exploratory Data Analysis

Performed:

- Missing Value Heatmap
- Correlation Matrix
- Distribution Plots
- Boxplots
- Outlier Analysis
- Feature Statistics

---

# Machine Learning Models

The following models were trained and compared:

- Linear Regression
- Random Forest
- XGBoost
- LightGBM
- CatBoost
- Neural Network (MLP)

---

# Model Performance

| Model | MAE | RMSE | Test R² |
|------|------:|------:|------:|
| **CatBoost** | **1.81** | **2.38** | **0.9589** |
| LightGBM | 1.90 | 2.57 | 0.9519 |
| XGBoost | 1.70 | 2.63 | 0.9497 |
| Random Forest | 2.24 | 3.36 | 0.9177 |
| Neural Network | 1.92 | 3.68 | 0.9015 |
| Linear Regression | 3.85 | 5.92 | 0.7454 |

---

# Best Model

🏆 **CatBoost Regressor**

Performance

- R² Score : **95.89%**
- MAE : **1.81**
- RMSE : **2.38**

---

# Explainable AI

The model was interpreted using SHAP.

Generated explanations include:

- SHAP Summary Plot
- SHAP Waterfall Plot
- Feature Importance Analysis

Top influential features:

- Carbon
- Oxygen
- Nitrogen
- Volatile Matter
- Moisture
- Temperature

---

# Streamlit Application

The trained CatBoost model was deployed using Streamlit.

Features:

- Interactive UI
- Biomass Species Selection
- Input Validation
- Real-Time Prediction
- Feature Importance
- Download Prediction Results

---

# Project Structure

```
bio-oil-yield-prediction/

│

├── app.py

├── requirements.txt

├── README.md

├── models/

│ ├── catboost_model.pkl

│ └── feature_names.pkl

├── notebooks/

├── data/

│ ├── raw/

│ └── processed/

├── results/

└── images/
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/bio-oil-yield-prediction.git
```

Move into project

```bash
cd bio-oil-yield-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

# Future Improvements

- Deep Learning Models
- AutoML Integration
- Real-Time Sensor Data
- Cloud Deployment
- API Integration

---

# Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- CatBoost
- LightGBM
- XGBoost
- SHAP
- Matplotlib
- Streamlit

---

# Author

**Nupur Sarkar**

Associate Software Development Engineer

AI & Machine Learning Enthusiast
