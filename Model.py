import streamlit as st
import pandas as pd
import joblib
import eli5
from eli5 import explain_weights, explain_prediction

#load xgb model 
xgb_model = joblib.load('xgb_model.pkl')
st.title('Bank Customer Churn Prediction')
age = st.number_input('Age', min_value=18, max_value=100, value=18)
credit_score = st.number_input('Credit Score', min_value=300, max_value=850, value=300)
balance = st.number_input('Balance', min_value=0, max_value=250000, value=0)
num_of_products = st.number_input('Number of Products', min_value=1, max_value=4, value=1)
tenure = st.number_input('Tenure', min_value=0, max_value=10, value=0)
has_cr_card = st.selectbox('Has Credit Card', ['Yes','No'])
is_active_member = st.selectbox('Is Active Member', ['Yes','No'])
gender = st.selectbox('Gender',['Male','Female'])
estimated_salary = st.number_input('Estimated Salary', min_value=0, max_value=250000, value=0)
geography = st.selectbox('Geography', ['France', 'Germany', 'Spain'])
#Preprocess user input
if has_cr_card == 'Yes':
    has_cr_card = 1
else:
    has_cr_card = 0
if is_active_member == 'Yes':
    is_active_member = 1
else:
    is_active_member = 0
if gender =='Male':
    gender = 0
else:
    gender = 1
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
    pred_prob = xgb_model.predict_proba(features)[0][1]
    if prediction == 0:
        st.write('Customer will not churn')
        st.write('Reason: Prediction Probability is {}'.format(pred_prob))
    else:
        st.write('Customer will churn')
        st.write('Reason: Prediction Probability is {}'.format(pred_prob))

        # Generate features weights
        eli5_weights = eli5.explain_weights(xgb_model)
        st.write('Feature Importance')
        st.write(eli5_weights)
        # Generate prediction explanation using eli5
        eli5_prediction = eli5.explain_prediction(xgb_model, features.iloc[0])
        st.write('Prediction Explanation')
        st.write(eli5_prediction)




