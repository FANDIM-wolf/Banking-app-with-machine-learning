from django.urls import path
from . import views
urlpatterns = [
    path('predict-credit-payability/', views.predict_credit_payability, name='predict-credit-payability'),
    # Add other URL patterns for your app
]