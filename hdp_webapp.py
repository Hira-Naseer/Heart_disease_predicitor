# -*- coding: utf-8 -*-
"""HDP_webapp.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1roid5F1-fzLHwmLxOFPdazTGBp5vjoqQ
"""

import streamlit as st
import numpy as np
import pickle

loaded_model=pickle.load(open('trained_model.sav','rb'))
df=pickle.load(open('df.sav','rb'))

def HDP_Prediction(input_data):

   # input_data=(33,0,0,1,14,61,0,0,30,1,25,1,2,2)
   #change input data to munpy array
   input_data_as_numpy_array= np.array(input_data)
   #reshape 
   input_data_reshape=input_data_as_numpy_array.reshape(1,14)
   #predict
   prediction=loaded_model.predict(input_data_reshape)
   print(prediction)
   return prediction[0]
   # if(prediction[0]==0):
   #
   #    st.write("Person do not have a heart disease")
   # else:
   #    print("Person have a heart disease .")

def main():
    
  #title
  st.title('Heart Disease Prediction System')
  
  age=st.number_input('What is your age',min_value=1)
  sex=st.selectbox('Enter your sex',df['sex'].unique())
  dataset=st.selectbox('Enter your dataset',df['dataset'].unique())
  cp=st.selectbox('Enter your cp type',df['cp'].unique())
  trestbps=st.number_input('Enter your trestbps',min_value=0,max_value=49)
  chol=st.number_input('Enter your cholestrol',min_value=0,max_value=152)
  fbs=st.selectbox('Enter your fbs',df['fbs'].unique())
  restecg=st.selectbox('Enter your restecg',df['restecg'].unique())
  thalch=st.number_input('Enter your thalch',min_value=0,max_value=91)
  exang=st.selectbox('Enter your exang',df['exang'].unique())
  oldpeak=st.number_input('Enter your oldpeak',min_value=0,max_value=39)
  slope=st.selectbox('Enter your slope',df['slope'].unique())
  ca=st.selectbox('Enter your ca',df['ca'].unique())
  thal=st.selectbox('Enter your thal',df['thal'].unique())


  if st.button("Heart Disease Diagnosis Result"):
     diagnosed_result=HDP_Prediction([age,sex,dataset,cp,trestbps,chol,fbs,restecg,thalch,exang,oldpeak,slope,ca,thal])

     if diagnosed_result==0:
        st.success('Person do not have a heart disease')
     else:
        st.success('Person have a heart disease.')


if __name__ == '__main__':
  main()

