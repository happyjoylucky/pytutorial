from django.urls import path
from . import views

app_name = 'stockexample'

urlpatterns = [
    path('', views.stock, name='stock'),
]

