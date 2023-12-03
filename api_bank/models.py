from django.db import models
from sklearn.neural_network import MLPRegressor
import pandas as pd
import os
class MLModel(models.Model):
    age = models.IntegerField()
    salary = models.FloatField()
    amount_of_finished_credits = models.IntegerField()
    amount_of_unfinished_credits = models.IntegerField()
    education_degree = models.IntegerField()
    marriage_status = models.IntegerField()
    years_of_work_experience = models.IntegerField()
    desired_credit = models.IntegerField()
    desired_credit_age = models.IntegerField()
    credit_payability = models.BooleanField()

def predict_credit_payability_model(data_frame):
    model_path = os.path.join(os.path.dirname(__file__), 'models/neural_network_model.pkl')
    model = MLPRegressor()
    model = model.fit(X, y)
    
    # Convert the data_frame to a pandas DataFrame
    input_df = pd.DataFrame(data_frame, columns=['age', 'salary', 'amount_of_finished_credits', 'amount_of_unfinished_credits', 'education_degree', 'marriage_status', 'years_of_work_experience', 'desired_credit', 'desired_credit_age'])
    
    prediction = model.predict(input_df)
    print(prediction[0])
    return prediction[0]
# Create your models here.
