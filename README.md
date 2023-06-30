# Bank_Customer_churn
Bank Customer Churn Prediction

## Step by step Documentation for the project
- [x] This document will take you through the summary of this project with a result at the rend
### Loading the libraries
- [x] Please check the requirements.txt file for the libraries used in the project.
### EDA.ipynb with code explanation
- This notebook contains the Exploratory Data Analysis of the dataset.
the definition of the columns are as follows:'
- RowNumber: Row Numbers from 1 to 10000
- CustomerId: Unique Ids for bank customer identification
- Surname: Customer's last name
- CreditScore: Credit score of the customer
- Age: Customer's age in years
- Tenure: Number of years for which the customer has been with the bank
- Balance: Bank balance of the customer
- NumOfProducts: Number of bank products the customer is utilising
- HasCrCard: Binary Flag for whether the customer holds a credit card with the bank or not
- IsActiveMember: Binary Flag for whether the customer is an active member with the bank or not
- EstimatedSalary: Estimated salary of the customer in Dollars
- churn : Binary flag 1 or 0
#### The Project contains the following sections:
- [x] Data Cleaning
- [x] Data Visualization
- [x] Data Preprocessing
- [x] Feature Selection
- [x] Model Building
- [x] Model Evaluation
- [x] Model Deployment
### Documentation for Model.py Deployment
- [x] This file contains the code for the deployment of the model using streamlit.
-[x] below is the import of the libraries used in the file.

```python
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import eli5
from eli5 import explain_weights, explain_prediction
```
- [x] Below we load xgboost model  using joblib.
```python
#load the xgboost model
model = joblib.load('xgb_model.pkl')
```	
 - [x] Call feature_names function to get the feature names.
```python
#call feature_names function to get the feature names
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
```
- [x] Below we create a dictionary of the input values.
```python
# create a dictionary of inputs
features = pd.Dataframe({'age':age, 'credit_score': credit_score,....})
```
the rest is history, do feel free to catch on the rest of the code in the file.

#### Preview of the app and predictions
![image](https://github.com/Mfundo-debug/Bank_Customer_churn/blob/main/pic.png)
![image](https://github.com/Mfundo-debug/Bank_Customer_churn/blob/main/pic_1.png)
### Conclusion
- [x] The model was deployed using streamlit.
- [x] The duration of the project was 3 hours.
- [x] Enjoy the app. pleae do leave a feedback.
- [x] Find here the link to the app https://bank-churn-customer.streamlit.app/
- [x] Thank you.