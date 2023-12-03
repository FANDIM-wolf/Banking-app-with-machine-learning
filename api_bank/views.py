from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import predict_credit_payability_model  # Import the predict_credit_payability function from models
import pandas as pd
from sklearn.neural_network import MLPRegressor
import os
import joblib
@api_view(['POST'])
def predict_credit_payability(request):
    data = request.data 
    age = data["age"]
    salary = data["salary"]
    amount_of_finished_credits = data["amount_of_finished_credits"]
    amount_of_unfinished_credits = data["amount_of_unfinished_credits"]
    education_degree = data["education_degree"]
    marriage_status = data["marriage_status"]
    years_of_work_experience = data["years_of_work_experience"]
    desired_credit = data["desired_credit"]
    desired_credit_age = data["desired_credit_age"]
    
    # Create a data frame from the input
    input_data = {
        'age': [age],
        'salary': [salary],
        'amount_of_finished_credits': [amount_of_finished_credits],
        'amount_of_unfinished_credits': [amount_of_unfinished_credits],
        'education_degree': [education_degree],
        'marriage_status': [marriage_status],
        'years_of_work_experience': [years_of_work_experience],
        'desired_credit': [desired_credit],
        'desired_credit_age': [desired_credit_age]
    }
    input_df = pd.DataFrame(input_data)
   
    # Load the pre-trained model
    model_path = os.path.join(os.path.dirname(__file__), 'models/random_forest_model.pkl')
    model = joblib.load(model_path)

    # Make the prediction
    prediction = model.predict(input_df)
    predicted_credit_payability = prediction[0]

    return Response({'predicted_credit_payability': predicted_credit_payability ,'salary': salary })
# Create your views here.
