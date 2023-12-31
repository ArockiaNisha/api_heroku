# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:53:09 2023

@author: nisha1999
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

class model_input(BaseModel):


  age : int
  sex : int 
  cp : int
  trestbps : int
  chol : int
  fbs : int
  restecg : int
  thalach : int
  exang : int
  oldpeak : float
  slope : int
  ca : int
  thal : int

#loading  the saved model
 
heart_disease_model =  pickle.load(open('heart_disease_model.pickle', 'rb')) 


@app.post('/heartdisease_prediction')
def heartdisease_pred(input_parameters : model_input ):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    
    age = input_dictionary['age']
    sex = input_dictionary['sex']
    cp = input_dictionary['cp']
    trestbps = input_dictionary['trestbps']
    chol = input_dictionary['chol']
    fbs = input_dictionary['fbs']
    restecg= input_dictionary['restecg']
    thalach = input_dictionary['thalach']
    exang = input_dictionary['exang']
    oldpeak = input_dictionary['oldpeak']
    slope = input_dictionary['slope']
    ca = input_dictionary['ca']
    thal = input_dictionary['thal']
    
    
    input_list = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
    prediction = heart_disease_model.predict([input_list])
    
    
    if (prediction[0] ==0):
        return "The person has no heart disease"
    else:
        return "The person has heart disease"
        