# Credit Risk Prediction

A machine learning project that predicts customer credit risk using the German Credit Dataset. The model classifies applicants as **Low Risk (Good)** or **High Risk (Bad)** based on financial and demographic information.

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-red)](https://credit-risk-prediction.streamlit.app)

## Features

- Data preprocessing and feature encoding
- Logistic Regression-based prediction model
- Streamlit web application
- Real-time credit risk prediction
- User-friendly interface

## Dataset

This project uses the German Credit Dataset.

### Features Used

- Age
- Sex
- Job
- Housing
- Saving Account Status
- Checking Account Status
- Credit Amount
- Duration
- Purpose

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## Project Structure

```text
credit-risk-prediction/
│
├── app.py
├── Credit_risk.ipynb
├── german_credit_data.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/credit-risk-prediction.git
cd credit-risk-prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

## Model

The project uses a **Logistic Regression Classifier** trained on the German Credit Dataset. Categorical features are encoded and preprocessed before prediction.

## How It Works

1. Enter customer details.
2. Features are encoded using trained encoders.
3. The Logistic Regression model processes the input.
4. The model predicts credit risk.
5. The result is displayed instantly.

## Output

The application predicts:

- ✅ Low Risk (Good)
- ⚠️ High Risk (Bad)

## Future Improvements

- Add multiple ML models for comparison
- Improve accuracy through hyperparameter tuning
- Deploy on Streamlit Cloud
- Add visualization dashboards
- Include probability-based risk scores

## Requirements

```text
streamlit
pandas
numpy
scikit-learn
joblib
```

Generate the complete requirements file using:

```bash
pip freeze > requirements.txt
```

## Author

**Pallavi B**


## License

This project is licensed under the MIT License.
