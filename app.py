import streamlit as st
import pandas as pd
import joblib
import warnings
warnings.filterwarnings("ignore")

model = joblib.load("credit_model.pkl")
encoders = joblib.load("encoders.pkl")

le_housing = encoders["housing"]
le_job = encoders["job"]
le_sex = encoders["sex"]
le_saving = encoders["saving"]
le_checking = encoders["checking"]
le_Purpose = encoders["Purpose"]



st.title("Credit Risk Prediction")
st.write("Provide the following details to predict credit risk:")
age=st.number_input("Age",18,100,30)
sex=st.selectbox("Sex",["male","female"])
job=st.selectbox("Job",[0, 1, 2, 3])
housing=st.selectbox("Housing",["own","rent","free"])
saving_accounts=st.selectbox("Saving Accounts",["little","moderate","rich","quite rich"])
checking_account=st.selectbox("Checking Account",["little","moderate","rich"])                  
credit_amount=st.number_input("Credit Amount",100,100000,5000)
duration=st.number_input("Duration (in months)",4,72,12)
Purpose=st.selectbox("Purpose",["car","furniture/equipment","radio/TV","education","business","domestic appliances","repairs","vacation/others"])
if st.button("Predict Credit Risk"):
    input_data=pd.DataFrame({
        'Age':[age],
        'Sex':[sex],
        'Job':[job],
        'Housing':[housing],
        'Saving accounts':[saving_accounts],
        'Checking account':[checking_account],
        'Credit amount':[credit_amount],
        'Duration':[duration],
        'Purpose':[Purpose]
    })
    input_data["Housing"] = le_housing.transform(input_data["Housing"])
    input_data["Job"] = le_job.transform(input_data["Job"])
    input_data["Sex"] = le_sex.transform(input_data["Sex"])
    input_data["Saving accounts"] = le_saving.transform(input_data["Saving accounts"])
    input_data["Checking account"] = le_checking.transform(input_data["Checking account"])
    input_data["Purpose"] = le_Purpose.transform(input_data["Purpose"])
    prediction=model.predict(input_data)[0]
    risk="Low Risk (Good)" if prediction==1 else "High Risk (Bad)"
    st.success(f"Predicted Credit Risk: {risk}")    
