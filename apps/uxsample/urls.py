from django.urls import path

from . import views

app_name = 'uxsample'
urlpatterns = [
    path('', views.index, name='index'),
    path('blank/', views.blank, name='blank'),
    path('button/', views.button, name='button'),
    path('card/', views.card, name='card'),
    path('chart/', views.chart, name='chart'),
    path('findpasswd/', views.findpasswd, name='findpasswd'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('table/', views.table, name='table'),
    path('util_ani/', views.util_ani, name='util_ani'),
    path('util_border/', views.util_border, name='util_border'),
    path('util_color/', views.util_color, name='util_color'),
    path('util_other/', views.util_other, name='util_other'),
    path('404/', views.err404, name='err404'),
    # path('', views.index, name='index'),
]