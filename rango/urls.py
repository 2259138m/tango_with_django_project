# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:09:15 2021

@author: lewis
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]