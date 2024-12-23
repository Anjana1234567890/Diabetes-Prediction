# -- coding: utf-8 --
"""
Created on Tue Nov 12 13:29:13 2024

@author: Anjana
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model
diabetes_model = pickle.load(open('C:/Users/Anjana/Desktop/multiple disease prediction/diabetes_model (1).sav', 'rb'))








#sidebar for navigation
with st.sidebar:
    selected = option_menu('Disese prediction system',
                           ['Diabetes Prediction'],
                           
                           icons = ['Activity'],
                           
                           default_index=0)
    
      
    
#diabetes prediction page
if(selected =='Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    
    #getting the input data from the user
    #columns for input feilds
    
    col1, col2, col3 = st.columns(3)
    
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')
    

#code for prediction
    diab_diagnosis = ''
    
#creating a button for prediction
    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

        
        
        
        
        
        