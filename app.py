# -*- coding: utf-8 -*-
"""
Created on Sun June 05 15:01:17 2020

"""

import streamlit as st 
import pandas as pd
import numpy as np
#import matplotlib as plt
#from sklearn.ensemble import RandomForestClassifier
import matplotlib.image as mp
import pickle





st.title('Hello user')

# img = mp.imread("heart2.png")
# st.image(img)


st.sidebar.header('User, please give your inputs for the following:')

loaded_model1 = pickle.load(open('logistic_regression.pkl','rb'))


def user_input_features():
    BMI = st.sidebar.number_input('Insert your BMI',0,100)
    Smoking = st.sidebar.selectbox('Do you smoke?',["Yes","No"])
    AlcoholDrinking = st.sidebar.selectbox('Do you drink alcohol',["Yes","No"])
    Stroke = st.sidebar.selectbox("Did you ever have stroke before?",["Yes","No"])
    PhysicalHealth = st.sidebar.number_input("Insert your physical health status",0,30)
    MentalHealth = st.sidebar.number_input('Insert your mental health status',0,30)
    DiffWalking = st.sidebar.selectbox('Do you have different walking?',["Yes","No"])
    Sex = st.sidebar.selectbox('Select your sex',["Male","Female"])
    AgeCategory = st.sidebar.selectbox("Select the Age category",('55-59','80 or older','65-69','75-79','40-44','70-74','60-64','50-54','45-49','18-24','35-39','30-34','25-29'))
    Race = st.sidebar.selectbox("Select your race",('White','Black','Asian','American Indian/Alaskan Native','Other','Hispanic'))
    Diabetic = st.sidebar.selectbox('Are you diabetic',('Yes (during pregnancy)','Yes','No, borderline diabetes','No'))
    PhysicalActivity = st.sidebar.selectbox('Any physical activities?',["Yes","No"])
    GenHealth = st.sidebar.selectbox('Select your general health status',('Very good','Poor','Good','Fair','Excellent'))
    SleepTime = st.sidebar.number_input("Insert your sleep time",1,24)
    Asthma = st.sidebar.selectbox("Do you have asthma?",["Yes","No"])
    KidneyDisease = st.sidebar.selectbox("Do you have/had kidney disease?",["Yes","No"])
    SkinCancer = st.sidebar.selectbox("Do you have skin cancer?",["Yes","No"])
        
        
    data1 = {'BMI':BMI,
            'Smoking':Smoking,
            'AlcoholDrinking':AlcoholDrinking,
            'Stroke':Stroke,
            'PhysicalHealth':PhysicalHealth,
            'MentalHealth':MentalHealth,
            'DiffWalking':DiffWalking,
            'Sex':Sex,
            'AgeCategory':AgeCategory,
            'Race':Race,
            'Diabetic':Diabetic,
            'PhysicalActivity':PhysicalActivity,
            'GenHealth':GenHealth,
            'SleepTime':SleepTime,
            'Asthma':Asthma,
            'KidneyDisease':KidneyDisease,
            'SkinCancer':SkinCancer}
    features = pd.DataFrame(data1,index = [0])
    return features 



df = user_input_features()
st.subheader('User inserted values')
st.write(df)

#data = pd.read_csv("heart_2020_cleaned.csv")
cls = [["Smoking","AlcoholDrinking","Stroke","DiffWalking","PhysicalActivity","Asthma","KidneyDisease","SkinCancer"]]

for a in cls:
    for i in df[a]:
        if i == "Yes":
            df[a] = 1
        else:
            df[a] = 0

for i in df["Diabetic"]:
    if i == "No":
        df["Diabetic"] = 0
    elif i == "No, borderline diabetes":
        df["Diabetic"] = 1
    elif i == "Yes":
        df["Diabetic"] = 2
    else:
        df["Diabetic"] = 3

for i in df["GenHealth"]:
    if i == "Excellent":
        df["GenHealth"] = 0
    elif i == "Fair":
        df["GenHealth"] = 1
    elif i == "Good":
        df["GenHealth"] = 2
    elif i == "Poor":
        df["GenHealth"] = 2
    else:
        df["GenHealth"] = 3

for i in df["Sex"]:
    if i == "Male":
        df["Sex"] = 1
    else:
        df["Sex"] = 0

for i in df["AgeCategory"]:
    if i == "18-24":
        df["AgeCategory"] = 0
    elif i == "25-29":
        df["AgeCategory"] = 1
    elif i == "30-34":
        df["AgeCategory"] = 2
    elif i == "35-39":
        df["AgeCategory"] = 3
    elif i == "40-44":
        df["AgeCategory"] = 4
    elif i == "45-49":
        df["AgeCategory"] = 5
    elif i == "50-54":
        df["AgeCategory"] = 6
    elif i == "55-59":
        df["AgeCategory"] = 7
    elif i == "60-64":
        df["AgeCategory"] = 8
    elif i == "65-69":
        df["AgeCategory"] = 9
    elif i == "70-74":
        df["AgeCategory"] = 10
    elif i == "75-79":
        df["AgeCategory"] = 11
    else:
        df["AgeCategory"] = 12


race= ["American Indian/Alaskan Native","Asian","Black","Hispanic","Other","White"]

for i in df["Race"]:
    if i == race[0]:
        df["Race"] = 0
    elif i == race[1]:
        df["Race"] = 1
    elif i == race[2]:
        df["Race"] = 2
    elif i == race[3]:
        df["Race"] = 3
    elif i == race[4]:
        df["Race"] = 4
    else:
        df["Race"] = 5


predictions = loaded_model1.predict(df)


st.subheader('Predicted Result')




# Create a button in the UI for making predictions
if st.button('Predict'):
    predictions = loaded_model1.predict(df)
    st.subheader('Predicted Result')

    # Function to determine the result message based on the prediction
    def result(predictions):
        if predictions == 0:
            return "You do not have a heart disease."
        else:
            return "Heart disease detected"

    # Call the result function and store the result
    result_message = result(predictions[0])

    # Display the result message
    st.write(result_message)






#prediction = loaded_model1.predict(df)
#prediction_proba = loaded_model1.predict_proba(df)

#st.subheader('Prediction Probability')
#st.write(prediction_proba)

#st.subheader('Predicted Result')
#if btn is True:
#    st.write('Heart disease detected' if prediction_proba[0][1] > 0.5 else 'You do not have a heart disease')
