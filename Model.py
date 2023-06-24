import streamlit as st
import pandas as pd
import joblib

#load xgb model 
xgb_model = joblib.load('xgb_model.pkl')
st.title('Bank Customer Churn Prediction')
age = st.number_input('Age', min_value=18, max_value=100, value=18)
credit_score = st.number_input('Credit Score', min_value=300, max_value=850, value=300)
balance = st.number_input('Balance', min_value=0, max_value=250000, value=0)
num_of_products = st.number_input('Number of Products', min_value=1, max_value=4, value=1)
tenure = st.number_input('Tenure', min_value=0, max_value=10, value=0)
has_cr_card = st.selectbox('Has Credit Card', [0,1])
is_active_member = st.selectbox('Is Active Member', [0,1])
gender = st.selectbox('Gender',[0,1])
estimated_salary = st.number_input('Estimated Salary', min_value=0, max_value=250000, value=0)
geography = st.selectbox('Geography', ['France', 'Germany', 'Spain'])
#Preprocess user input
if geography == 'France':
    geography = 0
elif geography == 'Germany':
    geography = 1
else:
    geography = 2
#Create features from user input
features = pd.DataFrame({'CreditScore': credit_score, 'Age': age, 'Tenure': tenure, 'Balance': balance, 'NumOfProducts': num_of_products, 'HasCrCard': has_cr_card, 'IsActiveMember': is_active_member,'Gender':gender, 'EstimatedSalary': estimated_salary, 'Geography': geography}, index=[0])
#Predict
if st.button('Predict'):
    prediction = xgb_model.predict(features)
    if prediction == 0:
        st.write('Customer will not churn')
    else:
        st.write('Customer will churn')

