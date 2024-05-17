from django.urls import path

from .views import (LSTMInputView, calculate_risk, daily_return_view,
                    get_risk_coefficients, moving_average_view,
                    predict_stock_price)

urlpatterns = [
    path('predict_lstm/', LSTMInputView.as_view(), name='predict_lstm'),
    path('moving-average/', moving_average_view, name='moving_average'),
    path('daily-return/', daily_return_view, name='daily_return'),
    path('risk_coefficients/', get_risk_coefficients, name='risk_coefficients'),
    path('calculate_risk/', calculate_risk, name='calculate_risk'),
    path('predict_stock_price/', predict_stock_price, name='predict_stock_price'),

]
