from django.urls import path
from . import views

app_name = 'practice03'


urlpatterns = [
    path('', views.post_list, name='post_list'),
]