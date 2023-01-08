from django.urls import path, include
from . import views



urlpatterns = [
    path('Income/', views.submit_income, name='submit_income'),
    path('Exopense/', views.submit_expense, name='submit_expense'),
    path('register/', views.register, name='views.register'),
    path('', views.index, name='views.index'),

]
